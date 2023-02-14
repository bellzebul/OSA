import subprocess
import PIL
from PIL import Image, ImageDraw, ImageFont
import psycopg2
import os
import datetime
from amount_students import fbme, fel, ipp, fti
from params import port, host, password, user, database_name, pass_to_Rfile, faculty, current_teacher, semestr


def set_image(save_prepod, akadem_kind, alternative_way, current_teacher, questions, faculty, amount, mode,
              n_students) -> None:
    backgrond: PIL.Image = Image.open('/Users/bellzebull/Documents/КПИ/OSA/back_osa.png')
    backgrond = backgrond.resize((1220, 1170))

    radar: PIL.Image = Image.open('/Users/bellzebull/Documents/КПИ/OSA/OSA_graphic/spyder.jpeg')
    radar_crop = radar.crop((120, 90, 390, 365))

    radar_crop: PIL.Image = radar_crop.resize((420, 420))
    backgrond.paste(radar_crop, (570, 120))

    comfort: PIL.Image = Image.open('/Users/bellzebull/Documents/КПИ/OSA/OSA_graphic/comfortable.jpg')
    comfort: PIL.Image = comfort.resize((290, 290))
    backgrond.paste(comfort, (450, 680))

    adaptiv: PIL.Image = Image.open('/Users/bellzebull/Documents/КПИ/OSA/OSA_graphic/adaptiv.jpg')
    adaptiv: PIL.Image = adaptiv.resize((290, 290))
    backgrond.paste(adaptiv, (850, 680))

    draw = ImageDraw.Draw(backgrond)
    if os.path.exists(f'/Users/bellzebull/Documents/КПИ/OSA/faculty_photos/{faculty}'):
        try:
            photo: PIL.Image = Image.open(
                f'/Users/bellzebull/Documents/КПИ/OSA/faculty_photos/{faculty}/{current_teacher}.jpg')
        except FileNotFoundError:
            photo: PIL.Image = Image.open('/Users/bellzebull/Documents/КПИ/OSA/cool_cat.jpg')
        photo: PIL.Image = photo.resize((310, 350))
    else:
        raise FileNotFoundError(f'Such files are not found')

    draw.rectangle((78, 78, 392, 432), fill='black')
    backgrond.paste(photo, (80, 80))

    headline = ImageFont.truetype('/Users/bellzebull/Documents/КПИ/OSA/fonts/NeueMachina-Bold.ttf', size=27)
    headline_1 = ImageFont.truetype('/Users/bellzebull/Documents/КПИ/OSA/fonts/NeueMachina-Medium.ttf', size=17)
    prsnt = ImageFont.truetype('/Users/bellzebull/Documents/КПИ/OSA/fonts/KyivTypeSans-Bold.ttf', size=40)
    prsnt_down = ImageFont.truetype('/Users/bellzebull/Documents/КПИ/OSA/fonts/NeueMachina-Medium.ttf', size=20)
    amount_font = ImageFont.truetype('/Users/bellzebull/Documents/КПИ/OSA/fonts/KyivTypeSans-Bold.ttf', size=30)
    axis_font = ImageFont.truetype('/Users/bellzebull/Documents/КПИ/OSA/fonts/NeueMachina-Light.ttf', size=16)

    background_color = (242, 241, 250)
    draw = ImageDraw.Draw(backgrond)
    name = current_teacher.split(' ')
    draw.rectangle((85, 443, 392, 500), fill=background_color)
    draw.rectangle((85, 500, 262, 525), fill=background_color)
    if (len(name[0]) + len(name[1]) + 1) >= 18:
        draw.text((78, 450), name[0], font=headline, fill=(0, 0, 0))
        draw.text((78, 477), name[1] + ' ' + name[2], font=headline, fill=(0, 0, 0))
    else:
        draw.text((78, 450), name[0] + ' ' + name[1], font=headline, fill=(0, 0, 0))
        draw.text((78, 477), name[2], font=headline, fill=(0, 0, 0))

    if mode == 'both':
        draw.text((78, 510), 'Лектор і практик', font=headline_1, fill=(96, 96, 96))
    if mode == 'lecture':
        draw.text((78, 510), 'Лектор', font=headline_1, fill=(96, 96, 96))
    if mode == 'practice':
        draw.text((78, 510), 'Практик', font=headline_1, fill=(96, 96, 96))

    draw.rectangle((103, 595, 340, 660), fill=background_color)

    red = (218, 60, 35)
    orange = (233, 113, 35)
    yellow = (230, 173, 22)
    green = (44, 174, 44)

    if 0 <= save_prepod < 25:
        if len(str(save_prepod)) == 1:
            draw.rectangle((200, 550, 260, 595), fill=background_color)
            draw.text((195, 550), str(save_prepod) + '%', font=prsnt, fill=red)
        elif len(str(save_prepod)) == 2:
            draw.rectangle((182, 550, 260, 595), fill=background_color)
            draw.text((175, 550), str(save_prepod) + '%', font=prsnt, fill=red)
    elif 25 <= save_prepod < 50:
        draw.rectangle((182, 550, 260, 595), fill=background_color)
        draw.text((175, 550), str(save_prepod) + '%', font=prsnt, fill=orange)
    elif 50 <= save_prepod <= 75:
        draw.rectangle((182, 550, 260, 595), fill=background_color)
        draw.text((175, 550), str(save_prepod) + '%', font=prsnt, fill=yellow)
    elif 75 <= save_prepod <= 100:
        if len(str(save_prepod)) == 2:
            draw.rectangle((182, 550, 260, 595), fill=background_color)
            draw.text((175, 550), str(save_prepod) + '%', font=prsnt, fill=green)
        elif len(str(save_prepod)) == 3:
            draw.rectangle((182, 550, 281, 595), fill=background_color)
            draw.text((169, 550), str(save_prepod) + '%', font=prsnt, fill=green)

    draw.text((90, 600), questions['10'], font=prsnt_down, fill=(0, 0, 0))

    draw.rectangle((103, 745, 370, 810), fill=background_color)

    if 0 <= akadem_kind < 25:
        if len(str(akadem_kind)) == 1:
            draw.rectangle((200, 700, 260, 745), fill=background_color)
            draw.text((195, 700), str(akadem_kind) + '%', font=prsnt, fill=red)
        elif len(str(akadem_kind)) == 2:
            draw.rectangle((182, 700, 260, 745), fill=background_color)
            draw.text((175, 700), str(akadem_kind) + '%', font=prsnt, fill=red)
    elif 25 <= akadem_kind < 50:
        draw.rectangle((182, 700, 260, 745), fill=background_color)
        draw.text((175, 700), str(akadem_kind) + '%', font=prsnt, fill=orange)
    elif 50 <= akadem_kind <= 75:
        draw.rectangle((182, 700, 260, 745), fill=background_color)
        draw.text((175, 700), str(akadem_kind) + '%', font=prsnt, fill=yellow)
    elif 75 <= akadem_kind <= 100:
        if len(str(akadem_kind)) == 2:
            draw.rectangle((182, 700, 260, 745), fill=background_color)
            draw.text((175, 700), str(akadem_kind) + '%', font=prsnt, fill=green)
        elif len(str(akadem_kind)) == 3:
            draw.rectangle((182, 700, 281, 745), fill=background_color)
            draw.text((169, 700), str(akadem_kind) + '%', font=prsnt, fill=green)

    draw.text((90, 750), questions['11'], font=prsnt_down, fill=(0, 0, 0))

    if mode != 'lecture':
        draw.rectangle((103, 895, 370, 960), fill=background_color)

        if 0 <= alternative_way < 25:
            if len(str(alternative_way)) == 1:
                draw.rectangle((200, 850, 260, 895), fill=background_color)
                draw.text((195, 850), str(alternative_way) + '%', font=prsnt, fill=red)
            elif len(str(alternative_way)) == 2:
                draw.rectangle((182, 850, 260, 895), fill=background_color)
                draw.text((175, 850), str(alternative_way) + '%', font=prsnt, fill=red)
        elif 25 <= alternative_way < 50:
            draw.text((175, 850), str(alternative_way) + '%', font=prsnt, fill=orange)
        elif 50 <= alternative_way <= 75:
            draw.rectangle((182, 850, 260, 895), fill=background_color)
            draw.text((175, 850), str(alternative_way) + '%', font=prsnt, fill=yellow)
        elif 75 <= alternative_way <= 100:
            if len(str(alternative_way)) == 2:
                draw.rectangle((182, 850, 260, 895), fill=background_color)
                draw.text((175, 850), str(alternative_way) + '%', font=prsnt, fill=green)
            elif len(str(alternative_way)) == 3:
                draw.rectangle((182, 850, 281, 895), fill=background_color)
                draw.text((169, 850), str(alternative_way) + '%', font=prsnt, fill=green)

        draw.text((90, 900), questions['12'], font=prsnt_down, fill=(0, 0, 0))

    # For correct display the number of voters
    if len(str(amount)) == 1:
        draw.rectangle((183, 1048, 270, 1080), fill=background_color)
        draw.rectangle((127, 1080, 320, 1105), fill=background_color)
        draw.text((175, 1050), str(amount) + '/' + str(n_students), font=amount_font, fill=(0, 0, 0))
    elif len(str(amount)) == 2:
        draw.rectangle((174, 1048, 283, 1080), fill=background_color)
        draw.rectangle((127, 1080, 320, 1105), fill=background_color)
        draw.text((165, 1050), str(amount) + '/' + str(n_students), font=amount_font, fill=(0, 0, 0))
    elif len(str(amount)) == 3:
        draw.rectangle((165, 1048, 290, 1080), fill=background_color)
        draw.rectangle((127, 1080, 320, 1105), fill=background_color)
        draw.text((155, 1050), str(amount) + '/' + str(n_students), font=amount_font, fill=(0, 0, 0))

    draw.text((120, 1085), "кількість опитаних", font=prsnt_down, fill=(0, 0, 0))

    font_color = (0, 0, 0)

    #  Radar-chart for both-type
    if mode == 'both':
        draw.rectangle((710, 77, 866, 91), fill=background_color)
        draw.text((705, 80), questions['1'], font=headline_1, fill=font_color)

        draw.rectangle((980, 159, 1084, 192), fill=background_color)
        draw.text((975, 162), questions['2'], font=headline_1, fill=font_color)

        draw.rectangle((1022, 367, 1150, 403), fill=background_color)
        draw.text((1017, 370), questions['3'], font=headline_1, fill=font_color)

        draw.rectangle((819, 573, 945, 590), fill=background_color)
        draw.text((815, 575), questions['4'], font=headline_1, fill=font_color)

        draw.rectangle((619, 562, 735, 600), fill=background_color)
        draw.text((615, 565), questions['5'], font=headline_1, fill=font_color)

        draw.rectangle((445, 364, 542, 405), fill=background_color)
        draw.text((435, 365), questions['6'], font=headline_1, fill=font_color)

        draw.rectangle((455, 159, 585, 200), fill=background_color)
        draw.text((450, 162), questions['7'], font=headline_1, fill=font_color)

    #  Radar-chart for lectors
    elif mode == 'lecture':
        draw.rectangle((735, 85, 846, 117), fill=background_color)
        draw.text((730, 90), questions['2'], font=headline_1, fill=font_color)

        draw.rectangle((995, 252, 1115, 282), fill=background_color)
        draw.text((987, 257), questions['3'], font=headline_1, fill=font_color)

        draw.rectangle((855, 516, 996, 530), fill=background_color)
        draw.text((850, 520), questions['4'], font=headline_1, fill=font_color)

        draw.rectangle((617, 518, 730, 548), fill=background_color)
        draw.text((610, 523), questions['5'], font=headline_1, fill=font_color)

        draw.rectangle((458, 240, 576, 287), fill=background_color)
        draw.text((455, 245), questions['7'], font=headline_1, fill=font_color)

    #  Radar-chart for practices
    elif mode == 'practice':
        draw.rectangle((735, 105, 890, 117), fill=background_color)
        draw.text((730, 110), questions['1'], font=headline_1, fill=font_color)

        draw.rectangle((995, 252, 1105, 282), fill=background_color)
        draw.text((987, 257), questions['2'], font=headline_1, fill=font_color)

        draw.rectangle((855, 516, 984, 546), fill=background_color)
        draw.text((850, 520), questions['3'], font=headline_1, fill=font_color)

        draw.rectangle((617, 518, 750, 533), fill=background_color)
        draw.text((610, 523), questions['4'], font=headline_1, fill=font_color)

        draw.rectangle((462, 240, 570, 287), fill=background_color)
        draw.text((455, 245), questions['6'], font=headline_1, fill=font_color)

    draw.text((735, 956), 'бал', font=axis_font, fill=(0, 0, 0))
    draw.text((400, 653), 'кількість\nголосів', font=axis_font, fill=(0, 0, 0))
    draw.rectangle((510, 975, 720, 1035), fill=background_color)
    draw.text((500, 980), questions['8'], font=headline_1, fill=(0, 0, 0))
    draw.text((1135, 956), 'бал', font=axis_font, fill=(0, 0, 0))
    draw.text((810, 653), 'кількість\nголосів', font=axis_font, fill=(0, 0, 0))
    draw.rectangle((897, 980, 1130, 1020), fill=background_color)
    draw.text((890, 985), questions['9'], font=headline_1, fill=(0, 0, 0))

    year = datetime.datetime.now().year

    draw.text((680, 1085), f'{semestr} семестр, {year - 1} - {year} рік', font=prsnt_down, fill=(200, 200, 200))

    backgrond.show()
    backgrond.save(f'/Users/bellzebull/Documents/КПИ/OSA/ready_photos/{mode}_{current_teacher}.png')

    # Remove diagrams from directory for avoiding mistakes

    os.remove(f'/Users/bellzebull/Documents/КПИ/OSA/OSA_graphic/adaptiv.jpg')
    os.remove(f'/Users/bellzebull/Documents/КПИ/OSA/OSA_graphic/comfortable.jpg')
    os.remove(f'/Users/bellzebull/Documents/КПИ/OSA/OSA_graphic/spyder.jpeg')


def amount_of_students(cursor) -> int:
    if faculty == 'fbme':
        faculty_dict = fbme
    elif faculty == 'fel':
        faculty_dict = fel
    elif faculty == 'ipp':
        faculty_dict = ipp
    elif faculty == 'fti':
        faculty_dict = fti

    cursor.execute(f"SELECT name, teachers FROM {faculty}.groups")
    rows = cursor.fetchall()

    groups_teachers = {rows[i][0]: [] for i in range(len(rows))}

    for j in range(len(rows)):
        for i in range(len(rows[j][1])):
            groups_teachers[rows[j][0]].append(rows[j][1][i]['full_name'])

    for i in range(len(rows)):
        groups_teachers[rows[i][0]] = list(set(groups_teachers[rows[i][0]]))

    all_teachers = [i for i in list(groups_teachers.values())]
    all_teachers = list(set([item for sublist in all_teachers for item in sublist]))

    teachers_groups = {all_teachers[i]: [] for i in range(len(all_teachers))}

    for teacher in all_teachers:
        for group in range(len(rows)):
            if teacher in groups_teachers[rows[group][0]]:
                teachers_groups[teacher].append(rows[group][0])
    potential_amount_votes = 0

    for group in teachers_groups[current_teacher]:
        try:
            potential_amount_votes += faculty_dict[group]
        except KeyError:
            potential_amount_votes += 0

    return potential_amount_votes


def getting_data(con, cursor, teachers, role) -> None:
    # Removing invalid role rows (when role in teachers table not match the role in json from results column in votes
    # table)
    if teachers[current_teacher][1] == 'practice':
        cursor.execute(
            f"DELETE FROM {faculty}.votes WHERE teacher_id = {teachers[current_teacher][0]} AND results ?& array['lecture']")
    elif teachers[current_teacher][1] == 'lecture':
        cursor.execute(
            f"DELETE FROM {faculty}.votes WHERE teacher_id = {teachers[current_teacher][0]} AND results ?& array['practice']")
    con.commit()

    # Running Rscript to get diagrams
    # subprocess.run(['Rscript', pass_to_Rfile, current_teacher, faculty, role])

    questions: dict = {'1': 'Дотримання РСО',
                       '2': 'Зручність\nкомунікації',
                       '3': 'Комфортність\nспілкування',
                       '4': 'Пунктуальність',
                       '5': 'Актуальність\nматеріалу',
                       '6': 'Достатність\nнавчальних\nматеріалів',
                       '7': 'Відповідність\nлекцій\nпрактикам',
                       '8': 'Наскільки зручним\nі ефективним є формат\nдистанційного навчання',
                       '9': 'Адаптивність викладача\nдо надзвичайних ситуацій',
                       '10': 'опитуваних хочуть,\nщоб викладач\nпродовжив викладати',
                       '11': 'вважають, що викладач\nдотримується академічної\nдоброчесності',
                       '12': 'мали можливість вибору\nальтернативного способу\nотримання знань і балів', }
    if role == 'both':
        cursor.execute(
            f"SELECT results FROM {faculty}.votes WHERE"
            f" teacher_id = {teachers[current_teacher][0]} AND results?& array['lecture', 'practice']"
        )
    elif role == 'lecture':
        cursor.execute(
            f"SELECT results FROM {faculty}.votes WHERE"
            f" teacher_id = {teachers[current_teacher][0]} AND results?& array['lecture']"
        )
    elif role == 'practice':
        cursor.execute(
            f"SELECT results FROM {faculty}.votes WHERE"
            f" teacher_id = {teachers[current_teacher][0]} AND results?& array['practice']"
        )



    rows = cursor.fetchall()
    votes = []
    for row in rows:
        votes.append(row)

    print(votes)

    marks: list[list[int]] = []
    if role != 'lecture':
        for i in range(len(votes)):
            temp = [votes[i][0]['practice']['marks'][-j] for j in range(3, 0, -1)]
            marks.append(temp)

        save_prepod = round(sum(marks[i][0] for i in range(len(marks))) / len(marks) * 100)
        akadem_kind = round(sum(marks[i][1] for i in range(len(marks))) / len(marks) * 100)
        alternative_way = round(sum(marks[i][2] for i in range(len(marks))) / len(marks) * 100)
    else:
        for i in range(len(votes)):
            temp = [votes[i][0]['lecture']['marks'][-j] for j in range(2, 0, -1)]
            marks.append(temp)
        save_prepod = round(sum(marks[i][0] for i in range(len(marks))) / len(marks) * 100)
        akadem_kind = round(sum(marks[i][1] for i in range(len(marks))) / len(marks) * 100)
        alternative_way = None

    n_students = amount_of_students(cursor)

    if role == 'both':
        set_image(save_prepod, akadem_kind, alternative_way, current_teacher, questions, faculty, len(votes), 'both',
                  n_students)
    elif role == 'lecture':
        set_image(save_prepod, akadem_kind, alternative_way, current_teacher, questions, faculty, len(votes), 'lecture',
                  n_students)
    elif role == 'practice':
        set_image(save_prepod, akadem_kind, alternative_way, current_teacher, questions, faculty, len(votes),
                  'practice', n_students)


def set_role() -> None:
    """This function will check teacher's role and choose which picture to create"""
    con = psycopg2.connect(
        database=database_name,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM {faculty}.teachers")
    rows = cursor.fetchall()

    teachers: dict = {}
    for row in rows:
        teachers.update({row[1]: [row[0], row[2]]})

    if teachers[current_teacher][1] == 'practice':
        role = 'practice'
        getting_data(con, cursor, teachers, role)
    elif teachers[current_teacher][1] == 'lecture':
        role = 'lecture'
        getting_data(con, cursor, teachers, role)
    elif teachers[current_teacher][1] == 'both':

        getting_data(con, cursor, teachers, 'practice')
        # getting_data(con, cursor, teachers, 'lecture')
        # getting_data(con, cursor, teachers, 'both')

    con.close()


set_role()

library('DBI')
# install.packages('RPostgreSQL')
library('RPostgreSQL')
# install.packages('rjson')
library('rjson')
# install.packages('glue')
library('glue')
# install.packages('fmsb')
library('fmsb')
# install.packages('ggplot2')
library('ggplot2')



radar <- function(data){
  jpeg("/Users/bellzebull/Documents/КПИ/OSA/OSA_graphic/spyder.jpeg")
  radar_chart <- radarchart(data,
                            vlcex= 0.0001,
                            axistype = 6,
                            pcol = rgb(0.74, 0.72, 0.98, 0.8),
                            pty = 32,
                            plty = 1,
                            plwd = 1,
                            pfcol = rgb(0.74, 0.72, 0.98, 0.7),
                            cglty = 1,
                            cglwd = 0.2,
                            axislabcol = rgb(0.375, 0.375, 0.375, 0.7),
                            seg = 5,
                            caxislabels = c(0, 1, 2, 3, 4, 5),
                            calcex = 0.5)
  dev.off()
}

ghist <- function(ghist_data){
  
  
  comf <- ggplot(data = ghist_data, aes(x = n8)) + 
    geom_histogram(binwidth = 0.5,
                   bins = 5,
                   fill = rgb(0.74, 0.72, 0.98, 0.7)) +
    theme_bw()+
    theme(panel.grid.major = element_blank(),
          panel.border = element_blank(),
          axis.line = element_line(colour = rgb(0.375, 0.375, 0.375, 0.7),
                                   linewidth = 0.3),
          axis.title = element_blank(),
          text = element_text(size = 30))+
    expand_limits(x = c(1,2,3,4,5)) 
  ggsave("comfortable.jpg", 
         plot = comf, 
         path = '/Users/bellzebull/Documents/КПИ/OSA/OSA_graphic')
  
  
  
  adaptive <- ggplot(data = ghist_data, aes(x = n9)) + 
    geom_histogram(binwidth = 0.5,
                   bins = 5,
                   fill = rgb(0.74, 0.72, 0.98, 0.7)) +
    theme_bw()+
    theme(panel.grid.major = element_blank(),
          panel.border = element_blank(),
          axis.line = element_line(colour = rgb(0.375, 0.375, 0.375, 0.7),
                                   linewidth = 0.3),
          axis.title = element_blank(),
          text = element_text(size = 30)) +
    expand_limits(x = c(1,2,3,4,5))
  
  ggsave("adaptiv.jpg", 
         plot = adaptive,
         path = '/Users/bellzebull/Documents/КПИ/OSA/OSA_graphic')
}

diagrams_data <- function(questions, questions_id, marks_frame, vec_len, role){
  
  if (role == 'both'){
    n1 = vector(mode = 'numeric')
    n2 = as.vector(n1)
    n3 = as.vector(n1)
    n4 = as.vector(n1)
    n5 = as.vector(n1)
    n6 = as.vector(n1)
    n7 = as.vector(n1)
    n8 = as.vector(n1)
    n9 = as.vector(n1)
    n10 = as.vector(n1)
    n11 = as.vector(n1)
    n12 = as.vector(n1)
    
    i <-  1
    while (i <= nrow(marks_frame)){
      if (marks_frame$lecture.questions_ids[i] == 2){
        n2 <- append(n2, marks_frame$lecture.marks[i])
        i = i + 1
      }else if (marks_frame$lecture.questions_ids[i] == 3){
        n3 <- append(n3, marks_frame$lecture.marks[i])
        i = i + 1
      }else if (marks_frame$lecture.questions_ids[i] == 4){
        n4 <- append(n4, marks_frame$lecture.marks[i])
        i = i + 1
      }else if (marks_frame$lecture.questions_ids[i] == 5){
        n5 <- append(n5, marks_frame$lecture.marks[i])
        i = i + 1
      }else if (marks_frame$lecture.questions_ids[i] == 7){
        n7 <- append(n7, marks_frame$lecture.marks[i])
        i = i + 1
      }else if (marks_frame$lecture.questions_ids[i] == 8){
        n8 <- append(n8, marks_frame$lecture.marks[i])
        i = i + 1
      }else if (marks_frame$lecture.questions_ids[i] == 9){
        n9 <- append(n9, marks_frame$lecture.marks[i])
        i = i + 1
      }else if (marks_frame$lecture.questions_ids[i] == 1 ||
                marks_frame$lecture.questions_ids[i] == 6 ||
                marks_frame$lecture.questions_ids[i] == 10 ||
                marks_frame$lecture.questions_ids[i] == 11 ||
                marks_frame$lecture.questions_ids[i] == 12 ||
                marks_frame$lecture.questions_ids[i] == 20)
        i = i + 1
    }
    
    i <-  1
    while (i <= nrow(marks_frame)){
      if (marks_frame$practice.questions_ids[i] == 1){
        n1 <- append(n1, marks_frame$practice.marks[i])
        i = i + 1
      }else if (marks_frame$practice.questions_ids[i] == 6){
        n6 <- append(n6, marks_frame$practice.marks[i])
        i = i + 1
      }else if (marks_frame$practice.questions_ids[i] == 2 ||
                marks_frame$practice.questions_ids[i] == 3 || 
                marks_frame$practice.questions_ids[i] == 4 || 
                marks_frame$practice.questions_ids[i] == 5 ||
                marks_frame$practice.questions_ids[i] == 7 ||
                marks_frame$practice.questions_ids[i] == 8 || 
                marks_frame$practice.questions_ids[i] == 9 ||
                marks_frame$practice.questions_ids[i] == 10 ||
                marks_frame$practice.questions_ids[i] == 11 ||
                marks_frame$practice.questions_ids[i] == 12){
        i = i + 1
      }
    }
    
    ghist_data <- data.frame('n8' = n8,
                             'n9' = n9)
    data <- data.frame('Дотримання РСО' = c(5, 0, mean(n1)),
                       'Зручність комунікації' = c(5, 0, mean(n2)),
                       "Комфортність спілкування" = c(5, 0, mean(n3)),
                       'Пунктуальність' = c(5, 0, mean(n4)),
                       'Актуальність матеріалу' = c(5, 0, mean(n5)),
                       'Достатність навчальних матеріалів' = c(5, 0, mean(n6)),
                       'Відповідність лекцій практикам' = c(5, 0, mean(n7)))
    
  }else if (role == 'lecture'){
    
    n2 = vector(mode = 'numeric')
    n3 = as.vector(n2)
    n4 = as.vector(n2)
    n5 = as.vector(n2)
    n7 = as.vector(n2)
    n8 = as.vector(n2)
    n9 = as.vector(n2)
    n10 = as.vector(n2)
    n11 = as.vector(n2)
    
    i <-  1
    while (i <= nrow(marks_frame)){
      if (marks_frame$questions_ids[i] == 2){
        n2 <- append(n2, marks_frame$marks[i])
        i = i + 1
      }else if (marks_frame$questions_ids[i] == 3){
        n3 <- append(n3, marks_frame$marks[i])
        i = i + 1
      }else if (marks_frame$questions_ids[i] == 4){
        n4 <- append(n4, marks_frame$marks[i])
        i = i + 1
      }else if (marks_frame$questions_ids[i] == 5){
        n5 <- append(n5, marks_frame$marks[i])
        i = i + 1
      }else if (marks_frame$questions_ids[i] == 7){
        n7 <- append(n7, marks_frame$marks[i])
        i = i + 1
      }else if (marks_frame$questions_ids[i] == 8){
        n8 <- append(n8, marks_frame$marks[i])
        i = i + 1
      }else if (marks_frame$questions_ids[i] == 9){
        n9 <- append(n9, marks_frame$marks[i])
        i = i + 1
      }else if (marks_frame$questions_ids[i] == 1 ||
                marks_frame$questions_ids[i] == 10 ||
                marks_frame$questions_ids[i] == 11 ||
                marks_frame$questions_ids[i] == 12 ||
                marks_frame$questions_ids[i] == 20)
        i = i + 1
    }
    
    ghist_data <- data.frame('n8' = n8,
                             'n9' = n9)
    data <- data.frame('Зручність комунікації' = c(5, 0, mean(n2)),
                       "Комфортність спілкування" = c(5, 0, mean(n3)),
                       'Пунктуальність' = c(5, 0, mean(n4)),
                       'Актуальність матеріалу' = c(5, 0, mean(n5)),
                       'Відповідність лекцій практикам' = c(5, 0, mean(n7)))
  }else if (role == 'practice'){
    n1 = vector(mode = 'numeric')
    n2 = as.vector(n1)
    n3 = as.vector(n1)
    n4 = as.vector(n1)
    n6 = as.vector(n1)
    n8 = as.vector(n1)
    n9 = as.vector(n1)
    n10 = as.vector(n1)
    n11 = as.vector(n1)
    n12 = as.vector(n1)
    i <-  1
    while (i <= nrow(marks_frame)){
      if (marks_frame$questions_ids[i] == 2){
        n2 <- append(n2, marks_frame$marks[i])
        i = i + 1
      }else if (marks_frame$questions_ids[i] == 1){
        n1 <- append(n1, marks_frame$marks[i])
        i = i + 1
      }else if (marks_frame$questions_ids[i] == 3){
        n3 <- append(n3, marks_frame$marks[i])
        i = i + 1
      }else if (marks_frame$questions_ids[i] == 4){
        n4 <- append(n4, marks_frame$marks[i])
        i = i + 1
      }else if (marks_frame$questions_ids[i] == 6){
        n6 <- append(n6, marks_frame$marks[i])
        i = i + 1
      }else if (marks_frame$questions_ids[i] == 8){
        n8 <- append(n8, marks_frame$marks[i])
        i = i + 1
      }else if (marks_frame$questions_ids[i] == 9){
        n9 <- append(n9, marks_frame$marks[i])
        i = i + 1
      }else if (marks_frame$questions_ids[i] == 10 ||
                marks_frame$questions_ids[i] == 11 ||
                marks_frame$questions_ids[i] == 12)
        i = i + 1
      
    }
    
    ghist_data <- data.frame('n8' = n8,
                             'n9' = n9)
    data <- data.frame('Дотримання РСО' = c(5, 0, mean(n1)),
                       'Зручність комунікації' = c(5, 0, mean(n2)),
                       "Комфортність спілкування" = c(5, 0, mean(n3)),
                       'Пунктуальність' = c(5, 0, mean(n4)),
                       'Достатність навчальних матеріалів' = c(5, 0, mean(n6)))
  }
  
  
  radar(data)
  ghist(ghist_data)
}


create_dataset <- function(teacher_id, faculty, connec, role){
  # role <- dbGetQuery(connec, glue("SELECT type from {faculty}.teachers
  #                        WHERE id = {teacher_id}"))
  # 
  if (role == "both"){
    questions_id <- dbGetQuery(connec,
                               "SELECT id FROM public.questions where type != 'open'")
  } else if (role == "lecture") {
    questions_id <- dbGetQuery(connec,
                               "SELECT id FROM public.questions where type = 'lecture' or
                                type = 'both'")
  } else if (role == "practice"){
    questions_id <- dbGetQuery(connec,
                               "SELECT id FROM public.questions where type = 'practice' or
                              type = 'both'")
  }
  votes_id_list <- dbGetQuery(connec,
                              glue("SELECT id FROM {faculty}.votes
                               where teacher_id = {teacher_id}"))
  vec_len <- nrow(votes_id_list)
  
  all_marks_json <- vector(mode = "list", length = vec_len)
  if (role == 'practice'){
    all_marks_json <- dbGetQuery(connec,
                                 glue("SELECT results FROM {faculty}.votes
                               where teacher_id = {teacher_id} AND results ?& array['practice']"))
    vote <- fromJSON(all_marks_json[1,])
    # vote$lecture$marks <- append(vote$lecture$marks, 20)
    # vote$lecture$questions_ids <- append(vote$lecture$questions_ids, 20)
    marks_frame <- as.data.frame(vote$practice)

    names(marks_frame) <- c("marks", 'questions_ids')
    
    i <- 2
    while (i <= nrow(all_marks_json)) {
      temp <- fromJSON(all_marks_json[i,])
      temp <- temp$practice
      
      temp_frame <- as.data.frame(temp)
      marks_frame <- rbind(marks_frame, temp_frame)
      i = i + 1
    }
    
  }else if (role == 'lecture'){
    all_marks_json <- dbGetQuery(connec,
                                 glue("SELECT results FROM {faculty}.votes
                               where teacher_id = {teacher_id} AND results ?& array['lecture']"))
    vote <- fromJSON(all_marks_json[1,])
    marks_frame <- as.data.frame(vote$lecture)
 
    names(marks_frame) <- c("marks", 'questions_ids')

    i <- 2
    while (i <= nrow(all_marks_json)) {
      temp <- fromJSON(all_marks_json[i,])
      temp <- temp$lecture

      temp_frame <- as.data.frame(temp)
      marks_frame <- rbind(marks_frame, temp_frame)
      i = i + 1
    }
    
    
  }else if (role == 'both'){
    all_marks_json <- dbGetQuery(connec,
                                 glue("SELECT results FROM {faculty}.votes
                               where teacher_id = {teacher_id} AND results ?& array['lecture', 'practice']"))
    
    
    vote <- fromJSON(all_marks_json[1,])
    vote$lecture$marks <- append(vote$lecture$marks, 20)
    vote$lecture$questions_ids <- append(vote$lecture$questions_ids, 20)
    marks_frame <- as.data.frame(vote)

    i <- 2
    while (i <= nrow(all_marks_json)) {
      temp <- fromJSON(all_marks_json[i,])
      temp$lecture$marks <- append(temp$lecture$marks, 20)
      temp$lecture$questions_ids <- append(temp$lecture$questions_ids, 20)
      temp_frame <- as.data.frame(temp)
      marks_frame <- rbind(marks_frame, temp_frame)
      i = i + 1
    }
  }
    
  
  
  diagrams_data(questions, questions_id, marks_frame, vec_len, role)
  
}


check_option <- function(connec){
  # args = commandArgs(trailingOnly=TRUE)
  # teacher <- args[1]
  # faculty <- args[2]
  # role <- args[3]
  teacher = "Бакун Володимир Володимирович"
  faculty = "fbme"
  role = 'lecture'
  teacher_id <- dbGetQuery(connec,
                           glue("SELECT id from {faculty}.teachers
                         WHERE full_name like '%{teacher}%'"))
  
  create_dataset(teacher_id, faculty, connec, role)
}


connection_check <- function(){
  mode <- 0
  dsn_database = "coba_test"
  dsn_hostname = "MacBook-Air-bellzebull.local"
  dsn_port = "5432"
  dsn_uid = "postgres"
  dsn_pwd = "Zozerman1"
  tryCatch({
    drv <- dbDriver("PostgreSQL")
    print("Connecting to Database…")
    connec <- dbConnect(drv,
                        dbname = dsn_database,
                        host = dsn_hostname,
                        port = dsn_port,
                        user = dsn_uid,
                        password = dsn_pwd)
    print("Database Connected!")
  },
  error=function(cond) {
    mode <- 1
    print("Unable to connect to Database.")
  })
  if (mode == 0){
    check_option(connec)
    
  } 
}


connection_check()














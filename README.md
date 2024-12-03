# OTUS_lessons_10-20_Selenium

[![Header](https://github.com/GoodyrevQA/OTUS_auto_web_QA_2024/blob/main/assets/OTUS.jpg)](https://github.com/GoodyrevQA/OTUS_auto_web_QA_2024)

### Languages and Tools used:
[![Python](https://img.shields.io/badge/-Python-24292f??style=for-the-badge&logo=Python&logoColor=47c5fb)](https://github.com/GoodyrevQA/python_tg_bot)
[![pytest](https://img.shields.io/badge/-pytest-24292f??style=for-the-badge&logo=pytest&logoColor=0099d9)](https://github.com/GoodyrevQA/python_autotests)
[![Git](https://img.shields.io/badge/-Git-24292f??style=for-the-badge&logo=Git&logoColor=f43010)](https://github.com/GoodyrevQA)
[![Docker](https://img.shields.io/badge/-Docker-24292f??style=for-the-badge&logo=Docker&logoColor=47c5fb)](https://github.com/GoodyrevQA/OTUS_lessons_10-20_Selenium)



### Настройка Jenkins:
Инструкция:
https://docs.google.com/document/d/1VsRfM31dv6cdzzRRVdK5Fiu_HEq0mcBmo2lu_PGVw3Y/edit?tab=t.0#heading=h.icoyi4idm65z

На основе доккерфайла Jenkins с Docker https://github.com/GoodyrevQA/OTUS_lessons_10-20_Selenium/tree/with_docker_compose/docker-file-for-jenkins
создать образ:
```
docker build -t jenkins-with-docker .
```

на основе образа создать контейнер (333 - имя дашборда в Jenkins):
```
docker run -d --name jenkins-docker -p 50000:50000 -p 8080:8080 \
-v /var/run/docker.sock:/var/run/docker.sock -v jenkins_home:/var/jenkins_home \
-v jenkins-shared-data:/var/jenkins_home/workspace/333/allure-results jenkins-with-docker
```
- параметр -v /var/run/docker.sock:/var/run/docker.sock монтирует доккер соккет хоста в контейнер
- -v jenkins_home:/var/jenkins_home сохраняет данные Jenkins между перезапусками контейнера
- -v jenkins-shared-data:/var/jenkins_home/workspace/333/allure-results создает общий том, к которому потом подключится и поднятый контейнер с тестами

Чтобы у пользователя Jenkins были права на соккет хоста и на запись в общий том,
нужно зайти в контейнер Jenkins с правами администратора:
```
docker exec -it --user root jenkins-docker /bin/sh
```
и выполнить команды:
```
chmod 666 /var/run/dpcker.sock
chown -R jenkins:jenkins /var/jenkins_home/workspace/333/allure-results
chmod -R 755 /var/jenkins_home/workspace/333/allure-results
```

### Внутри контейнера Jenkins (в web интерфейсе Jenkins)
Настраиваем параметры сборки.
Создаем образ с тестами (Dockerfile находится в корне, в Jenkins он скачается с репозитория):
```
docker build -t pytest333 .
```
создаем и запускаем контейнер с тестами с указанием общего тома:
```
docker run -i --rm -v jenkins-shared-data:/app/allure-results pytest333 pytest --browser=${browser} \
--external-password ${password} -n ${number_of_threads} --alluredir=allure-results ./tests
```
# Stepic_web_project from [this](https://stepik.org/course/154/info) course
My Stepik web project, _started at 05.23.21_
# Gunicorn start up
in /home/box/web/ask: ```gunicorn -c ../etc/gunicorn.conf --access-logfile acc.log --error-logfile err.log ask.wsgi:application```


don't forget: in /etc/mysql/my.cnf
add: 
```[client]  
database = stepic_web

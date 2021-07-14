# Stepic_web_project from [this](https://stepik.org/course/154/info) course
My Stepik web project, _started at 23.05.21_
# Gunicorn start up
in /home/box/web/ask: ```gunicorn -c ../etc/gunicorn.conf --access-logfile acc.log --error-logfile err.log ask.wsgi:application```


don't forget to add in /etc/mysql/my.cnf 
```
[client]  
database = stepic_web


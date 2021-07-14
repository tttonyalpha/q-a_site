# Stepic_web_project from [this](https://stepik.org/course/154/info) course
My Stepik web project, _started at 23.05.21_
# Gunicorn start up
in /home/box/web/ask: ```gunicorn -c ../etc/gunicorn.conf --access-logfile acc.log --error-logfile err.log ask.wsgi:application```


don't forget to add in /etc/mysql/my.cnf 
```
[client]  
database = stepic_web
```
# running database
git clone https://github.com/tttonyalpha/stepic_web_project 

sudo apt update  

sudo apt install python3.5 -y  
sudo apt install python3.5-dev -y  
sudo unlink /usr/bin/python3  
sudo ln -s /usr/bin/python3.5 /usr/bin/python3  
sudo python3 -m pip install gunicorn  
sudo python3 -m pip install django==2.0  
sudo python3 -m pip install mysqlclient  

    
sudo /etc/init.d/mysql start  
mysql -uroot -e "CREATE DATABASE stepic_web;"  
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"  


python3 manage.py makemigrations qa  
python3 manage.py migrate  


# splitwise

Steps to set up  

sudo apt-get update  
sudo apt-get install python-django  

django-admin startproject projectname  
cd projectname  

*** Strongly Recommend Pycharm platform ****

create database splitwise, change the username and password in the splitwise/setting

python makemigrations  
python manage.py migrate  
python manage.py createsuperuser      #<username> pathak #<password> !@#$%^&*  
#future help   
python manage.py changepassword <user_name>  
python manage.py runserver 0.0.0.0:8000  

http://0.0.0.0:8000/admin/


python manage.py shell   
--> from MoneyTransact.models import Balance  
--> a = Balance(taker ='name'...)  
--> a.save
--> Balance.objects.all()  
--> Balance.objects.filter(taker='name')  


setting.py change MYsql settings  
form users : tut 34




work to do 
1) sign up / sign in frontend 
2) your balance sheet  -> frontend (view)
3) advanced form interactive 
4) Splitwise python code 
5) Database obtimization indexing : Alternate 1 
									Alterante 2    Hashing 
									Alternate 3	   B+ Tree 	

									Time analysis 
									
## Project Name

- Award.
## Author 

- Lucky Ogumbo Oula

## Project Description

- Basically the app allow users to view project and rate them

## Technologies Used

- PYTHON
- DJANGO
- POSTMAN API TESTING
- POSTGRES DATABASE
- BOOTSTRAP AND CSS
- HTLM5




​
### Installing
​
A step by step series of examples that tell you how to get a development env running
​
1. set up a virtual environment using the following command
​
```
virtualenv env
```
​
And activate it
​
```
source env/bin/activate
```
1. install the latest version of pip
​
```
curl https://bootstrap.pypa.io/get-pip.py | python
```
​
1. Install the requirements in the requirements.txt file using
```
pip install -r requirements.txt
```
1. create a .env file in your rootfolder and add the following configurations
```
SECRET_KEY='<random-string>'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='postgres://databaseowner:password@localhost/databasename'
```
1. create postgres database
```
CREATE DATABASE <your-database-name>
```
1. create a migration using the following command
```
python3.6 manage.py makemigrations
```
​
and migrate
```
python3.6 manage.py migrate
```
1. create a admin account
```
python 3.6 manage.py createsuperuser
```
and add your credentials
​
1. run the application using 
```
python3.6 manage.py runserver
```
1. navigate to the admin panel by typing 
```
localhost:8000/admin
```
​
​
End with an example of getting some data out of the system or using it for a little demo

## Project live-link

- https://award254.herokuapp.com/




## Support and contact details
> The application is an open-source product if you  want to improve it or in an event of a bug  contact this
> Email:(luckyoula@gmail.com) .
### License
>You can check out the license [click here](https://choosealicense.com/licenses/mit/)
This project is licensed under the terms of **MIT**

- 
  Copyright (c)  2020

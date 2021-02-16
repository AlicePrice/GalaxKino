# GalaxKino
Django cinema web application


Dependencies:
```
  python3

  django3.3
```

Init repo:
```
  Install virtualenv: https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3#:~:text=Virtualenv%20is%20a%20tool%20used,the%20globally%20installed%20libraries%20either).

  Create envirolment: python3 -m venv ./env

  Activate Linux: source ./env/bin/activate

  Activate Windows: .\env\[bin|scripts]\activate.bat

  Install depends: pip3 install django

  Clone repo: git clone https://github.com/AlicePrice/GalaxKino.git

  Proceed migrations: cd GalaxKino && python3 manage.py migrate && python3 manage.py makemigrations && python3 manage.py migrate

  Create superuser: python3 manage.py createsuperuser
```

Start web service
```
  On loopback: python3 manage.py runserver

  Page: http://127.0.0.1:8000

  AdminPage: http://127.0.0.1:8000/admin

  On any local ip: python3 manage.py runserver <ip>:<port>
```
  

Django is a backend server side web framework.
Django is a free open source and written in python.
Django is easier to make web pages using python.
Django is easier to create web sites using python.
How Does Django works:
Django follows the MVT(Model view Template) design pattern.
Model: The Data you want present ,usually data from Databases.
View: the request handle the return Specific template-Based on the request from the user request.
Template: like text file(html) built a page ,how the logics build on file.
How to create project:
-->create a folder: mkdir myproject
-->change directory: cd myproject
-->installing virtualenv: pip install virtualenv
-->create virtual environment folder: python -m venv myvenv
-->activate virtual environment: ./myvenv/scripts/activate
-->deactive the virtual environment: deactivate
-->if we want active virtual environment: ./myvenv/scripts/activate
-->in search icon we type "powershell" as adminstrator>yes>In cmd System32:Set-ExecutionPolicy RemoteSigned
-->list of softwares :pip list
-->installing the django: pip install django
-->startproject: django-admin startproject myproject .
-->run server: python manage.py runserver
-->create a app: python manage.py startapp core
-->install migrates: python manage.py migrate

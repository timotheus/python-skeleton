# python-skeleton

_This skeleton for Django and python CLI projects. It provides a directory structure for projects during development and deployment._

## How to create an project using this skeleton

_Make sure you have Django >= 1.9 installed._

```bash
> django-admin startproject myproject --template=https://github.corp.ebay.com/NetDev/python-skeleton/archive/master.zip --extension=py,ini,in
```

## Running the project

_Once you've successfully started the Django project using the skeleton template, you'll need create the virtualenv and install a few Python dependancies._

```bash
> cd myproject
> virtualenv venv36 -p <path to python36>
> source venv36/bin/activate
> pip install -r requirements.txt
> python manage.py runserver
```

## Authors

- Tim Keefer <tkeefer@ebay.com>

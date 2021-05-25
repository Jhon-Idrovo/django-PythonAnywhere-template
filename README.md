Create a virtual enviroment named venv
py -m venv venv

Activate the virtual enviroment
cd venv/Scripts/activate

Install requirements
cd ../../
pip install -r requirements.txt

Create a django app
manage.py startapp appname .

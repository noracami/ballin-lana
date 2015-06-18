# ballin-lana

---

``` bash
# Mac$
python3 -m venv venv
```

``` bash
# ubuntu$
pyvenv-3.4 --without-pip venv
source ./venv/bin/activate
wget https://pypi.python.org/packages/source/s/setuptools/setuptools-3.4.4.tar.gz
tar -vzxf setuptools-3.4.4.tar.gz
cd setuptools-3.4.4
python setup.py install
cd ..
wget https://pypi.python.org/packages/source/p/pip/pip-1.5.6.tar.gz
tar -vzxf pip-1.5.6.tar.gz
cd pip-1.5.6
python setup.py install
cd ..
deactivate
source ./venv/bin/activate
```

---

``
pip install -U pip
export DJANGO_SETTINGS_MODULE=djangoconnectiondashboard.settings.local
```

---

``` bash
# Run this from your terminal:
# Please ensure that you have Ruby installed.
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
```

---

```
python manage.py runserver 0.0.0.0:8008
```

---

```
django-admin startproject djangoconnectiondashboard
python manage.py startapp teams
```

It is easy to use Python with forever.js:

``` bash
forever start -c python python_script.py
```

To use it with virtualenv is a little bit more complicated, I did it using a bash script (call it python_virtualenv):

``` bash
#!/bin/bash
# Script to run a Python file using the local virtualenv
source bin/activate
bin/python $@
```

Now use that script with forever:

``` bash
forever start -c ./python_virtualenv python_script.py
```

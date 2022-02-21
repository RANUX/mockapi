## How to create new project in hesti cp

1. Create new domain
2. Create new site
3. In advanced option enable ssl 
    Web Template: Django_app
    Backend template: no_php
    Proxy template: Django_proxy_pass
4. Login to ssh

Edit djangoapp/settings.py

```
cd /home/sites/web/mockapi.htmldoc.ru
. venv/bin/activate
pip install -Ur requirements.txt
cd djangoapp/
./manage.py migrate
./manage.py collectstatic
./manage.py createsuperuser

systemctl daemon-reload
systemctl restart mockapi.htmldoc.ru-gunicorn.service

# To read sqlite.db change owner of djangoapp
chown sites djangoapp/

```
#!/bin/sh

for i in $(cd ../django/conf/locale/; ls -d ??)
do
    PYTHONPATH=.. ../django/bin/django-admin.py makemessages -l $i
    ./cldr_territories_to_po.py $i > locale/$i/LC_MESSAGES/django.po
done

PYTHONPATH=.. ../django/bin/django-admin.py compilemessages

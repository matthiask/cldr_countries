#!/bin/sh

for i in $(cd ../django/django/conf/locale/; ls -d *)
do
    django-admin makemessages -l $i
    mkdir -p locale/$i/LC_MESSAGES
    ./cldr_territories_to_po.py $i > locale/$i/LC_MESSAGES/django.po
done

django-admin compilemessages

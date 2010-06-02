#!/bin/sh

curl -O http://unicode.org/Public/cldr/1.8.1/core.zip
unzip core.zip
./cldr_territories_en_to_py.py > data.py
mkdir locale

echo "Now generate the translations you need or execute for_django.sh"

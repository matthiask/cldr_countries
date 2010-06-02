#!/usr/bin/python
#
# Usage: ./cldr_territories_en_to_py.py de de_CH > countries.py

from xml.etree import ElementTree


xml = ElementTree.fromstring(open('common/main/en.xml').read())

print '''# coding=utf-8

from django.utils.translation import ugettext_lazy as _


countries = {'''

for t in xml.findall('localeDisplayNames/territories/territory'):
    print ('    \'%s\': _(\'%s\'),' % (t.attrib['type'], t.text)).encode('utf-8')

print '}'

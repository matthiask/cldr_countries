#!/usr/bin/python
#
# Usage: ./cldr_territories_to_po.py de de_CH > django.po

import sys
from xml.etree import ElementTree


orig = ElementTree.fromstring(open('common/main/en.xml').read())
translated = [ElementTree.fromstring(open('common/main/%s.xml' % t).read()) for t in sys.argv[1:]]

print '''# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: PACKAGE VERSION\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: 2010-05-31 18:34+0200\\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"
"Language-Team: LANGUAGE <LL@li.org>\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Language: \\n"
"Plural-Forms: nplurals=2; plural=(n != 1)\\n"
'''

orig_elems = orig.findall('localeDisplayNames/territories/territory')
translated_elems = [xml.findall('localeDisplayNames/territories/territory') for xml in translated]

orig_dict = dict((t.attrib['type'], t.text) for t in orig_elems)
translated_dict = {}
for elems in translated_elems:
    translated_dict.update(dict((t.attrib['type'], t.text) for t in elems))

for key, orig in orig_dict.iteritems():
    print ('''msgid "%s"\nmsgstr "%s"\n''' % (orig, translated_dict.get(key, u''))).encode('utf-8')

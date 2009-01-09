#! /usr/bin/python

import sys, random
import gen_data

try:
    count = int (sys.argv[1])
except:
    count = 1

vcard = """BEGIN:VCARD
VERSION:3.0
FN:%s
N:%s;%s;;;
ORG:%s
BDAY:%s
EMAIL;TYPE=WORK:%s
X-JABBER;TYPE=HOME:%s
ADR;TYPE=HOME:;;%s;%s;%s;%s;USA
END:VCARD"""

for i in range (0, count):
    name = gen_data.create_name()
    adr = gen_data.create_city_state_zip()
    company = gen_data.create_company_name()

    print >>open(str(i), "w"), vcard % (' '.join(name),
                   name[1], name[0],
                   company,
                   gen_data.create_birthday(),
                   gen_data.create_email(name=name),
                   gen_data.create_email(name=name),
                   gen_data.create_street(),
                   adr[1], adr[2], adr[0],
                   )

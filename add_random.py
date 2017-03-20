#/usr/bin/env python
from uuid import uuid4

f = open("mails.txt", "r")
mails = f.readlines()
f.close()

for line in mails:
    mails[mails.index(line)] = line.replace("\n", "")
    mails[mails.index(line.replace("\n", ""))] += "|" + str(uuid4())

f = open("mails.txt", "w")
f.write("\n".join(mails))
f.close()

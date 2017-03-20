#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) Ignacio Rodríguez <ignacio@sugarlabs.org>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import json
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def verify():
    mail_addresses = []

    # name|email|verificationhash
    f = open("mails.txt", "r")
    mails_data = f.readlines()
    f.close()

    for line in mails_data:
        try:
            mail_addresses.append(line.split("|"))
        except:
            # bad format line
            pass

    # name|email
    f = open("mails_verified.txt", "r")
    mails_verified = f.read()
    f.close()

    verificationhash = request.args.get('verify')
    verified = False
    name = None

    if verificationhash:
        for user_data in mail_addresses:
            name, email, vhash = user_data
            vhash = vhash.replace("\n", "")  # Replace newline
            txt_data = "%s|%s" % (name, email)

            if vhash == verificationhash:
                if (txt_data not in mails_verified):
                    mails_verified += "%s\n" % (txt_data)

                    f = open("mails_verified.txt", "w")
                    f.write(mails_verified)
                    f.close()
                verified = True
                break

    return render_template(
        "index.html",
        verified=verified,
        name=name)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)

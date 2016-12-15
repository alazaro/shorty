SHORTY
=====

This is a link shortener created for an interview. I decided to publish it in order to show some of my code to other interested companies.

The user part doesn't have much practical sense, but it was one of the requirements, so I will leave it there for now.


INSTALLATION
------------

- Create a Python3 virtualenv `virtualenv -p python3 venv`
- Activate the virtualenv `. venv/bin/activate`
- Install the requirements `pip install -r requirements.txt`
- Create the database `./manage.py migrate`
- Create the users `./manage.py create_fake_users <user_count>`
- Start the server `./manage.py runserver`


Tests
-----

Run `./manage.py test`


License
-------

The MIT License (MIT)
Copyright (c) 2016 Álvaro Lázaro Gallego

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

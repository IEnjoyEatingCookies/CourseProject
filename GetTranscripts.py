'''
This file uses a library called "coursera-dl" which goes through
Coursera and for every lesson, extracts key information such as videos, readings,
attachments to lessons, and html files.
'''
import os

#Enter your credentials
email = ""
password = ""
course_name = "cs-410"
cauth = "Your_CAUTH"
language = "en"
os.system("coursera-dl -u %s -p %s course_name %s -ca %s -sl %s" % (email, password, course_name, cauth, language))

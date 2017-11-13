import csv
import requests
import json
from bs4 import BeautifulSoup, SoupStrainer
import operator
import sys
import re
from urllib.request import urlopen
import lxml

''' find emails and phone numbers
def findcontactdetails(urlsypops):
    f = urlopen(urlsypops)
    s = BeautifulSoup(f, 'html.parser')
    s = s.get_text()

    contactdeets = []

    #regex for phone numbers in US - may need to change for UK
    phone = re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})",s)

    #regex for emails shiuld work for everywhere
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}",s)

    if len(phone) == 0:
        contactdeets.append("n/a")
    else :
        contactdeets.append(phone[0])
    if len(emails) != 0:
        contactdeets.append(emails[0])
    else:
        contactdeets.append(" ")
    return contactdeets

'''

urlingtons = []

data = "http://www.brandcalibre.com" #\"video+marketing\"+UK+tel:"
querypage = urlopen(data)
soupy = BeautifulSoup(querypage, 'lxml')

for link in soupy
    if link.has_attr('href'):
        urlingtons.append(link['href'])

print(urlingtons)

# make list of urls from a google query

list_of_urls = []

class targetcompany:
    company = "name"
    name = "individual"
    email = "contact@company.com"
    phone = "01412126356"


    # The class "constructor" - It's actually an initializer
    def __init__(self, company, name, email, phone):
        self.company = company
        self.name = name
        self.email = email
        self.phone = phone

targetcompanies = []

#print(findcontactdetails("http://www.deggen.com"))


# call function on each item in that list of urls




'''
for i in range(0, len(jobject['Rows'])):
    targetcompanies.append(targetcompany(
        jobject['Rows'][i]["cite"], #url of company
        jobject['Rows'][i]["emailaddresstag"],
        jobject['Rows'][i]["phonenumbertag"))

#make an empty list for csvalues
linecsv = ""

for c in targetcompanies:
    lincsv += str(c.company)


#
text_file = open("./dumpdata.csv", "w")
text_file.write("%s" % linecsv)
text_file.close() '''

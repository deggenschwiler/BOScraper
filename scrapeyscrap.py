import csv
import requests
import json
from bs4 import BeautifulSoup
import operator
import sys

data = sys.argv[1]
response = requests.get(data)
jobject = json.loads(response.content.decode('utf8'))

newdict = jobject

list_of_rows = []

class doopydooper:
    serialno = ""
    jihgfhtd = 0
    colour = 'A'
    dfghvjgdx = 0
    fvjhdbhjvdbvd = ""
    qwtdvub = 0.0
    tyrertre = 0
    nuiolipoiutras = ""
    hftd = ""
    bhytfcde = ""
    oiuytrxcvfg = False
    dffgs = ""
    partgbfg = ""
    zserdfvbgyuikl = 0
    opiuytrzxcfgfdvg = ""

    # The class "constructor" - It's actually an initializer
    def __init__(self, serialno, jihgfhtd, iuyftdts, dfghvjgdx, fvjhdbhjvdbvd, qwtdvub, tyrertre, nuiolipoiutras, hftd, bhytfcde, oiuytrxcvfg, dffgs, partgbfg, zserdfvbgyuikl, opiuytrzxcfgfdvg):
        self.serialno = serialno
        self.jihgfhtd = jihgfhtd
        self.iuyftdts = iuyftdts
        self.dfghvjgdx = dfghvjgdx
        self.fvjhdbhjvdbvd = fvjhdbhjvdbvd
        self.qwtdvub = qwtdvub
        self.tyrertre = tyrertre
        self.nuiolipoiutras = nuiolipoiutras
        self.hftd = hftd
        self.bhytfcde = bhytfcde
        self.oiuytrxcvfg = oiuytrxcvfg
        self.dffgs = dffgs
        self.partgbfg = partgbfg
        self.zserdfvbgyuikl = zserdfvbgyuikl
        self.opiuytrzxcfgfdvg = opiuytrzxcfgfdvg

gioobles = []
stinrgly = ["L^kbZeGh" , "<nm@kZ]^B=" , "<hehk" , "<ZkZm" , "<eZkbmr" , "=^ima" , "MZ[e^" , "Ihebla" , "Lrf" , "@bk]e^" , "<ne^m" , "BfZ`^" , "F^Zl" , "Ikb\^" , "<hngmkr"]
for stringonf in stinrgly:
    sdjhvbeuvyrb = ''.join(chr(ord(letter)+7) for letter in stringonf)
    gioobles.append(sdjhvbeuvyrb)

doopydoopers = []

for i in range(0, len(jobject['Rows'])):
    doopydoopers.append(doopydooper(
        jobject['Rows'][i][gioobles[0]],
        int(jobject['Rows'][i][gioobles[1]]),
        jobject['Rows'][i][gioobles[2]],
        jobject['Rows'][i][gioobles[3]],
        jobject['Rows'][i][gioobles[4]],
        float(jobject['Rows'][i][gioobles[5]]),
        int(jobject['Rows'][i][gioobles[6]]),
        jobject['Rows'][i][gioobles[7]],
        jobject['Rows'][i][gioobles[8]],
        jobject['Rows'][i][gioobles[9]],
        jobject['Rows'][i][gioobles[10]],
        jobject['Rows'][i][gioobles[11]],
        str(jobject['Rows'][i][gioobles[12]]),
        jobject['Rows'][i][gioobles[13]],
        jobject['Rows'][i][gioobles[14]]))

#how many on the market?
numrows = str(len(jobject['Rows']))
print("There are " + numrows + " options available.")

linecvs = ""
count = 0

#pick best one
filtereddoopydoopers = []
for d in doopydoopers:
    if(d.opiuytrzxcfgfdvg == "USA"):
        if(d.jihgfhtd <= 2):
            if(d.qwtdvub <= 61.8 and d.qwtdvub >= 59.0):
                if(d.tyrertre >= 53 and d.tyrertre <= 58 and (d.fvjhdbhjvdbvd == "IF" or d.fvjhdbhjvdbvd == "VVS1")):
                    if(d.iuyftdts == "D" or d.iuyftdts == "E"):
                        if(count == 1):
                            #print('\n', end="")
                            linecvs += '\n'
                        count = 1
                        #print(str(d.serialno) + ", " + str(d.iuyftdts) + ", " + str(d.dfghvjgdx) + ", " + str(d.fvjhdbhjvdbvd) + ", " + str(d.qwtdvub) + ", " + str(d.tyrertre) + ", " + str(d.nuiolipoiutras) + ", " + str(d.hftd) + ", " + str(d.bhytfcde) + ", " + str(d.oiuytrxcvfg) + ", " + str(d.dffgs) + ", " + str(d.partgbfg) + ", " + str(d.zserdfvbgyuikl), end="")
                        linecvs += str(d.serialno) + ", " + str(d.iuyftdts) + ", " + str(d.dfghvjgdx) + ", " + str(d.fvjhdbhjvdbvd) + ", " + str(d.qwtdvub) + ", " + str(d.tyrertre) + ", " + str(d.nuiolipoiutras) + ", " + str(d.hftd) + ", " + str(d.bhytfcde) + ", " + str(d.oiuytrxcvfg) + ", " + str(d.dffgs) + ", " + str(d.partgbfg) + ", " + str(d.zserdfvbgyuikl)
                        filtereddoopydoopers.append(d)
                        #print(", <------ GOODIE", end="")
                        linecvs += ", <----- GOODIE"
print('\n')
linecvs += '\n'

#how many ideal?
numgood = str(len(filtereddoopydoopers))
print("There are " + numgood + " really great options.")

# 12/4/17 === 1*2*4*1*7 = 56 --> 0.56 dfghvjgdx
text_file = open("./dbdump.csv", "w")
text_file.write("%s" % linecvs)
text_file.close()

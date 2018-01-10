import argparse
import subprocess
import smtplib
import datetime
import os
from email.mime.text import MIMEText

parser = argparse.ArgumentParser(description='A software to automate tests with predefined data sets on '
                                             'specified programs written on C/C++')
parser.add_argument('--program', '-p', required=True, dest='program',
                    help='Program which will be tested')
parser.add_argument('--output-type', '-t', required=True, default="file", choices=['file', 'mail'],
                    help='Output type: send to your mail or save to file', dest='type')
parser.add_argument('--input-sets', '-s', required=True, dest='sets',
                    help='Predefined data set for tests')
parser.add_argument('--output', '-o', default="info.txt",
                    help='File with information about output file name or with e-mail.', dest='output')
parser.add_argument('--input-file', '-i', required=True, dest='input',
                    help='Input file name for program')

args = parser.parse_args()

programName = args.program;
outputType = args.type;
inputFile = args.sets;
outputDestination = args.output;
inputFileName = args.input;

def readDest(file):
    handler = open(file)
    destination = handler.read().strip()
    return destination

def readSets(file):
    tmpDict = dict()
    handler = open(file)
    for line in handler:
        tmpString = line.split()
        tmpDict[tmpString[0]] = tmpString[1]
    handler.close()
    return tmpDict

def runSoft(file, inName, parFirst, parSecond):
    p = subprocess.Popen(['./{0}'.format(file), '{0} {1} {2}'.format(inName, parFirst, parSecond)], stdout=subprocess.PIPE)
    result, error = p.communicate()
    print(result.decode("utf-8"))
    return result

def saveData(type, data, dest):
    if type == 'mail':
        sendMail(data, dest)
    if type == 'file':
        saveToFile(data, dest)

def saveToFile(data, dest):
    handler = open(dest, 'w')
    handler.write(data)
    handler.close()

def sendMail(data, dest):
    msg = MIMEText(data)
    me = 'results@gebka.cloud'
    msg['Subject'] = 'Data set @{0}'.format(datetime.datetime.now().time())
    msg['From'] = me
    msg['To'] = dest
    s = smtplib.SMTP('localhost')
    s.sendmail(me, [dest], msg.as_string())
    s.quit()


dataSets = readSets(inputFile)
result = ""
dataList = list()
for key in dataSets.keys():
    result += runSoft(programName, inputFileName, key, dataSets[key])
    result += '\t'

saveData(outputType, result, readDest(outputDestination))






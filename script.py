import os
import csv

file =  open ('DataMiner.csv', newline = '')
reader = csv.reader(file)

header = next(reader)

profileNameList = []

for row in reader:
    profileName = (row[0])
    profileNameList.append(profileName)


os.system('cd profiles')
os.system('instagram-scraper %s' % (profileNameList))


#os.system('instagram-scraper {profilename}')

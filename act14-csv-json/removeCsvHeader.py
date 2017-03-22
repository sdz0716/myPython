#! python3
# remooveCsvHeader.py - remove CSV files' head line

import csv
import os

os.makedirs('C:\\Users\\daize\\Desktop\\pythontest\\Automate\\csv\\headerRemoved', exist_ok=True)       #活用os相关方法
os.chdir('C:\\Users\\daize\\Desktop\\pythontest\\Automate\\csv')
for filename in os.listdir('C:\\Users\\daize\\Desktop\\pythontest\\Automate\\csv'):
    if filename.endswith('.csv'):
        lstNew = []
        file = open(filename)
        fileNew = open('C:\\Users\\daize\\Desktop\\pythontest\\Automate\\csv\\headerRemoved\\%s' % filename, 'w', newline='')
        csvReader = csv.reader(file)
        csvWriter = csv.writer(fileNew)
        for line in csvReader:
            if csvReader.line_num != 1:
                # print(csvReader.line_num)
                # print(line)
                csvWriter.writerow(line)
        file.close()
        fileNew.close()

        # fileNew = open('C:\\Users\\daize\\Desktop\\pythontest\\Automate\\csv\\headerRemoved\\%s' % filename, 'w', newline='')
        # csvWriter = csv.writer(fileNew)
        # csvWriter.writer
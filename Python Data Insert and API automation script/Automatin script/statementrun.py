#!/usr/bin/env python

# assuming a csv file with a account numbers in column 0 and The Amount in column 1
# Currency in Column 3 and Date plus time in Column 4

import requests
import csv
import json
import time
import datetime

allRows = []
# open file to read
with open("statementdata.csv", 'r') as csvfile:
# iterate on all lines
    i = 0
    for line in csvfile:
        data = line.strip().split(',')
        print(data)

        # API calling and data inserting from CSV
        # taking date and hour in format by following the column no of CSV file, table in DB, Time stamp also

        dtString = data[3]
        element = datetime.datetime.strptime(dtString, "%Y-%m-%d %H:%M:%S")
        timestampData = datetime.datetime.timestamp(element)
        print(timestampData)

        url = "http://localhost:9999/statements"
        # url is the hosting address at local

        dataDict = { "statement": {"account_id": data[0], "amount": data[1], "currency": data[2], "date": timestampData} }
        jsonObj  = json.dumps(dataDict)
        print (jsonObj)
        #exit()
        r = requests.post(url, data=jsonObj)

        # get api statistics into allRows to save in csv
        data.append(timestampData)
        data.append(r.status_code)
        data.append(r.elapsed.total_seconds())

        print("Response status code:", r.status_code)
        print("Response content:", r.text)

        allRows.append(data)
        # exit();

# write the new csv with result of API response time and status code and also storing the timestamp data
with open('statements_result.csv', "a+", newline='') as fw:
    writer = csv.writer(fw)
    writer.writerows(allRows)
fw.close()

import sys
import json
import re
import csv

for i in range(1, 21):
    f = open("./jsonFiles/j" + str(i) + ".json", "r")
    jsonify = json.loads(f.read())

    full_despription = jsonify[0]["textAnnotations"][0]["description"]

    split_despcription = full_despription.split("\n")
    phoneHits = []

    for token in split_despcription:
        result = re.findall(
            "\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}", token)
        if len(result) > 0:
            phoneHits.append(result[0])

    # Reformatting numbers to match csv file format
    newPhoneHits = []
    for phone in phoneHits:
        newPhone = phone.replace(
            "-", "").replace("(", "").replace(")", "").replace(" ", "")
        newPhoneHits.append(newPhone)

    with open("./supplierLists/supplierlist1.csv", "r") as csv_file1:
        csv_reader1 = csv.DictReader(csv_file1)
    with open("./supplierLists/supplierlist2.csv", "r") as csv_file2:
        csv_reader2 = csv.DictReader(csv_file2)
        
    for newPhone in newPhoneHits:
        found = False
        lineNum = 0
        for row in csv_reader1:
            if (lineNum == 0):
                # skip first row which is headers
                pass
            else:
                if(newPhone == row["Phone"]):
                    name = row["Business Name"]
                    print(
                        f"Supplier name: {name}, csv1, Line number: {lineNum+2}")
                    found = True
                    break
            lineNum += 1
        if (not found):
            lineNum = 0
            for row in csv_reader2:
                if (lineNum == 0):
                    # skip first row which is headers
                    pass
                else:
                    if(newPhone == row["Phone"]):
                        name = row["Business Name"]
                        print(
                            f"Supplier name: {name}, csv2, Line number: {lineNum+2},  ")
                lineNum += 1

    # print(f"{i} - {newPhoneHits}")

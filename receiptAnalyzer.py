import sys
import json
import csv

jsonFilePath = sys.argv[1]

for j in range(1,21):
    f = open(jsonFilePath + "\\j" + str(j) + ".json", "r")
    jsonify = json.loads(f.read())
    f.close()

    full_description = jsonify[0]["textAnnotations"][0]["description"]
    split_description = full_description.split("\n")

    found_in = -1


    def removeTags(token):
        simple_token = token.replace(
            "-", "").replace("(", "").replace(")", "").replace(" ", "").replace(".", "")
        return simple_token


    with open(".\\supplierLists\\supplierlist1.csv",
              "r") as f:
        supplierList = csv.DictReader(f)
        matchRow = []
        i = 0
        found = False
        for row in supplierList:
            if not found:
                i += 1
                if row["Phone"] != '0':
                    number_of_tokens = 15
                    for token in split_description:
                        number_of_tokens -= 1
                        if row["Phone"] in removeTags(token):
                            print("Found NUM Match!!!")
                            matchRow = row
                            found = True
                            found_in = 1
                            break
                        if number_of_tokens == 0:
                            break
        f.close()

    if matchRow == []:
        with open(".\\supplierLists\\supplierlist2.csv",
              "r") as f:
            supplierList = csv.DictReader(f)
            matchRow = []
            i = 0
            found = False
            for row in supplierList:
                if not found:
                    i += 1
                    if row["Phone"] != '0':
                        number_of_tokens = 15
                        for token in split_description:
                            number_of_tokens -= 1
                            if row["Phone"] in removeTags(token):
                                print("Found NUM Match!!!")
                                matchRow = row
                                found = True
                                found_in = 2
                                break
                            if number_of_tokens == 0:
                                break
            f.close()
    if matchRow == []:
        with open(".\\supplierLists\\supplierlist1.csv",
              "r") as f:
            supplierList = csv.DictReader(f)
            matchRow = []
            i = 0
            found = False
            for row in supplierList:
                if not found:
                    i += 1
                    number_of_tokens = 15
                    for token in split_description:
                        number_of_tokens -= 1
                        if len(row["Business Name"]) > 3 and row["Business Name"].lower() in token.lower():
                            print("Found WORD Match!!!")
                            matchRow = row
                            found = True
                            found_in = 1
                            break
                        if number_of_tokens == 0:
                            break
            f.close()

    if not matchRow:
        with open(".\\supplierLists\\supplierlist2.csv",
              "r") as f:
            supplierList = csv.DictReader(f)
            matchRow = []
            i = 0
            found = False
            for row in supplierList:
                if not found:
                    i += 1
                    number_of_tokens = 15
                    for token in split_description:
                        number_of_tokens -= 1
                        if len(row["Business Name"]) > 3 and row["Business Name"].lower() in token.lower():
                            print("Found WORD Match!!!")
                            matchRow = row
                            found = True
                            found_in = 2
                            break
                        if number_of_tokens == 0:
                            break
            f.close()
    print("Done Running File " + str(j) + ". \n\t Found at row: " + str(i + 1) + " in supplierlist" +
          str(found_in) + ".csv" + "\n\t Supplier Name: " + matchRow["Business Name"] + "\n\t SIC4: " + matchRow["SIC4 Category"] + "\n\t SIC8: " + matchRow["SIC8 Category"])

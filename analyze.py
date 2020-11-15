import sys
import json
import re

# # total arguments
# n = len(sys.argv)
# print("Total arguments passed:", n)
#
# # Arguments passed
# print("\nName of Python script:", sys.argv[0])

# print("\nArguments passed:")
# for i in range(1, n):
#     print(sys.argv[i])

for i in range(1, 21):
    f = open("./jsonFiles/j" + str(i) + ".json", "r")
    jsonify = json.loads(f.read())

    full_despription = jsonify[0]["textAnnotations"][0]["description"]

    split_despcription = full_despription.split("\n")
    phoneHits = []

    for token in split_despcription:
        result = re.findall("\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}",
                      token)
        if len(result) > 0:
            phoneHits.append(result[0])

    print(phoneHits)

# print(re.split("\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}", receipt_despcription))

# print(jsonify[0]["textAnnotations"][0]["description"].split("\n"))

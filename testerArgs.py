import sys
import json
 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:")
for i in range(1, n):
    print(sys.argv[i])
     
f = open(sys.argv[1], "r")
jsonify = json.loads(f.read())

print(jsonify[0]["textAnnotations"][2])
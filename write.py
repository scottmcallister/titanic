import csv
import numpy as np

test_file = open("test.csv", "rb")
test_file_object = csv.reader(test_file)
header = test_file_object.next()

output_file = open("genderbasemodel.csv", "wb")
output = csv.writer(output_f)

output.writerow(["passenger", ""])
for row in test_file_object:
    if row[3] == "female":
        output.writerow(row[0], 1)
    else:
        output.writerow(row[0], 0)
output_file.close()
test_file.close

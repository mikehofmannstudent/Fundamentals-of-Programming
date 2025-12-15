import csv

with open('results.csv') as f:
    reader = csv.DictReader(f)
    for line in reader:
        sn = line.get("student_number")
        fname = line.get("first_name")
        lname = line.get("last_name")
        score = line.get("score")
        print(sn, fname, lname, score)

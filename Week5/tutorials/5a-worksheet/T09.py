csvContent = """student_number,first_name,last_name,score
A111,John,Smith,90
B222,Peter,Martin,80
C333,Bob,Ross,98"""

with open('results.csv', 'w') as f:
    f.write(csvContent)

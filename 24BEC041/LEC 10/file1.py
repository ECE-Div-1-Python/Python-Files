import csv
data=[['sr_no.','Roll_no.','Name'],
      ['1.','24BEC050','Divyam'],
      ['2.','24BEC022','Foram'],
      ['3.','24BEC031','devansh'],
      ['4.','24BEC041','Riddhi']]

file= "files/new.csv"
with open(file, 'w', newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(data)
print(f"CSV file '{file}' created successfully!")

import csv
import os

# Read the CSV file
with open('jika.csv', 'r', newline='',encoding="utf-8_sig") as csvfile:
   reader = csv.reader(csvfile)
   header = next(reader)
   rows = []
   for row in reader:
       new_row = []
       for i, col in enumerate(row):
           if i == 2:
               col = float(col.replace('$', '').replace(',', ''))
           elif i == 8:
               col = float(col.split()[0].replace(',', ''))
           new_row.append(col)
       rows.append(new_row)

# Calculate the value for the 11th column
kijyun = float(rows[0][8])

print(kijyun)
for i, row in enumerate(rows[0:]):
   bairitu = round(float(row[8]) / kijyun, 1)
   row.append(bairitu)
   row.append(int((float(row[8]) / kijyun) * float(row[2])))

# Write the converted data to a new CSV file
with open('jika_converted.csv', 'w', newline='') as csvfile:
   writer = csv.writer(csvfile)
   writer.writerow(header + ['bairitu']+['fixd_jika(US$)'])
   for row in rows:
       writer.writerow(row)
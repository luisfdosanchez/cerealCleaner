import csv
import os

inputfile=os.path.join(".","resources","cereal.csv")

with open(inputfile, "r", encoding="UTF-8") as csvfile:
    readcsv=csv.reader(csvfile,delimiter=",")

    title=next(readcsv)
    print(f"Varnames are: {title}")

    for row in readcsv:
        if float(row[7])>=5:
            print(row)

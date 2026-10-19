import csv

def to_csv(rows, out):
    csv.writer(out).writerows(rows)

from django.core.management.base import BaseCommand
import csv

with open ('TACO.csv') as f:
    csv_reader=csv.reader(f)
    reader = csv.reader(f)
    for row in reader:
        print(row)

#!/usr/bin/python

import csv

def calculated_test_coverage():
    with open(file="target/site/jacoco/jacoco.csv", mode="r") as file:
        csv_reader = csv.reader(file, delimiter=',') # makes csv easier to handle
        next(csv_reader) # skip titles on first line
        covered = 0
        missed = 0
        for lines in csv_reader: 
            missed += int(lines[3])
            covered += int(lines[4])
        return str(int(covered/(missed+covered)*100))+"%"

print(calculated_test_coverage())
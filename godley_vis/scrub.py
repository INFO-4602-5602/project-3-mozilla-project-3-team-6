#!/usr/bin/env python3

import csv
import re
import pickle
import operator
import numpy as np
from matplotlib import pyplot as plt

class ScrubData():
    def __init__(self, data_dir = "./data/", data_file = "20171013111831-SurveyExport.csv"):
        self.data_dir = data_dir
        self.data_file = data_file
        self.data_file_path = data_dir+data_file
        self.data = {}
        self.header = []

    def scrub(self, encoding="ISO-8859-1"):
        with open(self.data_file_path, 'r', encoding=encoding) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            i = 0
            for row in spamreader:
                if i>0:
                    for j in range(len(row)):
                        #print("data[%s][%s]): %s" % (row[0], self.header[j], row[j]))
                        if j==0:
                            self.data[row[0]] = {}
                            self.data[row[0]][self.header[j]] = row[j]
                            #print(self.data[row[0]][self.header[j]])
                        else:
                            self.data[row[0]][self.header[j]] = row[j]
                else:
                    self.header = row
                i += 1
            print("Parsed %i lines from %s" % (i, self.data_file_path))

    def dump(self):
        pickle.dump(self.data, open("%s.p" % self.data_file[:-4], "wb"))
        pickle.dump(self.header, open("header.p", "wb"))
        print("Data pickled to %s.p" % self.data_file[:-4])

    def load(self, data_file=None):
        if data_file==None:
            self.data = pickle.load(open("%s.p" % self.data_file[:-4], "rb"))
            self.header = pickle.load(open("header.p", "rb"))
            print("Data loaded from %s.p" % self.data_file[:-4])
        else:
            return pickle.load(open("%s.p" % data_file, "rb"))
            print("Data loaded from %s.p" % self.data_file)

if __name__ == "__main__":
    scrubber = ScrubData()
    #scrubber.scrub()
    #scrubber.dump()
    scrubber.load()
    record = "1"
    header = scrubber.header[10]
    #print("data[%s][%s] = %s" % (record, header, scrubber.data[record][header]))
    for header in scrubber.header:
        print(header)


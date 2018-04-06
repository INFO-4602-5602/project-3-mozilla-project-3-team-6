#!/usr/bin/env python3

import csv
import re
import pickle
import operator
import numpy as np
from matplotlib import pyplot as plt

'''
Response ID
Time Started
Date Submitted
Status
Language
Country
Link Name
I consider myself:
WiFi Router:Check all the internet connected devices you currently own:
Laptop computer:Check all the internet connected devices you currently own:
Smart phone:Check all the internet connected devices you currently own:
Smart TV:Check all the internet connected devices you currently own:
Activity Tracker (ex: Fitbit or Apple Watch):Check all the internet connected devices you currently own:
Smarthome Hub (ex. Amazon Echo, Google Alexa):Check all the internet connected devices you currently own:
Car that connects to the internet:Check all the internet connected devices you currently own:
Smart Thermostat (ex: Nest):Check all the internet connected devices you currently own:
Smart Appliance (ex. Coffeemaker, Refrigerator, Oven, Fridge):Check all the internet connected devices you currently own:
Smart Door Locks (ex. Door locks for your home you can open via bluetooth):Check all the internet connected devices you currently own:
Smart Lighting (ex. Connected lighting switches, dimmers, or bulbs):Check all the internet connected devices you currently own:
Thinking about a future in which so much of your world is connected to the internet leaves you feeling:
What are you most excited about as we move toward a more digitally connected future?
What is your biggest fear as we move towards a more connected future?
Who is most responsible for protecting the online safety, privacy, and security of the connected apps and devices you own?
Who do you most trust to help you learn how to protect your safety, security and privacy online?
Price:You're planning on buying your next cool new tech toy. Maybe it's a smart TV or a new smartphone. åÊTake a look at the items below and arrange them in order of importance as you make that purchase.
Features:You're planning on buying your next cool new tech toy. Maybe it's a smart TV or a new smartphone. åÊTake a look at the items below and arrange them in order of importance as you make that purchase.
Safety:You're planning on buying your next cool new tech toy. Maybe it's a smart TV or a new smartphone. åÊTake a look at the items below and arrange them in order of importance as you make that purchase.
Security:You're planning on buying your next cool new tech toy. Maybe it's a smart TV or a new smartphone. åÊTake a look at the items below and arrange them in order of importance as you make that purchase.
Privacy:You're planning on buying your next cool new tech toy. Maybe it's a smart TV or a new smartphone. åÊTake a look at the items below and arrange them in order of importance as you make that purchase.
Reliability:You're planning on buying your next cool new tech toy. Maybe it's a smart TV or a new smartphone. åÊTake a look at the items below and arrange them in order of importance as you make that purchase.
User Reviews:You're planning on buying your next cool new tech toy. Maybe it's a smart TV or a new smartphone. åÊTake a look at the items below and arrange them in order of importance as you make that purchase.
Expert Recommendation:You're planning on buying your next cool new tech toy. Maybe it's a smart TV or a new smartphone. åÊTake a look at the items below and arrange them in order of importance as you make that purchase.
Friend or Family Recommendation:You're planning on buying your next cool new tech toy. Maybe it's a smart TV or a new smartphone. åÊTake a look at the items below and arrange them in order of importance as you make that purchase.
Convenience:You're planning on buying your next cool new tech toy. Maybe it's a smart TV or a new smartphone. åÊTake a look at the items below and arrange them in order of importance as you make that purchase.
IoT:Check all the terms below that you could explain to a friend:
Connected Devices:Check all the terms below that you could explain to a friend:
Botnet:Check all the terms below that you could explain to a friend:
Blockchain:Check all the terms below that you could explain to a friend:
RFID:Check all the terms below that you could explain to a friend:
DDOS:Check all the terms below that you could explain to a friend:
Zero Day:Check all the terms below that you could explain to a friend:
VPN:Check all the terms below that you could explain to a friend:
TOR:Check all the terms below that you could explain to a friend:
I don't know what any of these things are:Check all the terms below that you could explain to a friend:
Country or Region (optional)
'''

class ScrubData():
    def __init__(self, data_dir = "./data/", data_file = "20171013111831-SurveyExport.csv"):
        self.data_dir = data_dir
        self.data_file = data_file
        self.data_file_path = data_dir+data_file
        self.header = []
        self.data = []


    def scrub(self, encoding="ISO-8859-1"):
        with open(self.data_file_path, 'r', encoding=encoding) as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for i, row in enumerate(spamreader):
                if i == 0:
                    self.header = row
                else:
                    info = { }
                    for field, value in zip(self.header, row):
                        info[field] = value

                    self.data.append(info)


    def dump(self):
        pickle.dump(self.data, open("%s.p" % self.data_file[:-4], "wb"))
        pickle.dump(self.header, open("header.p", "wb"))
        print("Data pickled to %s.p" % self.data_file[:-4])

    def load(self, data_file=None):
        if data_file==None:
            self.data = pickle.load(open("%s.p" % self.data_file[:-4], "rb"))
            self.header = pickle.load(open("header.p", "rb"))
        else:
            return pickle.load(open("%s.p" % data_file, "rb"))


# 4 Language
# 5 Country
# 20 What are you most excited about as we move toward a more digitally connected future?
# 21 What is your biggest fear as we move towards a more connected future?
from collections import defaultdict
def parse(header, data):
    fields = [header[x] for x in [4, 5, 20, 21]]

    filtered_data = [ [ row[field] for field in fields ] for row in data ]   
    by_field = []
    for i in range(len(fields)):
        by_field.append([ row[ i ] for row in filtered_data ])

    languages_vales = by_field[0]
    countries_values = by_field[1]
    positives_values = by_field[2]
    negatives_values = by_field[3]

    languages = set(languages_vales)
    countries = set(countries_values)
    positives = set(positives_values)
    negatives = set(negatives_values)

    output_info = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    for i, (c, p, n) in enumerate(zip(countries_values, positives_values, negatives_values)):
        c = c.encode('ascii',errors='ignore').decode("utf-8")
        p = p.encode('ascii',errors='ignore').decode("utf-8")
        n = n.encode('ascii',errors='ignore').decode("utf-8")
        output_info['positive'][p][c] += 1
        output_info['negative'][n][c] += 1


    with open('output.csv', 'w') as f:
        f.write("sentiment,country,question,count\n")
        for c in countries:
            for p in positives:
                f.write("{0},{1},{2},{3}\n".format('positive', c, p, output_info['positive'][p][c]))
            for n in negatives:
                f.write("{0},{1},{2},{3}\n".format('negative', c, n, output_info['negative'][n][c]))


if __name__ == "__main__":
    scrubber = ScrubData()
    # scrubber.scrub()
    # scrubber.dump()
    scrubber.load()
    parse(scrubber.header, scrubber.data)

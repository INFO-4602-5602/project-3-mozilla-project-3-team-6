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

def search_data(data, header, criteria):
    x, y = []
    for record in range(len(data)):
        if criteria in data[record][header]:
            x.append(record)

    return x, y

def plott(x, y, xlabel="X", ylabel="Y", title="X vs Y"):
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(xlabel+"_vs_"+ylabel+".png")
    plt.show()

if __name__ == "__main__":
    scrubber = ScrubData()
    #scrubber.scrub()
    #scrubber.dump()
    scrubber.load()
    record = "1"
    header = scrubber.header[10]
    #print("data[%s][%s] = %s" % (record, header, scrubber.data[record][header]))
    i = 0
    for header in scrubber.header:
        print(str(i)+": "+header)
        i += 1

    quit()
    search_data(scrubber.data, scrubber.header[7])



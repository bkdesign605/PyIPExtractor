#!/usr/bin/python3
#
# CYB333: Final Course Project
# Project Title: IP Extractor
# Project Option: Count the frequency of IP Addresses in a (.txt) weblog.
# Display top 10 and how many duplicates were found.
# Author: BKdesign605
# Date: June 21, 2021
#

from tkinter import *  # import tkinter GUI toolkit
from tkinter import filedialog  # from tkinter import the filedialog module
from collections import Counter
import sys
import re  # import regex (regular expression)
import time  # import time module

root = Tk()  # initialize interpreter, create root window
root.withdraw()  # closes tkinter root window

print("—" * 45)
print("Welcome to IP Extractor")
print("Created by: BKdesign610")
print("—" * 45)
time.sleep(1)

print("Please select a .txt file from your desktop")
print("—" * 45)
time.sleep(.5)


#  Open file box, user can select file.
log = filedialog.askopenfile(filetypes=(('text files', '.txt'),), parent=root, initialdir="Desktop:/",
                             title='Please select a log file')


def linecount():
    try:
        total_number_lines = 0
        with open(log.name) as infile:  # count the number of lines in the file that was uploaded
            for line in infile:
                total_number_lines += 1
        return total_number_lines
    except:
        print('There was an error opening the file, please try again!')
        sys.exit(0)


def main():

    try:
        # read log with variable "text" assigned.
        text = log.read()
        # Regex expression to find ip addresses in text.
        ip_address = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
        counts = dict()
        total_ipaddress = 0
        no_multiples = 0
        t = Counter(ip_address)
        high = t.most_common(10)  # Count top 10 ip addresses
        now = time.strftime('%I:%M:%S %p')
        end = time.strftime('%I:%M:%S %p')
        timer = time.time()

        for line in ip_address:
            text = line.split()
            log.close()
            # Count the number of times each ip address appears in log.
            for ip_address in text:
                total_ipaddress += 1
                if ip_address not in counts:
                    counts[ip_address] = 1  # found ip address once once.
                else:
                    counts[ip_address] += 1  # found multiples of the same address add +1.
                    no_multiples = total_ipaddress - len(counts)
        lst = list(counts.items())  # sort list by how many times each ip address is found in log.
        lst.sort(key=lambda x: x[1], reverse=True)  # sort list in reverse, print IPs found highest to lowest.
        time.sleep(1)
        print("Thank you for uploading your weblog!")
        print("—" * 45)
        time.sleep(2)
        print("Please hold a moment, while I scan your file for IP Addresses.\n" "Your scan started at: ", now)
        print("—" * 65)
        time.sleep(3)

        # print all ip addresses found in file (key, val).
        for key, val in lst:
            time.sleep(.02)
            print("IP Address:", key, "is found", val, "times(s).")  # print ip address final list.

        time.sleep(1)
        print("—" * 50)
        # print top 10 IP address found in the list.
        print("Top 10 IP Addresses:")
        print("—" * 50)
        for key, val in high:
            time.sleep(.02)
            print("IP Address:", key, "is found", val, "times(s).")

        time.sleep(1)
        print("—" * 50)
        # print total number of IP addresses found in the list.
        print('Total number of IP Addresses:')
        print("—" * 50)
        time.sleep(1)
        print('%d were found in your weblog file.' % total_ipaddress)
        print('%d were found multiple times.' % len(counts))
        print('%d were found only once.' % no_multiples)
        print('Out of a total of %d lines in your file.' % linecount())
        time.sleep(1)
        print("—" * 50)
        print('Thank you, your search is now complete!\n' 'Your scan ended at: ', end)
        print('It took:', time.time() - timer, 'seconds to scan your file.')
        # get user input to exit Python program once it has completed extracting the IP addresses.
        input('Press ENTER to exit')
    except KeyboardInterrupt:
        print('Scan was interrupted, please try again!')
        pass
    except UnicodeDecodeError:
        print('There was no IP Addresses found in your file, please try a different weblog!')
        sys.exit(0)
    except IOError:
        print('There was an error opening the file, please try again!')
        sys.exit(0)


if __name__ == "__main__":
    main()

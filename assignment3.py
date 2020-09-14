#!/usr/bin/env python
# _*_ coding: utf-8 _*_

#week3 assignment3
#Lang | 9/14/2020 | I was lost, needed help from a friend but I learn alot as well.

import urllib2
import csv
import datetime
import logging
import argparse
import sys
import re

#Part1 : Pull down web log file
def downloadData (url):
    """Takes in a string called url to download contents located at url and return to caller.

    Args:
        url(str): the url to be call/open

    Returns:
        myfile : infomation from the data in URL.

    Examples:
         >>> downloadData(https:www.wikipedia.com)
    """
   myfile = urllib2.urlopen(url)
   return myfile

#_________________________________________________________________________________________________
#Part2,3,4 : Process File using CSV, Search for image and browser hits
#Print out "Image requests account for 45.3% of all requests"
#Print out which browser is the most popular that day.
def processData(myfile):
    """Process data from file line by line.

    Args:
        myfile(csv) : A .csv file of weblog

    Example:
        >>>

    """

weblog_data = csv.reader(myfile)
image_hits_dict = {"images": 0, "total":0}   #store imgae hits in a dictionary
browser_hits_dict = {"Chrome": 0,"Firefox":0, "IE": 0,"Safari":0} #store browser hits in a dict

    for (line, col) in enumerate(weblog_data):
        image_hits_dict["total"] += 1  #update the total hits count

        if re.search(r"\.(?:jpe|jpeg|gif|png|PNG)$", col[0]):   #PNG for capital letter
            image_hits_dict["images"] +=1  #look for image hits with extensions

        if re.search("chrome", col[2], re.I):   #search for chrome hit, re.I to ignorelettercase
            browser_hits_dict["Chrome"] += 1
        elif re.search("safari", col[2], re.I)and not re.search("chrome", col[2],re.I):
            browser_hits_dict["Safari"] +=1   #should be safari and NOT chrome
        elif re.search("firefox",col[2], re.I):
            browser_hits_dict["Firefox"] +=1
        elif re.search("msie", col[2], re.I):
            browser_hits_dict["IE"] +=1  #msie was a bit hard to find :D

    percent_of_image_hits = round((float(image_hits_dict["images"]) / image_hits_dict["total"]) * 100, 2)
    #looking for most hits/use browser
    poplar_browser = max (browser_hits_dict.items(), key=operator.itemgetter(1))
    #never use/heard of operator.itemgetter before/ need to learn about it.
    #A friend show me it should work with the problem here.

#Print out to screen for result
    print("Image requests account for {}% of all hits."
          .format(percent_of_image_hits)
    print("Most popular browser used on 1/27/2014 was {}."
          .format(popular_browser)
    
#____________________________________________________________________________________________________
#Part5 : Putting it all together(main function). using argparse module
def main():
    """ A function to be called when the program runs."""

#--url argument set up with argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--url",help="URL of CSV to download")
    args = parser.parse_args()

    if args.url:
        try:
            csvData = downloadData(args.url)
        except urllib2.URLError:
            print ("Can't retrieve, please check and try the URL again")
            sys.exit()

        processData(csvData)

    else:
        print ("Plese check the requirement of URL parameters")
        sys.exit()
                                     

if __name__ == '__main__':
    main()

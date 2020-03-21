#!/usr/bin/env python3
import time
import re
import requests
import argparse
from bs4 import BeautifulSoup
from optparse import OptionParser
 
refreshRate = 300
baseUrl = "https://www.worldometers.info/coronavirus/"
country = "country/"

def getStatsForCountry(countryCode):
    if not countryCode or countryCode == "ww":
        return getStatusForUrl(baseUrl)
    return getStatusForUrl(baseUrl + country + countryCode)

def getStatusForUrl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    infection_count = death_count = -1
    for el in soup.findAll('h1'):
        if "Coronavirus" in str(el):
            infection_count = re.sub("\D", "", re.sub('<[^<]+?>', '', str(el.find_next_sibling())).replace(" ", "")).replace("\n", "")
        elif "Deaths" in str(el):
            death_count = re.sub("\D", "", re.sub('<[^<]+?>', '', str(el.find_next_sibling())).replace(" ", "")).replace("\n", "")

    return (infection_count, death_count)

def write_stats(label, infection_count, death_count):
    if not label:
      label = ""
    return "{0} c: {1} d: {2} ".format(label, infection_count, death_count)

def main():
    parser = argparse.ArgumentParser(description='Optional label countryCode')
    parser.add_argument('country', type=str, nargs='?',
                        help='country code')
    parser.add_argument('label', type=str, nargs='?',
                        help='label')

    args = parser.parse_args()
    if args.label:
        label = args.label
    if not args.label and args.country:
        label = args.country
    
    try:
        (infection_count, death_count) = getStatsForCountry(args.country)
        print(write_stats(label, infection_count, death_count))
    except Exception as e:
        print("[!] Error:", e)

if __name__ == '__main__':
    main()

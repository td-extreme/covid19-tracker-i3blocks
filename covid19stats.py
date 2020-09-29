#!/usr/bin/env python3
import time
import re
import requests
import argparse
from bs4 import BeautifulSoup
from optparse import OptionParser

baseUrl = "https://www.worldometers.info/coronavirus/"
country = "country/"

def getStatsForCountry(countryCode):
    if not countryCode:
        return getStatusForUrl(baseUrl)
    if "usa/" in countryCode:
        return getStatusForUrl(baseUrl + countryCode)
    return getStatusForUrl(baseUrl + country + countryCode)

def getStatusForUrl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    infection_count = death_count = -1
    for el in soup.findAll('h1'):
        if "Coronavirus" in str(el):
            infection_count = re.sub('<[^<]+?>', '', str(el.find_next_sibling()).replace(" ", "")).replace("\n", "")
        elif "Deaths" in str(el):
            death_count = re.sub('<[^<]+?>', '', str(el.find_next_sibling()).replace(" ", "")).replace("\n", "")

    return (infection_count, death_count)

def main():
    parser = argparse.ArgumentParser(description='Optional countryCode')
    parser.add_argument('country', type=str, nargs='?',
                        help='country code')

    args = parser.parse_args()

    try:
        (infection_count, death_count) = getStatsForCountry(args.country)
        print(f" c: {infection_count} d: {death_count}")
    except Exception as e:
        print("[!] Error:", e)

if __name__ == '__main__':
    main()

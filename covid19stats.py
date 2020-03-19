import time
import re
import requests
from bs4 import BeautifulSoup
import datetime

def getStats():
    url = "https://www.worldometers.info/coronavirus/country/uk/"
    url2 = "https://www.worldometers.info/coronavirus/"

    # Get response from first URL which contains data about UK cases and deaths
    print("[!] Getting response from URL 1")
    startTime = time.time()
    response = requests.get(url)
    print("[!] Time taken to retrieve response", round((time.time() - startTime), 2))

    # Get response from second URL which contains worldwide cases and deaths
    print("[!] Getting response from URL 2")
    startTime = time.time()
    response2 = requests.get(url2)
    print("[!] Time taken to retrieve response", round((time.time() - startTime), 2))

    # Use BeautifulSoup library to parse the URLs we just retrieved
    soup = BeautifulSoup(response.text, "html.parser")
    soup2 = BeautifulSoup(response2.text, "html.parser")

    # Create empty array called stats
    stats = []

    # For each statement to catch all lines of code that contain h1 tag
    for el in soup.findAll('h1'):
        if "Coronavirus" in str(el):
            stats.append(re.sub('<[^<]+?>', '', str(el.find_next_sibling())).replace(" ", ""))
        elif "Deaths" in str(el):
            stats.append(re.sub('<[^<]+?>', '', str(el.find_next_sibling())).replace(" ", ""))

    for el in soup2.findAll('h1'):
        if "Coronavirus" in str(el):
            stats.append(re.sub('<[^<]+?>', '', str(el.find_next_sibling())).replace(" ", ""))
        if "Deaths" in str(el):
            stats.append(re.sub('<[^<]+?>', '', str(el.find_next_sibling())).replace(" ", ""))

    return stats


def main():
    difference = [0] * 4

    while True:

        try:
            oldstats = newstats

        except:
            print("start")

        try:
            newstats = getStats()

        except Exception as e:
            print("[!] Error retrieving stats; website most likely denied request. Reattempting in 60 seconds")
            time.sleep(60)
            try:
                newstats = getStats()
            except Exception as e:
                print("[!] Error retrieving second time; waiting 2m50s then running again")
                time.sleep(150)
                continue

        try:
            difference[0] += (int(re.sub("\D", "", newstats[0])) - int(re.sub("\D", "", oldstats[0])))
            difference[1] += (int(re.sub("\D", "", newstats[1])) - int(re.sub("\D", "", oldstats[1])))
            difference[2] += (int(re.sub("\D", "", newstats[2])) - int(re.sub("\D", "", oldstats[2])))
            difference[3] += (int(re.sub("\D", "", newstats[3])) - int(re.sub("\D", "", oldstats[3])))

        except Exception as e:
            print("[!] Variable old stats does not exist yet; most likely first run")

        try:
            print("[*] Updated stats at:", datetime.datetime.now())
            f = open("log.txt", "a")
            status_line = "\nUK C: {0} ({1}) UK D: {2} ({3}) WW C: {4} ({5}) WW D: {6} ({7})"
            formated_status_line = status_line.format(newstats[0], str(difference[0]), newstats[1], str(difference[1]), newstats[2], str(difference[2]), newstats[3], str(difference[3])).replace("\n", "")
            f.write("\n")
            f.write(formated_status_line)
            f.close()

        except Exception as e:
            print("[!] Error:", e)
            continue

        time.sleep(300)

if __name__ == '__main__':
    main()

'''
Created on Oct 13, 2019

@author: Elite-Intel

'''
import requests
from bs4 import BeautifulSoup
import Constants
import csv


DFO = Constants.DFO()
NST = Constants.NST()


def getNSTTeamPageSoup(teamAbbreviation):
    url = NST.TEAM_PAGE_URL.format(teamAbbreviation)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def getNSTPlayerID(soup,name):
    playerOptions = soup.find('select',{'name':NST.PLAYER_ABBREV})
    for option in playerOptions.find_all('option'):
        if(option.text == name):
            return option['value']
    return NST.DEFAULT_PLAYER_VAL

def getNumSearchablePlayers(p1,p2,p3):
    return (1 if(p1 != 0) else 0) + (1 if(p2 != 0) else 0) + (1 if(p3 != 0) else 0)

def getNSTLineStats(soup,line):
    p1 = getNSTPlayerID(soup,line[0])
    p2 = getNSTPlayerID(soup,line[1])    
    p3 = getNSTPlayerID(soup,line[2])
    numPlayers = getNumSearchablePlayers(p1,p2,p3)
    url = NST.LINE_PAGE_URL.format(p1,p2,p3)
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    table = soup.find('table', id='players')
    rows = table.find_all('tr')
    fullLineTDs= rows[1].find_all('td')
    lineData = []
    for td in fullLineTDs:
        lineData.append(td.get_text())
    return lineData[numPlayers:len(lineData)]    

    
def getDFORoster(teamName):
    url = DFO.ROSTER_URL.format(teamName)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    roster = []
    for i in range(1, DFO.MAX_LINES+1):
        line = DFO.FORWARD_ABBREV + str(i)
        forwards = soup.find(id=line)
        players = forwards.find_all(class_= DFO.PLAYER_NAME)
        lineArr = []
        for player in players:
            lineArr.append(player.get_text().strip())
        roster.append(lineArr)
    return roster

def getRosterStats(soup,roster):
    rosterWithStats = []
    for line in roster:
        rosterWithStats.append(line + getNSTLineStats(soup,line))
    return rosterWithStats

def writeToFile(roster,filename='output.csv'):
    with open(filename,'wb') as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerow(NST.DEFAULT_STATS_HEADERS)
        wr.writerows(roster)

if __name__ == '__main__':
    roster = getDFORoster("anaheim-ducks")
    soup = getNSTTeamPageSoup('ana')
    stats = getRosterStats(soup,roster)
    writeToFile(stats)
    pass
'''
Created on Oct 13, 2019

@author: Elite-Intel

'''
import csv
import datetime
import os
import time
from bs4 import BeautifulSoup
import requests
import Constants
from random import randint

DFO = Constants.DFO()
NST = Constants.NST()
NHL = Constants.NHL()

def getRequestWithSleep(URL,PARAMS=[],minSleep=1,maxSleep=10):
    page = requests.get(url=URL,params = PARAMS)
    time.sleep(randint(minSleep,maxSleep))
    return page
    

def getNSTTeamPageSoup(teamAbbreviation):
    url = NST.TEAM_PAGE_URL.format(teamAbbreviation)
    page = getRequestWithSleep(url)
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

def getNSTLineStats(line,abbr):
    soup = getNSTTeamPageSoup(abbr)
    p1 = getNSTPlayerID(soup,line[0])
    p2 = getNSTPlayerID(soup,line[1])    
    p3 = getNSTPlayerID(soup,line[2])
    numPlayers = getNumSearchablePlayers(p1,p2,p3)
    if numPlayers <= 1:
        return ['Not enough searchable players to return data!']
    url = NST.LINE_PAGE_URL.format(abbr,p1,p2,p3)
    page = getRequestWithSleep(url)
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
    page = getRequestWithSleep(url,[],0,0)
    soup = BeautifulSoup(page.content, 'html.parser')
    roster = []
    for i in range(1, DFO.MAX_LINES+1):
        line = DFO.FORWARD_ABBREV + str(i)
        forwards = soup.find(id=line)
        players = forwards.find_all(class_= DFO.PLAYER_NAME)
        lineArr = []
        for player in players:
            lineArr.append(player.get_text().encode('utf-8').strip())
        roster.append(lineArr)
    return roster

def getRosterStats(roster,abbr):
    rosterWithStats = []
    for line in roster:
        rosterWithStats.append(line + getNSTLineStats(line,abbr))
    return rosterWithStats

def writeToFile(game,filename='output.csv'):
    gameTitle = "{}@{}".format(game[NHL.AWAY]['name'],game[NHL.HOME]['name'])
    append_write = 'ab' if os.path.exists(filename) else 'wb'
    with open(filename,append_write) as result_file:
        wr = csv.writer(result_file, dialect='excel')
        wr.writerow([gameTitle])
        wr.writerow(NST.DEFAULT_STATS_HEADERS)
        wr.writerows(game[NHL.AWAY][NHL.ROSTER])
        wr.writerow(NST.DEFAULT_STATS_HEADERS)
        wr.writerows(game[NHL.HOME][NHL.ROSTER])
        wr.writerow([])

def getSchedule(date = datetime.datetime.today()):
    dateString = date.strftime('%Y-%m-%d') 
    URL = NHL.SCHEDULE_API_URL
    PARAMS = {'date':dateString}
    r = getRequestWithSleep(URL, PARAMS)
    data = r.json()
    matches = []
    for game in data['dates'][0]['games']:
        homeTeam = game['teams']['home']['team'][NHL.NAME]
        awayTeam = game['teams']['away']['team'][NHL.NAME]
        matches.append({NHL.HOME:homeTeam, NHL.AWAY:awayTeam})
    return matches

def getNSTTeamName(nhlName):
    return NHL.TEAM_NAMES[nhlName]['NST']

def getDFOTeamName(nhlName):
    return NHL.TEAM_NAMES[nhlName]['DFO']

def getLineStatsForGame(game):
    gameStats = {}
    homeNSTName = getNSTTeamName(game[NHL.HOME])
    awayNSTName = getNSTTeamName(game[NHL.AWAY])
    homeRoster = getDFORoster(getDFOTeamName(game[NHL.HOME]))
    awayRoster = getDFORoster(getDFOTeamName(game[NHL.AWAY]))
    gameStats[NHL.HOME] = {NHL.NAME:homeNSTName,NHL.ROSTER:getRosterStats(homeRoster,homeNSTName)}
    gameStats[NHL.AWAY] = {NHL.NAME:awayNSTName,NHL.ROSTER:getRosterStats(awayRoster,awayNSTName)}
    return gameStats

def scrape(date):
    games = getSchedule(date)
    for game in games:
        stats = getLineStatsForGame(game)
        writeToFile(stats)
    
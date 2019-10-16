'''
Created on Oct 13, 2019

@author: Elite-Intel

'''
import requests
from bs4 import BeautifulSoup
import Constants

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

def getNSTLineStats(soup,line):
    p1 = getNSTPlayerID(soup,line[0])
    p2 = getNSTPlayerID(soup,line[1])    
    p3 = getNSTPlayerID(soup,line[2])
    url = NST.LINE_PAGE_URL.format(p1,p2,p3)
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    table = soup.find('table', id='players')
    print table
    

    
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

if __name__ == '__main__':
    roster = getDFORoster("anaheim-ducks")
    soup = getNSTTeamPageSoup('ana')
    getNSTLineStats(soup,roster[0])
    pass
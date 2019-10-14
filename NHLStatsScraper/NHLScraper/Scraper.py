'''
Created on Oct 13, 2019

@author: Elite-Intel

'''
import requests
from bs4 import BeautifulSoup
import Constants

DFO = Constants.DFO()

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
    pass
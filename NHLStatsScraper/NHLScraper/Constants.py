'''
Created on Oct 14, 2019

@author: Elite-Intel
'''

class NST():
    TEAM_PAGE_URL = 'https://www.naturalstattrick.com/linestats.php?fromseason=20192020&thruseason=20192020&stype=2&sit=5v5&score=all&rate=n&team={}&vteam=ALL&view=wowy&loc=B&gpfilt=none&fd=2019-10-02&td=2020-04-04&tgp=2000&strict=incl'
    LINE_PAGE_URL = 'https://www.naturalstattrick.com/linestats.php?fromseason=20192020&thruseason=20192020&stype=2&sit=5v5&score=all&rate=n&team=ANA&vteam=ALL&view=wowy&loc=B&gpfilt=none&fd=2019-10-02&td=2020-04-04&tgp=2000&strict=incl&p1={}&p2={}&p3={}&p4=0&p5=0'
    PLAYER_ABBREV = 'p1'
    DEFAULT_PLAYER_VAL = 0
    
class DFO():
    '''
    classdocs
    '''
    ROSTER_URL = "https://www.dailyfaceoff.com/teams/{}/line-combinations/"
    FORWARD_ABBREV = "f"
    MAX_LINES = 4
    PLAYER_NAME = "player-name"
        


        
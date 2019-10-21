'''
Created on Oct 14, 2019

@author: Elite-Intel
'''
class NHL():
    SCHEDULE_API_URL = 'https://statsapi.web.nhl.com/api/v1/schedule'
    HOME = 'home'
    AWAY = 'away'
    NAME = 'name'
    ROSTER = 'ROSTER'
    TEAM_NAMES = {
                    'Anaheim Ducks':{'DFO':'Anaheim-Ducks','NST':'ANA'},
                    'Carolina Hurricanes':{'DFO':'Carolina-Hurricanes','NST':'CAR'},
                    'Chicago Blackhawks':{'DFO':'chicago-blackhawks','NST':'CHI'},
                    'Colorado Avalanche':{'DFO':'colorado-avalanche','NST':'COL'},
                    'Columbus Blue Jackets':{'DFO':'columbus-blue-jackets','NST':'CBJ'},
                    'Dallas Stars':{'DFO':'dallas-stars','NST':'DAL'},
                    'Detroit Red Wings':{'DFO':'Detroit-Red-Wings','NST':'DET'},
                    'Edmonton Oilers':{'DFO':'Edmonton-Oilers','NST':'EDM'},
                    'Florida Panthers':{'DFO':'florida-panthers','NST':'FLA'},
                    'New York Rangers':{'DFO':'new-york-rangers','NST':'NYR'},
                    'Ottawa Senators':{'DFO':'Ottawa-Senators','NST':'OTT'},
                    'Philadelphia Flyers':{'DFO':'Philadelphia-Flyers','NST':'PHI'},
                    'Pittsburgh Penguins':{'DFO':'pittsburgh-penguins','NST':'PIT'},
                    'St. Louis Blues':{'DFO':'St-Louis-Blues','NST':'STL'},
                    'Toronto Maple Leafs':{'DFO':'Toronto-Maple-Leafs','NST':'TOR'},
                    'Vegas Golden Knights':{'DFO':'vegas-golden-knights','NST':'VGK'},
                    'Washington Capitals':{'DFO':'washington-capitals','NST':'WSH'},
                 }

class NST():
    TEAM_PAGE_URL = 'https://www.naturalstattrick.com/linestats.php?fromseason=20192020&thruseason=20192020&stype=2&sit=5v5&score=all&rate=n&team={}&vteam=ALL&view=wowy&loc=B&gpfilt=none&fd=2019-10-02&td=2020-04-04&tgp=2000&strict=incl'
    LINE_PAGE_URL = 'https://www.naturalstattrick.com/linestats.php?fromseason=20192020&thruseason=20192020&stype=2&sit=5v5&score=all&rate=n&team={}&vteam=ALL&view=wowy&loc=B&gpfilt=none&fd=2019-10-02&td=2020-04-04&tgp=2000&strict=incl&p1={}&p2={}&p3={}&p4=0&p5=0'
    PLAYER_ABBREV = 'p1'
    DEFAULT_PLAYER_VAL = 0
    DEFAULT_STATS_HEADERS = ['Player 1', 'Player 2', 'Player 3', 'GP', 'TOI', 'CF', 'CA', 'CF%', 'FF', 'FA', 'FF%', 'SF', 'SA', 'SF%', 'GF', 'GA', 'GF%', 'xGF', 'xGA', 'xGF%', 'SCF', 'SCA', 'SCF%', 'HDCF', 'HDCA', 'HDCF%', 'HDGF', 'HDGA', 'HDGF%', 'MDCF', 'MDCA', 'MDCF%', 'MDGF', 'MDGA', 'MDGF%', 'LDCF', 'LDCA', 'LDCF%', 'LDGF', 'LDGA', 'LDGF%', 'On-Ice SH%', 'On-Ice SV%', 'PDO', 'Off.\xa0Zone Faceoffs', 'Neu.\xa0Zone Faceoffs', 'Def.\xa0Zone Faceoffs', 'Off.\xa0Zone Faceoff %']
    
class DFO():
    '''
    classdocs
    '''
    ROSTER_URL = "https://www.dailyfaceoff.com/teams/{}/line-combinations/"
    FORWARD_ABBREV = "f"
    MAX_LINES = 4
    PLAYER_NAME = "player-name"
        


        
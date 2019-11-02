import requests  
import json  
import pandas as pd

class category:
    Isolation = 'Isolation'
    Transition = 'Transition'
    PRBallHandler = 'PRBallHandler'
    PRRollman = 'PRRollman'
    Postup = 'Postup'
    Spotup = 'Spotup'
    Handoff = 'Handoff'
    Cut = 'Cut'
    OffScreen = 'OffScreen'
    OffRebound = 'OffRebound'
    Misc = 'Misc'
    Default = Isolation
    
class names:
    Offensive = 'offensive'
    Defensive = 'defensive'
    Default = Offensive
    
class seasonType:
    RegularSeason = 'Reg'
    PostSeason = 'Post'
    Default = RegularSeason

class season:
    Current = '2018'
    Default = Current

class limit:
    dlimit = '500'
    Default = dlimit

modifier = ['Isolation', 'Transition', 'PRBallHandler', 'PRRollman', 'Postup', 'Spotup', 'Handoff', 'Cut',
            'OffScreen', 'OffRebound', 'Misc']

BASE_URL = 'https://stats-prod.nba.com/wp-json/statscms/v1/synergy/{endpoint}'

class PlayerPlayTypeStats:
    _endpoint = 'player/'
    def __init__(self, 
                 category = category.Default,
                 names = names.Default,
                 season_type = seasonType.Default,
                 season = season.Default,
                 limit = limit.Default
                 ):

        self.json = requests.get(BASE_URL.format(endpoint=self._endpoint), 
            params={'category': category, 
                    'limit': limit,
                    'names': names,
                    'season': season,
                    'seasonType': season_type
                   })
    
    def totals(self):
        df = pd.DataFrame(self.json.json()['results'])
        
        df.drop(['BetterPPP', 'PlayerFirstName', 'PlayerNumber', 'TeamName', 'TeamNameAbbreviation', 'TeamShortName', 'WorsePPP', 
                 'PlayerLastName', 'FGm', 'FGmG'], axis=1, inplace=True)

        df.rename(columns={'PlayerIDSID' : 'PLAYER_ID', 'Time': 'FREQ', 'P' : 'POSITION', 'FG': 'FG_PCT', 'aFG' : 'EFG_PCT', 'FT' : 'FT_FREQ', 'TO' : 'TO_FREQ', 'SF' : 'SF_FREQ',
                           'Score' : 'SCORE_FREQ', 'PlusOne' : 'AND_ONE_FREQ', 'TeamIDSID' : 'TEAM_ID', 'season' : 'SEASON',
                           'seasonType' : 'SEASON_TYPE', 'name' : 'TYPE', 'Points' : 'PTS', 'Poss' : 'POSS', 'PossG' : 'POSSG'}, inplace=True)

        df_tot = df[['SEASON', 'TEAM_ID', 'PlAYER_ID', 'POSITION', 'GP', 'FREQ', 'POSS', 'PTS', 'PPP', 'FGM', 'FGA', 'FG_PCT', 
                     'EFG_PCT', 'FT_FREQ', 'AND_ONE_FREQ', 'SF_FREQ', 'SCORE_FREQ', 'TO_FREQ', 'TYPE', 'SEASON_TYPE']]
        
        return df_tot
    
    def per_game(self):
        df = pd.DataFrame(self.json.json()['results'])
        
        df.drop(['BetterPPP', 'PlayerFirstName', 'PlayerNumber', 'TeamName', 'TeamNameAbbreviation', 'TeamShortName', 'WorsePPP', 
                 'PlayerLastName', 'FGm', 'FGmG'], axis=1, inplace=True)

        df.rename(columns={'PlayerIDSID' : 'PLAYER_ID', 'P' : 'POSITION', 'Time': 'FREQ', 'FG': 'FG_PCT', 'aFG' : 'EFG_PCT', 'FT' : 'FT_FREQ', 'TO' : 'TO_FREQ', 'SF' : 'SF_FREQ',
                           'Score' : 'SCORE_FREQ', 'PlusOne' : 'AND_ONE_FREQ', 'TeamIDSID' : 'TEAM_ID', 'season' : 'SEASON',
                           'seasonType' : 'SEASON_TYPE', 'name' : 'TYPE', 'Points' : 'PTS', 'Poss' : 'POSS', 'PossG' : 'POSSG'}, inplace=True)
        
        df_pg = df[['SEASON', 'TEAM_ID', 'PLAYER_ID', 'POSITION', 'GP', 'FREQ', 'POSSG', 'PPG', 'PPP', 'FGMG', 'FGAG', 'FG_PCT',
                    'EFG_PCT', 'FT_FREQ', 'AND_ONE_FREQ', 'SF_FREQ', 'SCORE_FREQ', 'TO_FREQ', 'TYPE', 'SEASON_TYPE']]
        
        return df_pg

class TeamPlayTypeStats:
    _endpoint = 'team/'
    def __init__(self, 
                 category = category.Default,
                 names = names.Default,
                 season_type = seasonType.Default,
                 season = season.Default,
                 limit = limit.Default
                 ):

        self.json = requests.get(BASE_URL.format(endpoint=self._endpoint), 
            params={'category': category, 
                    'limit': limit,
                    'names': names,
                    'season': season,
                    'seasonType': season_type
                   })
    
    def totals(self):
        df = pd.DataFrame(self.json.json()['results'])
    
        df.drop(['BetterPPP', 'TeamName', 'TeamNameAbbreviation', 'TeamShortName',
                 'WorsePPP', 'FGm', 'FGmG'], axis=1, inplace=True)

        df.rename(columns={'Time': 'FREQ', 'FG': 'FG_PCT', 'aFG' : 'EFG_PCT', 'FT' : 'FT_FREQ', 'TO' : 'TO_FREQ',
                           'SF' : 'SF_FREQ', 'Score' : 'SCORE_FREQ', 'PlusOne' : 'AND_ONE_FREQ', 'TeamIDSID' : 'TEAM_ID', 
                           'season' : 'SEASON', 'seasonType' : 'SEASON_TYPE', 'name' : 'TYPE', 'Points' : 'PTS',
                           'Poss' : 'POSS', 'PossG' : 'POSSG'}, inplace=True)
        
        df_tot = df[['SEASON', 'TEAM_ID', 'GP', 'FREQ', 'POSS', 'PTS', 'PPP', 'FGM', 'FGA', 'FG_PCT', 'EFG_PCT', 
                     'FT_FREQ', 'AND_ONE_FREQ', 'SF_FREQ', 'SCORE_FREQ', 'TO_FREQ', 'TYPE', 'SEASON_TYPE']]

        return df_tot
    
    def per_game(self):
        df = pd.DataFrame(self.json.json()['results'])
        
        df.drop(['BetterPPP', 'TeamName', 'TeamNameAbbreviation', 'TeamShortName',
                 'WorsePPP', 'FGm', 'FGmG'], axis=1, inplace=True)

        df.rename(columns={'Time': 'FREQ', 'FG': 'FG_PCT', 'aFG' : 'EFG_PCT', 'FT' : 'FT_FREQ', 'TO' : 'TO_FREQ',
                           'SF' : 'SF_FREQ', 'Score' : 'SCORE_FREQ', 'PlusOne' : 'AND_ONE_FREQ', 'TeamIDSID' : 'TEAM_ID', 
                           'season' : 'SEASON', 'seasonType' : 'SEASON_TYPE', 'name' : 'TYPE', 'Points' : 'PTS',
                           'Poss' : 'POSS', 'PossG' : 'POSSG'}, inplace=True)

        df_pg = df[['SEASON', 'TEAM_ID', 'GP', 'FREQ', 'POSSG', 'PPG', 'PPP', 'FGMG', 'FGAG', 'FG_PCT', 'EFG_PCT', 
                    'FT_FREQ', 'AND_ONE_FREQ', 'SF_FREQ', 'SCORE_FREQ', 'TO_FREQ', 'TYPE', 'SEASON_TYPE']]
        
        return df_pg

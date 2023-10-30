import typing

from scrape.team import Team

class FantasyFootballData:
    def __init__(self, teams: list[Team] = []):
        self.teams: list[Team] = teams.sort(key=lambda t: t.wins - t.losses, reverse=True)
        self.matchups: typing.Dict[Team, set[Team]] = {}
        for team in teams:
            self.matchups[team] = set()

    def add_team(self, team: Team):
        self.teams.append(team)
        self.teams.sort(key=lambda t: t.wins - t.losses, reverse=True)
        self.matchups[team] = set()

    def add_matchup(self, team1, team2: Team):
        self.matchups[team1].add(team2)
        self.matchups[team2].add(team1)

    def get_rank(self, team: Team):
        return self.teams.index(team) + 1

    def get_power_rank(self, team: Team):
        teams = self.teams
        teams.sort(key=lambda t: t.points_for, reverse=True)
        return teams.index(team) + 1

    def get_opponents(self, team: Team):
        return self.matchups[team]

    def get_strength_of_schedule(self, team: Team):
        opponents = self.get_opponents(team)
        total = 0.0
        for opp in opponents:
            total += self.get_power_rank(opp)
        return total / len(opponents)

    def get_avg_opponent_points_for(self, team: Team):
        opponents = self.get_opponents(team)
        total = 0.0
        for opp in opponents:
            total += opp.points_for
        return total / len(opponents)

    def get_top_scorer(self):
        teams = self.teams
        teams.sort(key=lambda t: t.points_for, reverse=True)
        return teams[0]

    def get_lowest_scorer(self):
        teams = self.teams
        teams.sort(key=lambda t: t.points_for)
        return teams[0]


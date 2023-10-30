class Team:
    def __init__(self, name: str, wins = 0, losses = 0, points_for: list[float] = []):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.points_for = points_for

class Team:
    def __init__(self, name: str, rank: int, points_for: float):
        self.name = name
        self.rank = rank
        self.points_for = points_for
    def __str__(self):
        return '{rank}: {name}, PF: {points_for}'.format(rank = self.rank, name = self.name, points_for = self.points_for)

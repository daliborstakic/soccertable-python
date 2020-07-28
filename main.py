from prettytable import PrettyTable


# Class Club with two properties
class Club(object):
    def __init__(self, name):
        self.name = name
        self.gs = 0
        self.ga = 0
        self.wi = 0
        self.dr = 0
        self.lo = 0

    @property
    def goalDifference(self):
        return self.gs - self.ga

    @property
    def points(self):
        return self.wi * 3 + self.dr


# Printing the table using the PrettyTable module
def print_table():
    t = PrettyTable(['Pos.', 'Name', 'W', 'D', 'L', 'GS', 'GA', 'GD', 'P'])

    for club in clubs:
        t.add_row([clubs.index(club) + 1, club.name, club.wi, club.dr, club.lo, club.gs, club.ga, club.goalDifference,
                   club.points])

    print(t)


# Empty club list
clubs = []

# Entering club names
for i in range(1, 5):
    name = input('Enter the name of the {}. club: '.format(i))
    clubs.append(Club(name))

print_table()

results = []

# Entering results
for club in clubs:
    for i in range(4):
        if club.name != clubs[i].name:
            final_result = input('{} : {} '.format(club.name, clubs[i].name))
            results.append((club.name, clubs[i].name, final_result))

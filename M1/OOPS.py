class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __getitem__(self, item):
        return self.players[item]

    def __len__(self):
        return len(self.players)

    def __repr__(self):
        return f"\n Club {self.name} : {self.players} "

    def __str__(self):
        return f"\n Club {self.name} has {len(self)} players "

my_club = Club('LiverPool')
my_club.players.append('user')
print(my_club[0])
print(my_club)
my_club[0]
my_club
# Transfer Market Simulator - Diego Salcedo T.
# "台上三分钟，台下十年功"

class Team:
  def __init__(self, name, budget, country, city, league):
    self.name = name
    self.budget = budget
    self.country = country
    self.city = city
    self.league = league
    self.players = {}

  def __repr__(self):
    return f"^^^^^^^^^^^^^^^^^^^^\n Team: {self.name}\n    Country: {self.country}\n Budget: ${self.budget}\n     City: {self.city}\n^^^^^^^^^^^^^^^^^^^^"

  def change_league(self, new_league):
    self.league = new_league

  def Modify_budget(self, new_budget):
    self.budget = new_budget

  def Add_player(self, new_player):
    self.players[new_player.get_name()] = new_player

  def get_players(self):
      return list(self.players.keys())

  def get_players_cards(self):
    return list(self.players.values())
  
  def transfer_player(self, player, other_team):
    other_team.players[player.get_name()] = self.players.pop(player.get_name())
    self.budget += player.get_value()
    other_team.budget -= player.get_value()

  def get_name(self):
    return self.name

#Player_1 = Player(Player_1_name, Player_1_stats, Player_1_nationality, Player_1_position)

#print(Player_1)

class Player:
    def __init__(self, name, nationality, stats, position, age, value, foot = 'right'):
      self.name = name
      self.nationality = nationality
      self.stats = stats
      self.position = position
      self.foot = foot
      self.age = age
      self.value = value

    def __repr__(self):
      return f"--------------------\n Name: {self.name}\n      Age: {self.age}\n  Nationality: {self.nationality}\n    Position: {self.position}\n     Global: {self.stats.get('GLB')}\n PAC: {self.stats.get('PAC')} - DRI: {self.stats.get('DRI')}\n SHO: {self.stats.get('SHO')} - DEF: {self.stats.get('DEF')}\n PAS: {self.stats.get('PAS')} - PHY: {self.stats.get('PHY')}\n--------------------"

    def update_stats(self, new_stats):
        self.stats = new_stats

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def update_position(self, new_position):
        self.stats = new_position

# Instantiation of players:
Leo = Player("Leo Messi", "ARG", {"GLB": 93, "PAC": 85, "SHO": 92, "PAS": 91, "DRI": 95, "DEF": 34, "PHY": 65}, "RW", 36, 60000000)
Neymar = Player('Neymar Jr', 'BRA', {"GLB": 91, "PAC": 91, "SHO": 83, "PAS": 86, "DRI": 94, "DEF": 37, "PHY": 63}, 'LW', 31, 35000000)
Mbappe = Player('Kylian Mbappé', 'FRA', {"GLB": 91, "PAC": 97, "SHO": 89, "PAS": 80, "DRI": 92, "DEF": 36, "PHY": 76}, 'ST', 24, 180000000)
Donnarumma = Player('Gianluigi Donnarumma', 'ITA', {"GLB": 87, "PAC": 90, "SHO": 83, "PAS": 79, "DRI": 89, "DEF": 52, "PHY": 85}, 'GK', 24, 45000000)
Marquinhos = Player('Marcos Aoás Corrêa', 'BRA', {"GLB": 87, "PAC": 79, "SHO": 56, "PAS": 75, "DRI": 74, "DEF": 89, "PHY": 80}, 'CB', 29, 65000000)
Marco_Asensio = Player('Marco Asensio Willemsen', 'SPA', {"GLB": 83, "PAC": 82, "SHO": 80, "PAS": 81, "DRI": 83, "DEF": 43, "PHY": 62}, 'RW', 27, 25000000)
Cristiano_Ronaldo = Player(' Cristiano Ronaldo', 'POR', {"GLB": 87, "PAC": 81, "SHO": 92, "PAS": 78, "DRI": 85, "DEF": 34, "PHY": 75}, 'ST', 38, 15000000)

# Instantiation of teams:
Inter_Miami = Team('Inter Miami', 225000000, 'USA', 'Miami', 'MLS')
PSG = Team('Paris Saint-Germain', 600000000, 'FRA', 'Paris', 'Ligue 1')
Al_Nassr = Team('Al Nassr', 195500000, 'KSA', 'Riyadh', 'Pro League')

# Teams' initial card
#print(Inter_Miami)
#print(PSG)

# simulation of Transfer Market
Inter_Miami.Add_player(Leo)
Inter_Miami.Add_player(Neymar)
Inter_Miami.Add_player(Cristiano_Ronaldo)
PSG.Add_player(Mbappe)
PSG.Add_player(Donnarumma)
PSG.Add_player(Marquinhos)
PSG.Add_player(Marco_Asensio)
Inter_Miami.transfer_player(Neymar, PSG)
Inter_Miami.transfer_player(Cristiano_Ronaldo, Al_Nassr)

# Teams' squads
#print(Inter_Miami.get_name(), '-', Inter_Miami.get_players())
#print(PSG.get_name(), '-', PSG.get_players())

# Teams' updated cards
#print(Inter_Miami)
#print(PSG)

print(Al_Nassr)
print(Cristiano_Ronaldo)
print(Leo)
for player in PSG.get_players_cards():
  print(player)

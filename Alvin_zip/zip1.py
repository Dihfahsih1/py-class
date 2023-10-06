try:
    def players_and_shirtnumbers():
        shirt = [9, 11, 8, 7]
        players = ["Halland", "Neymar", "Bruno", "Cristiano"]
        player_shirt = zip(players, shirt)
        print(list(player_shirt))
    players_and_shirtnumbers()
except :
    print()
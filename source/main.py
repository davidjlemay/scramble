from source.components import Game, Player



player_ids = [1, 2, 3, 4]
players = [Player(x) for x in player_ids]
game = Game(players)


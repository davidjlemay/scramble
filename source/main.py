from source.components.components import Game, Player
from itertools import permutations


player_ids = [1, 2, 3, 4]
players = [Player() for x in player_ids]
game = Game(players)


def play_word(tiles_squares: dict):
    points = 0
    for tile, square in tiles_squares:
        if not game.board.grid.square.played:
            game.board.grid[square.row][square.col].square.set_value(tile)
            points += tile.value*square.value
            return points
        else:
            return 'Invalid move.'


def find_words(tiles: list):
    perms = permutations(tiles)
    words = []
    for perm in perms:
        if game.dictionary.has_subtrie(perm):
            words.append(perm)
    return words

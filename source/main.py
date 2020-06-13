from source.components.components import Game, Player
from itertools import permutations
import re
import numpy as np


player_ids = [1, 2, 3, 4]
players = [Player(x) for x in player_ids]
game = Game(players)


def play_word(tiles_squares: list):
    points = 0
    for x in tiles_squares:
        tile = x.tile
        row, col = x.square.split()
        square = game.board.grid[row][col].square
        if not square.played:
            square.set_value(tile)
            points += tile.value*square.value
            return points
        else:
            return 'Invalid move.'


def find_words(tiles: list):
    perms = permutations(tiles)
    words = []
    for perm in perms:
        if game.dictionary.has_subtrie(perm):
            words.append(''.join(perm))
    return words


def scan_board(words):
    matches = []
    board = make_board(np.array(game.board.grid))
    for pattern in board:
        for word in words:
            match = re.search(pattern, word)
            if match is not None:
                matches.append({'match': match, 'pattern': pattern})
    return regex_to_tiles(matches)


def regex_to_tiles(matches: list):
    match_tiles_list = []
    for match in matches:
        match_tiles = []
        pattern_tiles = []
        for letter in match['match']:
            for tile in Game.tiles:
                if tile.letter == letter:
                    match_tiles.append(tile)
            pattern_tiles.append(match['pattern'].index(letter))
        match_tiles_list.append({'match_tiles': match_tiles, 'pattern': pattern_tiles})
    return match_tiles_list


def make_board(grid: np.array):
    board = []
    for row in grid[0, :]:
        board.append(re.compile(regex_compile(row)))
    for col in grid[:, 0]:
        board.append(re.compile(regex_compile(col.T)))
    return board


def regex_compile(row: list):
    pattern = r''
    for square in row:
        if not game.board.grid[row][square].square.played:
            pattern += r'[\w\s]'
        else:
            pattern += game.board.grid.square.tile.letter
    return pattern


def match_high_score(matches: list):
    match_scores = []
    for match in matches:
        score = 0
        for tile in match['match']:
            index = 0
            square_value = match['pattern'][index].value
            score += square_value*tile.letter.value
            index += 1
        match_scores.append({'match': match, 'score': score})
    return match_scores


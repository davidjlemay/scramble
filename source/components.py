from random import randrange

from source.constructors import DictionaryConstructor, TilesConstructor
from source.parameters import *

from itertools import combinations
import re
import numpy as np


class User:
    def __init__(self, name: str, username: str, password: str):
        self.name = name
        self._id = create_id()
        self.username = username
        self.password = password

    #        self.stats = Stats()

    def get_name(self) -> str:
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id(self) -> str:
        return self._id

    def set_id(self, player_id):
        self._id = player_id

    def get_username(self) -> str:
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self) -> str:
        return self.password

    def set_password(self, password):
        self.password = password

    def get_stats(self) -> object:
        return self.stats

    def update_stats(self, Game):
        self.stats.update(Game)


class Stats:
    def __init__(self, user_id: str):
        self._id = user_id
        self.games_played = 0
        self.wins = 0
        self.elo = 0
        self.history = []

    def get_elo(self):
        return self.elo

    def get_games_played(self):
        return self.games_played

    def get_history(self) -> object:
        return self.history

    def update(self, game: object):
        self.history.append(game)
        self.games_played += 1
        if Game.winner == self._id:
            self.wins += 1
        self.elo = self.wins / self.games_played


class Player:
    def __init__(self, user: object):
        self.username = user.username
        self.rack = []
        self.score = 0
        self.moves = []
        self.words = []
        self.matches = []

    def get_score(self):
        return self.score

    def set_score(self, points):
        self.score += points

    def get_rack(self):
        return self.rack

    def add_tiles(self, tiles: list):
        for tile in tiles:
            self.rack.append(tile)

    def remove_tile(self, tile: object):
        self.rack.remove(tile)

    def remove_tiles(self, rack: list):
        for tile in rack:
            self.rack.remove(tile)

    def place_tile(self, i, j: int, placed_tile: object, game: object):
        try:
            game.add_tile(placed_tile)
        except:
            pass
        self.remove_tile(placed_tile)

    def play_word(tiles_squares: list):
        points = 0
        for x in tiles_squares:
            tile = x.tile
            row, col = x.square.split()
            square = Game.board.grid[row][col].square
            if not square.played:
                square.set_value(tile)
                points += tile.value * square.value
                return points
            else:
                return 'Invalid move.'

    def find_words(self, game: object):
        letters = [tile.letter for tile in self.rack]
        combs = [combinations(letters, n) for n in range(len(letters))]
        flat_combs = [item for sublist in combs for item in sublist]
        words = []
        for comb in flat_combs:
            word = ''.join(comb)
            if game.dictionary.dictionary.has_subtrie(word):
                words.append(word)
        self.words = words

    def scan_board(self):
        matches = []
        board = make_board(np.array(Game.board.grid))
        for pattern in board:
            for word in self.words:
                match = re.search(regex_compile(pattern), word)
                if match is not None:
                    matches.append(
                        {'match': regex_to_tiles(match.group(0)), 'pattern': pattern, 'x': board.index(pattern)})
        self.matches = matches


class Game:
    def __init__(self, players: list):
        self.players = [Player(x) for x in players]
        self.board = Board()
        self.dictionary = Dictionary()
        self.tiles = Tiles()
        self.complete = False
        self.winner = ''

    def verify_word(self, word: str):
        if word in self.dictionary.keys():
            return True
        else:
            return False

    def get_winner(self):
        if self.complete:
            return max(self.players, key=lambda player: player.score)
        return None

    def take_tiles(self, number_of_tiles: int):
        items = []
        for i in range(number_of_tiles):
            items.append(self.tiles.pop())
        return items

    def add_tile(self, i, j, placed_tile: object):
        if not self.board.grid[i][j].tile.letter:
            self.board.grid[i][j].tile = placed_tile

    def remove_tile(self, i, j, placed_tile: object):
        if self.board.grid[i][j].tile.letter is placed_tile:
            self.board.grid[i][j].tile = ''


class Board:
    def __init__(self):
        self.size = BOARD_SIZE
        self.grid = [[Square()] * BOARD_SIZE for _ in range(BOARD_SIZE)]


class Square:
    def __init__(self):
        self.value = 1
        self.played = False
        self.tile = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_tile(self):
        return self.tile

    def set_tile(self, tile: object):
        self.tile = tile
        self.played = True


class Tiles:
    def __init__(self):
        self.set = TilesConstructor().tiles_factory()

    def pop(self):
        return self.set.pop()


class Dictionary:
    def __init__(self):
        self.language = LANGUAGE
        self.dictionary = DictionaryConstructor().dictionary_factory()


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
        if not Game.board.grid[row][square].square.played:
            pattern += r'[\w\s]'
        else:
            pattern += Game.board.grid.square.tile.letter
    return pattern


def match_scores(matches: list):
    scores = []
    for match in matches:
        score = 0
        for tile in match['match']:
            index = 0
            square_value = match['pattern'][index].value
            score += square_value * tile.letter.value
            index += 1
        scores.append({'match': match, 'score': score})
    return scores


def create_id():
    return str(randrange(100))

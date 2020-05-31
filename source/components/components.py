from source.constructors.constructors import DictionaryConstructor, TilesConstructor
from source import parameters


class User:
    def __init__(self, name: str, username: str, password: str):
        self.name = name
        self._id = ''
        self.username = username
        self.password = password
        self.stats = Stats()

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

    def update_stats(self, game):
        self.stats.update(game)


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
        if game.winner == self._id:
            self.wins += 1
        self.elo = self.wins/self.games_played


class Player:
    def __init__(self, user_id: str):
        self._id = user_id
        self.tiles = []
        self.score = 0
        self.moves = []

    def get_score(self):
        return self.score

    def set_score(self, points):
        self.score += points

    def get_tiles(self):
        return self.tiles

    def add_tiles(self, tiles: list):
        for tile in tiles:
            self.tiles.append(tile)

    def remove_tiles(self, tiles: list):
        for tile in tiles:
            self.tiles.remove(tile)


class Game:
    def __init__(self, players: list):
        self.players = players
        self.board = Board()
        self.dictionary = Dictionary()
        self.tiles = Tiles()
        self.complete = False
        self.winner = ''

    def verify_word(self, word: str):
        if word in self.dictionary:
            return True
        else:
            return False

    def get_winner(self):
        if self.complete:
            return max(self.players, key=lambda player: player.score)
        else:
            return 'Game not over.'

    def take_tiles(self, number_of_tiles: int):
        tiles = []
        for tile in range(number_of_tiles):
            tiles.append(self.tiles.pop())
        return tiles


class Board:
    def __init__(self):
        self.size = parameters.BOARD_SIZE
        self.grid = Grid()


class Grid:
    def __init__(self):
        self.grid = [[Square()] * parameters.BOARD_SIZE for _ in range(parameters.BOARD_SIZE)]


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
        self.set = TilesConstructor()


class Tile:
    def __init__(self, letter: str, value: int):
        self.letter = letter
        self.value = value

    def get_letter(self):
        return self.letter

    def get_value(self):
        return self.value


class Dictionary:
    def __init__(self):
        self.language = parameters.LANGUAGE
        self.dictionary = DictionaryConstructor()










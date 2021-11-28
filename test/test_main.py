from source.components import *

user = User('david', 'azeroth', 'qwerty')
# computer = Computer()
game = Game([user])
game.players[0].add_tiles(game.take_tiles(7))


def test_add_user():
    assert game.players[0].username == 'azeroth'


def test_add_tiles():
    assert len(game.players[0].rack) == 7


def test_return_tile():
    game.players[0].place_tile(8, 6, game.players[0].rack[0], game)
    assert game.board.grid[8][6].tile is not None
    assert len(game.players[0].rack) == 6
    game.players[0].return_tile(8, 6, game)
    assert game.board.grid[8][6].tile is None
    assert len(game.players[0].rack) == 7


def test_play_word():
    game.players[0].rack = [Tile('V', 4), Tile('E', 1), Tile('S', 1), Tile('T', 1), Tile('E', 1), Tile('D', 2),
                            Tile('A', 1)]
    game.players[0].place_tile(8, 5, game.players[0].rack[0], game)
    game.players[0].place_tile(8, 6, game.players[0].rack[0], game)
    game.players[0].place_tile(8, 7, game.players[0].rack[0], game)
    game.players[0].place_tile(8, 8, game.players[0].rack[0], game)
    game.players[0].place_tile(8, 9, game.players[0].rack[0], game)
    game.players[0].place_tile(8, 10, game.players[0].rack[0], game)

    word = ''
    for x in game.board.grid[8]:
        if x.tile is not None:
            word += x.tile.letter
    assert word == 'VESTED'

    game.players[0].play_word(game)
    assert game.players[0].score == 10
    for x in game.board.grid[8]:
        if x.tile is not None:
            assert x.played is True

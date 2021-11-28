import random
import csv
import pygtrie
from source.parameters import *
from typing import NamedTuple


class DictionaryConstructor:
    def dictionary_factory(self):
        if DICTIONARY_TYPE == 'list':
            return self.ordered_list()
        else:
            return self.trie()

    @staticmethod
    def ordered_list():
        return sorted([line for line in open(LANGUAGE_ROOT_PATH + LANGUAGE + '-words-collins-2019.txt')])

    @staticmethod
    def trie():
        trie = pygtrie.CharTrie()
        for word in DictionaryConstructor.ordered_list():
            trie[word] = True
        return trie


class TilesConstructor:
    def tiles_factory(self):
        return self.frequency()

    @staticmethod
    def frequency():
        with open(LANGUAGE_ROOT_PATH + LANGUAGE + '-tile-distribution.csv') as f:
            frequency = [list(line) for line in csv.reader(f)]
            tiles = []

            class Tile(NamedTuple):
                letter: str
                value: int

            for x in frequency:
                for y in range(int(x[1])):
                    tiles.append(Tile(str(x[0]), int(x[2])))
            return random.sample(tiles, k=len(tiles))

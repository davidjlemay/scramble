import random
import csv
import pygtrie
from source import parameters


class DictionaryConstructor:
    def __init__(self):
        self.type = parameters.DICTIONARY_TYPE
        self.dictionary = self.dictionary_factory()

    def dictionary_factory(self):
        if self.type == 'list':
            return self.ordered_list()
        else:
            return self.trie()

    @staticmethod
    def ordered_list():
        return sorted([line for line in open(parameters.LANGUAGE_ROOT_PATH+parameters.LANGUAGE+'-words-collins-2019.txt')])

    @staticmethod
    def trie():
        trie = pygtrie.CharTrie()
        for word in DictionaryConstructor.ordered_list():
            trie[word] = True
        return trie


class TilesConstructor:
    def __init__(self):
        pass

    @staticmethod
    def frequency():
        with open(parameters.LANGUAGE_ROOT_PATH+parameters.LANGUAGE+'-tile-distribution.csv') as f:
            frequency = [list(line) for line in csv.reader(f)]
            distribution = [[x[0]] * int(x[1]) for x in frequency]
            flat_list = [item for sublist in distribution for item in sublist]
            flat_tuples_list = []
            for x in flat_list:
                for y in frequency:
                    if x == y:
                        flat_tuples_list.append({'name': x, 'value': y[2]})
            return random.sample(flat_tuples_list, k=len(flat_tuples_list))


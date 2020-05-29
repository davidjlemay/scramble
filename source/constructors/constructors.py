import random
import csv

class DictionaryConstructor:
    def __init__(self):
        pass

    @staticmethod
    def from_resources(language: str):
        return list(open('resources/languages/'+language+'-words-collins-2019.txt'))


class TilesConstructor:
    def __init__(self):
        pass

    @staticmethod
    def frequency(language: str):
        with open('resources/languages/'+language+'-tile-distribution.csv') as f:
            frequency = [list(line) for line in csv.reader(f)]
            distribution = [[x[0]] * int(x[1]) for x in frequency]
            flat_list = [item for sublist in distribution for item in sublist]
            return random.sample(flat_list, k=len(flat_list))


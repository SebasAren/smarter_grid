from hill_climber import HillClimber
from data_structure import House, Battery, read_csv
import copy

class Propagation(object):
    """

    """

    def __init__(self, houses, batteries, climbers=2):
        self.climber_list = [HillClimber(houses, batteries) for i in range(climbers)]
        self.best = None
        self.best_value = 0

    def climbing(self):
        for i, climber in enumerate(self.climber_list):
            climber.climbing()
            print('Current iteration: {} of {}.\nValue: {}.'.format(i + 1, len(self.climber_list), climber.current_value))

    def find_best(self):
        for i, climber in enumerate(self.climber_list):
            if climber < self.best:
                self.best = climber
        self.best = copy.copy(self.best)
        return self.best.current_value

    def create_variance(self, amount):
        if not self.best:
            raise AttributeError

        for i in range(amount):
            swap = self.best.pick_swap()
            self.best.swap_houses(swap[0], swap[1], swap[2], swap[3])

    def short_sequence(self, iterations, variations=2):
        self.climbing()
        for i in range(iterations):
            print(self.find_best())
            self.create_variance(variations)
            if self.best.loose_climbing():
                print('HOLY SHIT')
                self.best.climbing()
            self.climber_list.append(self.best)

if __name__ == '__main__':

    CSV_HOUSES = 'data/wijk1_huizen.csv'
    CSV_BATTERIES = 'data/wijk1_batterijen.csv'

    houses = read_csv(CSV_HOUSES, house=True)
    batteries = read_csv(CSV_BATTERIES)

    test = Propagation(houses, batteries, climbers=2)
    test.short_sequence(10)
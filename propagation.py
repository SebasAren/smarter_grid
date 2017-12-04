from hill_climber import HillClimber
from data_structure import House, Battery, read_csv
import copy

class Propagation(object):
    """

    """

    def __init__(self, houses, batteries, climbers=2):
        self.climber_list = [HillClimber(houses, batteries) for i in range(climbers)]
        self.best = None

    def climbing(self):
        for i, climber in enumerate(self.climber_list):
            climber.climbing()
            print('Current iteration: {} of {}.\nValue: {}.'.format(i + 1, len(self.climber_list), climber.current_value))

    def find_best(self):
        for climber in self.climber_list:
            if not self.best:
                self.best = copy.copy(climber)
            elif climber < self.best:
                self.best = copy.copy(climber)
        return self.best.current_value

    def create_variance(self, amount=1):
        if not self.best:
            raise AttributeError

        swap = self.best.pick_swap()
        for i in range(amount):
            self.best.swap_houses(swap[0], swap[1], swap[2], swap[3])

    def climb_best(self):
        return self.best.climbing()


    def short_sequence(self):
        self.climbing()
        self.find_best()
        self.create_variance()
        print(self.climb_best())

if __name__ == '__main__':

    CSV_HOUSES = 'data/wijk1_huizen.csv'
    CSV_BATTERIES = 'data/wijk1_batterijen.csv'

    houses = read_csv(CSV_HOUSES, house=True)
    batteries = read_csv(CSV_BATTERIES)

    test = Propagation(houses, batteries)
    test.short_sequence()
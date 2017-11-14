# main.py

from data_structure import Battery, House, read_csv
from itertools import combinations, chain
import data_generator

WIDTH = 1
HEIGHT = 2

def add(a,p,i):
    #adds a to the ith cell of partition p
    #returns a new partiton
    return [piece + [a] if j == i else piece for j, piece in enumerate(p)]

def addToAll(a,p):
    #adds a to all pieces of p
    #returns a list of partitions
    return [add(a,p,i) for i in range(len(p))]

def partition(n,k):
    memoDict = {}
    def helperPart(n,k):
        if n == 0 and k == 0: return [[]]
        elif n == 0 or k == 0: return []
        elif (n,k) in memoDict:
            return memoDict[(n,k)]
        else:
            kParts = helperPart(n-1,k)
            kMinusParts = helperPart(n-1,k-1)
            parts = [part + [[n]] for part in kMinusParts]
            for p in kParts:
                parts.extend(addToAll(n,p))
            memoDict[(n,k)] = parts
            return parts
    return helperPart(n,k)

def brute_force_solution(houses, batteries):
    cost = 0
    best_cost = 0
    data = []
    for i, row in enumerate(partition(len(houses), len(batteries))):
        data = [[] for i in range(len(row))]
        for j, el in enumerate(row):
            for k, house_num in enumerate(el):
                data[j].append(houses[house_num - 1])

        # actual check goes here!!!!
        try:
            print(data)
            for i, row_2 in enumerate(data):


                # try to check if contstraint has been violated
                for house in row_2:
                    price = batteries[i].c_house(house)
                    if not price:
                        for battery in batteries:
                            battery.clear()
                        raise TypeError
                    cost += price
            if cost < best_cost:
                for battery in batteries:
                    battery.clear()
                raise TypeError

            else:
                best_cost = cost
                best_data = data

        except TypeError:
                continue

    return [best_data, best_cost]

    # for el in [x for l in range(1, len(houses) + 1) for x in combinations(houses, l)]:

if __name__ == '__main__':
    import sys

    # create a list of houses
    with open('data/test_wijk/{}_huizen.csv'.format(sys.argv[1])) as f:
        houses = read_csv(f, house=True)

    # and batteries
    with open('data/test_wijk/{}_batterijen.csv'.format(sys.argv[1])) as f:
        batteries = read_csv(f)

    print(brute_force_solution(houses, batteries))
    print(batteries)
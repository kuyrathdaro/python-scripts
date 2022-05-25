from random import randint
from timeit import repeat

LIST_LENGTH = 10000

def run_sorting_algorithm(algorithm, list):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""
    
    stmt = f"{algorithm}({list})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

def main():
    list = [randint(0, 1000) for i in range(len(LIST_LENGTH))]
    run_sorting_algorithm(algorithm="sorted", list=list)

if __name__ == "__main__":
    main()
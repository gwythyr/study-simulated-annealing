import math
import random
from test_cases import small, large, cities


def init_random_path(length: int) -> [int]:
    points = list(range(1, length))
    random.shuffle(points)
    return [0] + points + [0]


def calculate_path_length(matrix: [[int]], path: [int]) -> int:
    path_length = 0
    for index in range(len(path) - 2):
        path_length += matrix[path[index]][path[index + 1]]
    return path_length


def find_best_path(matrix: [[int]]):
    path = init_random_path(len(matrix))
    path_length = calculate_path_length(matrix, path)
    no_improvement_counter = 0
    steps = 0
    while no_improvement_counter < len(matrix) ** 2:
        steps += 1
        random_point1 = random.randint(1, len(matrix) - 2)
        random_point2 = random.randint(random_point1 + 1, len(matrix) - 1)
        new_path = path.copy()
        new_path[random_point1], new_path[random_point2] = path[random_point2], path[random_point1]
        new_path_length = calculate_path_length(matrix, new_path)
        delta = path_length - new_path_length
        if delta > 0 or math.exp(-delta/steps) < random.random():
            path = new_path
            path_length = new_path_length
            no_improvement_counter = 0
        else:
            no_improvement_counter += 1
    return path, path_length, steps


def print_hi(name):
    for case in (small, large):
        path, path_length, steps = find_best_path(case)
        cities_path = list(map(lambda point: cities[point], path))
        print(f"Кількість міст - {len(case)}")
        print(f"Довжина маршруту: {path_length} км. Кількість ітерацій: {steps}. Маршрут: {'->'.join(cities_path)}")
        print()


if __name__ == '__main__':
    print_hi('PyCharm')

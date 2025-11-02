from itertools import combinations
from functools import lru_cache

def count_pairs_value(array):
    return sum(x * (x - 1) for x in array)  # Combination formula: xC2 = x * (x - 1)

def hand_points_value(array):
    return array[0] + 10 * sum(array[10:13])

@lru_cache(None)
def possible_hands(array):
    total = 1
    for x in array:
        total *= {0: 1, 1: 4, 2: 6, 3: 4}[x] if x <= 3 else 1
    return total

def count_runs_value(array):
    points = 0
    run_size = 0
    for i in range(13):
        if array[i] > 0:
            run_size += 1
        else:
            if run_size >= 3:
                points += sum(array[i - run_size:i])  # Count cards in the run
            run_size = 0
    if run_size >= 3:
        points += sum(array[-run_size:])
    return points

@lru_cache(None)
def count_fifteens(array):
    card_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    indices = [i for i in range(13) if array[i] > 0]
    points = 0
    for r in range(2, len(indices) + 1):
        for combo in combinations(indices, r):
            total = sum(card_values[i] * array[i] for i in combo)
            if total == 15:
                points += 2
    return points

def calculate_hands():
    hands_counter = 0
    total_combinations = 5**13

    for number in range(total_combinations):
        array = [(number // (5 ** i)) % 5 for i in range(13)]
        hand_points = hand_points_value(array)

        # Short-circuiting Cribbage points calculation
        cribbage_points = 0

        # Add pairs points
        cribbage_points += count_pairs_value(array)
        if cribbage_points > hand_points:
            continue

        # Add runs points
        cribbage_points += count_runs_value(array)
        if cribbage_points > hand_points:
            continue

        # Add fifteens points
        cribbage_points += count_fifteens(tuple(array))
        if cribbage_points > hand_points:
            continue

        # If points match, count possible hands
        if hand_points == cribbage_points:
            hands_counter += possible_hands(tuple(array))

        if number % (total_combinations // 100) == 0:
            print(f"Progress: {number / total_combinations:.2%}")

    return hands_counter

# Run the calculation
result = calculate_hands()
print(f"Total hands where hand points match Cribbage points: {result}")
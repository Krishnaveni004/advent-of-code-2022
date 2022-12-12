def calculate_priority(value):
    if value.islower():
        return ord(value) - ord('a') + 1
    return ord(value) - 38


if __name__ == '__main__':
    score = 0

    with open('input.txt', 'r') as puzzle_input:
        rucksacks = puzzle_input.readlines()
        for rucksack in rucksacks:
            compartment = set()

            length = len(rucksack)
            partition = length // 2
            for a in rucksack[:partition]:
                compartment.add(a)

            for a in rucksack[partition:]:
                if a in compartment:
                    score += calculate_priority(a)
                    break

    print(score)

max_quantity = 0

with open('input.txt', 'r') as puzzle_input:
    readable = puzzle_input.read()
    elf_quantities = readable.split('\n\n')
    for quantity in elf_quantities:
        max_quantity = max(max_quantity, sum(map(int, quantity.split('\n'))))

print(max_quantity)

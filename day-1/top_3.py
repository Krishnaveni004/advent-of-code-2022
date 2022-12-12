from heapq import heappush, heappop, heapify


class Heap:
    def __init__(self):
        self.data = []
        self.size = 0
        heapify(self.data)

    def push(self, ele):
        heappush(self.data, ele)
        self.size += 1

    def pop(self):
        heappop(self.data)
        self.size -= 1

    def __repr__(self):
        return str(self.data)


if __name__ == '__main__':

    quantities = Heap()

    with open('input.txt', 'r') as puzzle_input:
        readable = puzzle_input.read()
        elf_quantities = readable.split('\n\n')
        for quantity in elf_quantities:
            total = sum(map(int, quantity.split('\n')))
            quantities.push(total)

            if quantities.size > 3:
                quantities.pop()

    print(sum(quantities.data))

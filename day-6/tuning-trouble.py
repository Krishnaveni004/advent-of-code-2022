MARKER = 14

with open('input.txt', 'r') as puzzle_input:
    readable = puzzle_input.read()

    count = p1 = 0
    hashmap = set()

    for index, char in enumerate(readable):

        if count == MARKER:
            print(index)
            break

        if char in hashmap:
            while p1 < index:
                hashmap.remove(readable[p1])
                count -= 1

                if readable[p1] == char:
                    p1 += 1
                    break
                p1 += 1

        hashmap.add(char)
        count += 1

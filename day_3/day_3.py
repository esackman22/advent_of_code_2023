schematic = []
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
with open('day_3_input.csv') as f:
    for line in f:
        schematic.append(line.strip())

seen = set()
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
rows, cols = len(schematic), len(schematic[0])


def search_for_adjacent_symbol(row, col):
    for x, y in directions:
        if 0 <= row+x < rows and 0 <= col+y < cols:
            if schematic[row+x][col+y] not in nums and schematic[row+x][col+y] != '.':
                return True

    return False


total = 0

for row in schematic:
    print(row)

for row in range(rows):
    for col in range(cols):
        if (row, col) in seen:
            continue

        seen.add((row, col))
        symbol_adjacent = False
        cur = ''
        c = col
        while c < cols and schematic[row][c] in nums:
            seen.add((row, c))
            cur += schematic[row][c]
            if not symbol_adjacent:
                symbol_adjacent = search_for_adjacent_symbol(row, c)

            c += 1

        if cur and symbol_adjacent:
            total += int(cur)

print('Part I Total: ', total)

# Part II
visited = set()


def build_number(row, col):
    num = schematic[row][col]
    visited.add((row, col))
    # Build Left
    c = col - 1
    while c >= 0 and schematic[row][c] in nums:
        num += schematic[row][c]
        visited.add((row, c))
        c -= 1

    num = num[::-1]

    c = col + 1
    while c < cols and schematic[row][c] in nums:
        num += schematic[row][c]
        visited.add((row, c))
        c += 1

    return int(num)


def find_gear_ratio(row, col):
    num1, num2 = 0, 0
    for x, y in directions:
        if 0 <= row+x < rows and 0 <= col+y < cols:
            if (row+x, col+y) not in visited and schematic[row+x][col+y] in nums:
                if num1 == 0:
                    num1 = build_number(row+x, col+y)
                else:
                    num2 = build_number(row+x, col+y)
                    break

    return num1 * num2

gear_ratio_total = 0
for row in range(rows):
    for col in range(cols):
        if schematic[row][col] == '*':
            gear_ratio_total += find_gear_ratio(row, col)

print('Part II Total: ', gear_ratio_total)


# Part I
total = 0
with open('day_1_input.csv') as f:
    for line in f:
        num = ''
        for char in line:
            if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                num += char
                break

        for char in line[::-1]:
            if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                num += char
                break

        total += int(num)

print(total)

# Part II
# Numbers could be substrings of the larger string
# Implement a trie structure - at each character, if it's not a number, check for the substring of a digit
# Do a forwards trie and backwards trie


class TrieNode:

    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def __str__(self):
        words = []
        for child in self.root.children:
            words.append(child)

        return str(words)

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = TrieNode()
                curr = curr.children[char]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True

forwards_digits = Trie()
backwards_digits = Trie()

digits = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

for digit in digits:
    forwards_digits.insert(digit)
    backwards_digits.insert(reversed(digit))

new_total = 0
new_nums = []
with open('day_1_input.csv') as f:
    for line in f:
        num = ''
        for i in range(0, len(line)):
            if line[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                num += line[i]
                break
            else:
                j = i
                potential_num = line[j]
                real_num = ''
                while forwards_digits.startsWith(potential_num):
                    if forwards_digits.search(potential_num):
                        real_num = potential_num
                        break

                    j += 1
                    potential_num += line[j]

                if real_num:
                    num += digits[real_num]
                    break

        for i in range(len(line)-1, -1, -1):
            if line[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                num += line[i]
                break
            else:
                j = i
                potential_num = line[j]
                real_num = ''
                while backwards_digits.startsWith(potential_num):
                    if backwards_digits.search(potential_num):
                        real_num = potential_num
                        break

                    j -= 1
                    potential_num += line[j]

                if real_num:
                    real_num = real_num[::-1]
                    num += digits[real_num]
                    break

        new_total += int(num)
        new_nums.append((line, num))

print(new_total)

new_new_total = 0
new_new_nums = []
with open('day_1_input.csv') as f:
    for line in f:
        num = ''
        newline = line\
            .replace('one', 'one1one')\
            .replace('two', 'two2two')\
            .replace('three', 'three3three')\
            .replace('four', 'four4four')\
            .replace('five', 'five5five')\
            .replace('six', 'six6six')\
            .replace('seven', 'seven7seven')\
            .replace('eight', 'eight8eight')\
            .replace('nine', 'nine9nine')

        for char in newline:
            if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                num += char
                break

        for char in newline[::-1]:
            if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                num += char
                break

        new_new_total += int(num)
        new_new_nums.append(num)

print(new_new_total)

for i in range(len(new_nums)):
    line, new_num = new_nums[i]
    new_new_num = new_new_nums[i]

    if new_num != new_new_num:
        print(line, new_num, new_new_num)




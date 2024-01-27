from collections import deque


def Distance(checker, words):
    lenChecker = len(checker)
    lenWord = len(words)
    length_difference_threshold = 3
    if abs(lenChecker - lenWord) > length_difference_threshold:
        return -1

    # Initialize the dynamic programming table
    d = [[0] * (lenWord + 1) for _ in range(lenChecker + 1)]
    for i in range(lenChecker + 1):
        d[i][0] = i
    for j in range(lenWord + 1):
        d[0][j] = j

    # Fill the dynamic programming table
    for i in range(1, lenChecker + 1):
        for j in range(1, lenWord + 1):
            if checker[i - 1] == words[j - 1]:
                substitutionCost = 0
            else:
                substitutionCost = 1
            d[i][j] = min(
                d[i - 1][j] + 1,  # deletion
                d[i][j - 1] + 1,  # insertion
                d[i - 1][j - 1] + substitutionCost,  # substitution
            )

    return d[lenChecker][lenWord]


class LimitedQueue:
    def __init__(self):
        self.queue = deque(maxlen=8)

    def append(self, item):
        # Ensure the item has the correct format ["apples", 1]
        if not isinstance(item, list) or len(item) != 2 or not isinstance(item[1], int):
            raise ValueError(
                "Invalid item format. Should be a list with two elements: ['apples', 1]"
            )

        # Append the new element and maintain order based on the number element
        self.queue.append(item)
        self.queue = deque(sorted(self.queue, key=lambda x: (x[1], x[0])))
        if len(self.queue) > 8:
            self.queue.pop()

    def display(self):
        # Display table header
        print("{:<3} {:<10} {:<10}".format("nu", "word", "distance"))
        print("-" * 30)

        # Display table content
        for index, (word, distance) in enumerate(self.queue):
            print("{:<3} {:<10} {:<10}".format(index, word, distance))


# Example usage:


def wordChecker(word):
    limited_queue = LimitedQueue()

    file_path = "../../../database/dictionary.txt"
    word = " " + word.upper()

    with open(file_path, "r") as file:
        for line in file:
            temp = " " + line.strip().upper()
            dis = Distance(temp, word)
            if 0 < dis <= 2:
                limited_queue.append([line.strip(), dis])

    if limited_queue.queue:
        corrected_word = limited_queue.queue[0][0]
        return corrected_word
    else:
        return None







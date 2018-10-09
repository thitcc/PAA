def buildMemo(text_length):
    memo = [-1] * text_length

    for i in range(text_length):
        memo[i] = [-1] * text_length
    return memo

def badness(i, j):
    """ Badness calculate how good or bad a word sequence is in a row.
        It has a value of 500 if you have only one word in a row.
        Return is squared to put even more weight on the difference,
        that way we can avoid lines with many spaces """

    if i == j:
        return 500

    gaps = j - i  # Number of gaps between words
    total_length = 0

    for w in text[i:j+1]:
        total_length += len(w)

    total_length += gaps  # Total number of characters if each gap has only 1 space

    if total_length > width:
        return float('inf')

    spaces = width - total_length

    x = spaces // gaps  # Number of spaces to each gap
    y = spaces % gaps   # What is left of spaces to be distributed

    b = 0  # Resulting badness

    for _ in range(gaps - y):  # This loop will compute x spaces in each gap
        b += x ** 2

    for _ in range(y):
        b += (x + 1) ** 2  # This loop will calculate the distribution of y spaces in the gaps from back to front

    return b

def fillMatrix(text_length):
    for i in range(text_length):
        for j in range(i, text_length):
            memo[i][j] = badness(i, j)

def print_txt(i, j):
    gaps = j - i

    if gaps == 0:
        print(text[j])
        return

    spaces_to_gap = [' '] * gaps

    total_length = gaps

    for w in text[i:j+1]:
        total_length += len(w)

    spaces = width - total_length

    x = spaces // gaps  # Number of spaces to each gap
    y = spaces % gaps   # What is left of spaces to be distributed

    # The part above follow the same logic of badness

    for k in range(gaps):
        for _ in range(x):
            spaces_to_gap[k] += ' '

    for k in range(gaps-1, gaps - y - 1, -1):
        spaces_to_gap[k] += ' '

    k = 0
    for w in text[i:j+1]:
        if k == gaps:
            print(w)
        else:
            print(w + spaces_to_gap[k], end='')
        k += 1


def justify(n):
    costs = [-1] * (n + 1)
    result = [-1] * n

    for i in range(n-1, -1, -1):
        minimum = float('inf')
        for j in range(n, i, -1):
            value = costs[j] + memo[i][j-1]
            if value < minimum:
                minimum = value
                result[i] = j

        costs[i] = minimum

    print(result)

    k = 0
    for _ in range(0, n, result[k] - k):
        if k < n:
            print_txt(k, result[k] - 1)
            k = result[k]
    print()

memo = []
text = []
width = int(input())

while width > 0:
    line = input().split(' ')
    if line[0] != '':
        for word in line:
            text.append(word)
    else:
        tl = len(text)
        memo = buildMemo(tl)  # Build memo matrix for DP
        fillMatrix(tl)        # Put the costs in the memo matrix
        justify(tl)           # you know
        width = int(input())
        text = []

def fillWithBadness(txt_len, memo):
    for i in range(txt_len):
        memo[i][i] = 500    # when there is no word
        for j in range(i + 1, txt_len):
            gaps = j - i
            interval_length = gaps  # every element except the last one has at least one space, so it counts

            for word in text[i:j+1]:
                interval_length += len(word)

            if interval_length > width:
                memo[i][j] = float('inf')
            elif j - i == 1:
                memo[i][j] = 500  # when there is 1 word
            else:
                spaces = width - interval_length

                equal_spaces = spaces // gaps  # every gap will have itself (1) plus equal_spaces in it
                remaining_spaces = spaces % gaps  # we will distribute the remaining spaces

                result = [equal_spaces for _ in range(gaps)]

                while remaining_spaces > 0:
                    gaps -= 1
                    remaining_spaces -= 1
                    result[gaps] += 1

                badness = 0

                for gap in result:
                    badness += gap ** 2

                memo[i][j] = badness

    return memo

def justify(txt_len):
    memo = [[-1 for _ in range(txt_len)] for _ in range(txt_len)]  # memo init
    memo = fillWithBadness(txt_len, memo)  # memo fill
    print(memo)

width = int(input())
text = []

while width > 0:
    line = input().split()  # get a line from the paragraph
    if len(line) != 0:
        for element in line:
            text.append(element)  # fill the text array with every element in that line
    else:
        justify(len(text))
        width = int(input())
        text = []  # reset text array

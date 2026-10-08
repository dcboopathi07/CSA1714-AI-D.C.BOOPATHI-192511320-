from itertools import permutations

word1 = "SEND"
word2 = "MORE"
result = "MONEY"

letters = set(word1 + word2 + result)

for values in permutations(range(10), len(letters)):
    digit = dict(zip(letters, values))

    # First letters cannot be zero
    if digit['S'] == 0 or digit['M'] == 0:
        continue

    SEND = (digit['S'] * 1000 +
            digit['E'] * 100 +
            digit['N'] * 10 +
            digit['D'])

    MORE = (digit['M'] * 1000 +
            digit['O'] * 100 +
            digit['R'] * 10 +
            digit['E'])

    MONEY = (digit['M'] * 10000 +
             digit['O'] * 1000 +
             digit['N'] * 100 +
             digit['E'] * 10 +
             digit['Y'])

    if SEND + MORE == MONEY:
        print("Solution found:")
        print("S =", digit['S'])
        print("E =", digit['E'])
        print("N =", digit['N'])
        print("D =", digit['D'])
        print("M =", digit['M'])
        print("O =", digit['O'])
        print("R =", digit['R'])
        print("Y =", digit['Y'])

        print("\n", SEND)
        print("+", MORE)
        print("------")
        print(MONEY)
        break

n = int(input("Sisesta majade arv (1–9): "))

maja = [
    "  ~~~~~~  ",
    " /______\\ ",
    " |  []  | ",
    "  ------  "
]

for rida in maja:
    print((" " .join([rida] * n)))

n = int(input("Sisesta majade arv (1–9): "))

maja = [
    "    ~~~~~",
    "   /_____\\",
    "   | []  |",
    "    -----"
]

for rida in maja:
    print((" " .join([rida] * n)))

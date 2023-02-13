import random

angolszavak = ["dog", "cat", "mouse", "horse", "cow", "pig", "sheep", "chicken", "duck", "goat"]
magyar = ["kutya", "macska", "egér", "ló", "tehén", "malac", "bárány", "csirke", "kacsa", "kecske"]
wellAnswered = []
run = 0
while run == 0:
    option = int(input("1. Szókikérdezés\n2. Új szó felvitele\n3. Kilépés\n:"))
    if option == 1:
        index = 0
        correct = 0
        while index < 5:
            engWorld = random.choice(angolszavak)
            if engWorld not in wellAnswered:
                wellAnswered.append(engWorld)
                index += 1
                print(engWorld)
                answer = input("Add meg a magyar megfelelőjét: ")
                if answer == magyar[angolszavak.index(engWorld)]:
                    correct += 1
            else:
                if len(wellAnswered) == len(angolszavak):
                    print("Minden szót megismertél!")
                    break
                else:
                    continue
        print("Ön ", correct, " helyes választ adott meg, ez ", correct / 5 * 100, "%")
    if option == 2:
        angol = input("Add meg az új szót angolul: ")
        magyar.append(input("Add meg a magyar megfelelőjét: "))
        angolszavak.append(angol)
    if option == 3:
        run = 1
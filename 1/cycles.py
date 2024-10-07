for i in range(4+1):
    print("*" * i)

print()

Size = 4
for i in range(Size):
    print("*" * Size)

for i in "Фикус":
    print(i)

Step = 1
while Step < 10+1:
   print(f"Цикл выполнился: {Step} раз")
   Step += 1


Number = int(input())
while Number != 0:
    Sum = 0
    for Num in str(Number): Sum += int(Num)
    print("Число делится на 3" if Sum % 3 == 0 else "Число не делится на 3")
    Number = int(input())


Number = int(input())
while Number != 0:
    print("Чётное" if Number % 2 == 0 else "Нечётное")
    Number = int(input())
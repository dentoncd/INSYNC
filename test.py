import random, time

l = []
r = 0
for i in range(0, 50):
    l.append(random.randint(1, 20))

for i in range(0, len(l)):
    r = l[i]
    print(f"\rRandom Number: {r}", end="")
    time.sleep(0.05)
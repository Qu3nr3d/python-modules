def generator():
    n = 5
    while True:
        yield n
        n +=1

def generator_1():
    n = 5
    for i in range(5):
        yield n
        n +=1

numbers = generator_1()

for number in generator():
    print(number)




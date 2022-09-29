from time import sleep
queque = []

def counter():
    counter = 0
    while True:
        print(counter)
        counter += 1
        yield

def printer():
    counter = 0
    while True:
        if counter % 3 == 0:
            print('Bang!')
        counter += 1
        yield

def main():
    while True:
        g = queque.pop(0)
        next(g)
        queque.append(g)
        sleep(1)

if __name__ == '__main__':
    g1 = counter()
    queque.append(g1)
    g2 = printer()
    queque.append(g2)
    main()
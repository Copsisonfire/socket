#Делегирующий генератор это тот генератор, который вызывает другой
# генератор (подгенератор)

from inspect import getgeneratorstate

class BlaBlaError(Exception):
    pass

def do_none(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return wrapper

# @do_none
def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            # print('Ku-ky')
            break
        else:
            print('..............', message)
    return "returned from subgen()"

@do_none
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaError as er:
    #         g.throw(er)
    result = yield from g
    print(result)

sg = subgen()
g = delegator(sg)
g.send('Ok')
g.throw(StopIteration)

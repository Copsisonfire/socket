from inspect import getgeneratorstate

class BlaBlaError(Exception):
    pass

def do_none(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return wrapper

@do_none
def gen():
    count = 0
    sum = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        except BlaBlaError:
            print('vobla')
            break
        else:
            count += 1
            sum += x
            average = round(sum/count, 2)
    return f'Average = {average}'


a = gen()
print(getgeneratorstate(a))
a.send(4)
a.send(6)
a.send(9)

try:
    a.throw(StopIteration)
except StopIteration as er:
    print(er)
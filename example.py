def gen():
    print('1')
    yield 1
    print('2')
    yield 2
    print('3 dupa')


g = gen()

print(next(g))
print(next(g))
print(next(g))

# for x in gen():
#     print(x)

def gen_infinite():
    idx = 0

    while True:
        yield idx
        idx += 1
        if idx > 5:
            return 'StopIteration Exception'

# RxPy
# for x in gen_infinite():
#     print(x)

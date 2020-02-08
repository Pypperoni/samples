global globalvalue
globalvalue = 0

def test_loop():
    num = 0
    for i in range(500):
        num += i

    print('Expected sum: 124750')
    print('Built-in sum:', sum(range(500)))
    print('Loop sum:', num)

def test_nested_class():
    class NestedInterableClass:
        def __iter__(self):
            return self

        def __next__(self):
            global globalvalue
            globalvalue += 1
            return globalvalue

    c = NestedInterableClass()
    num = 0
    for number in c:
        num += number
        if number == 50:
            break

    print('Expected sum: 1275')
    print('Loop sum:', num)

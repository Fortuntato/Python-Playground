def coroutineDecorator(func):
    def wrap(*args, **kwargs):
        cr = func(*args,**kwargs)
        next(cr)
        return cr
    return wrap

@coroutineDecorator
def counter(string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item,str):
                if item in string:
                    count += 1
                    print(item)
                else:
                    print('No match')
            else:
                print('Not a string')
    except GeneratorExit:
        print(count)
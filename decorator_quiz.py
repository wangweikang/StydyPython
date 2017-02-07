# bar start
# hello world
# bar end

def bar(func):
    def log():
        print('Start bar')
        func()
        print('End bar')
    return log


@bar
def foo():
    print ("hello world")


foo()
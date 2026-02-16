#decorators- wraper funcation around the funcations are called as decorators

def make_preety (func):
    def inner():
        print("i got decorator")
        func()
    return inner
@make_preety
def vanillacake():
    print("I am the vanilla cake")

@make_preety
def strawberrycake():
    print("I am the strawberry cake")

vanillacake()
strawberrycake()
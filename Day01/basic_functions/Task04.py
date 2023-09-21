def bread () :
    print (" <////////// > ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print ("O O O O O O")
def ham () :
    print (" ============ ")

def sandwich(x, vegetarian=True) :
    for _ in range(x):
        bread()
        lettuce()
        tomato()
        if not vegetarian:
            ham()
            ham()
        bread()

sandwich(1, vegetarian=False)
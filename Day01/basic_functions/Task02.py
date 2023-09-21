def bread () :
    print (" <////////// > ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def tomato () :
    print ("O O O O O O")
def ham () :
    print (" ============ ")

def sandwich(x) :
    for _ in range(x):
        bread()
        lettuce()
        tomato()
        ham()
        ham()
        bread()

sandwich(42)
# unA

def unA(string, n):

    def nbr_lower(string):

        count=0

        for char in string:
            if char.islower():
                count+=1

        return count

    if nbr_lower(string) >= n:
        return True
    else:
        return False

print(unA("PoPo", 3))

# unB

def unB(string, n):

    def nbr_lower(string):

        count=0

        for char in string:
            if char.isupper():
                count+=1

        return count

    if nbr_lower(string) >= n:
        return True
    else:
        return False

print(unB("PoPo", 3))

# unC

def unC(string, n):

    def nbr_lower(string):

        count=0

        for char in string:
            if char.isalpha():
                count+=1

        return count

    if nbr_lower(string) >= n:
        return True
    else:
        return False

print(unC("PoPo",4))

# unD

def unD(string, n):

    def nbr_lower(string):

        count=0

        for char in string:
            if not (char.isalpha() or char.isdigit()):
                count+=1

        return count

    if nbr_lower(string) >= n:
        return True
    else:
        return False

print(unD("PoPo!!!",2))

# unE

def unE(string, n):

    def nbr_lower(string):

        count=0

        for char in string:
            if char.isdigit():
                count+=1
            else:
                count+=0

        return count

    if nbr_lower(string) >= n:
        return True
    else:
        return False

print(unE("5PoPo2!!!",2))
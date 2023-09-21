def check_password(rule, n, string):

    if rule == "lower":
        
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
        
    if rule == "special":

        def nbr_special(string):
            count=0

            for char in string:
                if not (char.isalpha() or char.isdigit()):
                    count+=1
            
            return count

        if nbr_special(string) >= n:
            return True
        else:
            return False

        
print(check_password("lower", 4, "bonjour123")) and (check_password("special", 2, "coucou"))
# Remove every single 9 between 7
# "79712312" --> "7712312"
# "79797"    --> "777"


def seven_ate9(str_):
    
    new_str = str_
    while "797" in new_str:
        i=new_str.find("797")
        if new_str[i:i+3]=="797":
            new_str=new_str.replace("797", "77")
          
    return new_str
        

str_="7779797"
result = seven_ate9(str_)
print(result)
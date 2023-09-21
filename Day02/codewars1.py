def mix(colors):

    if len(colors) == 1:
        return colors[0]

    new_colors=[]

    for i in range(len(colors)-1):
        if (i+1)>(len(colors)-1):
            break
        elif (colors[i] == "R" and colors[i+1] == "R") or ((colors[i] == "B" and colors[i+1] == "G") or (colors[i+1] == "B" and colors[i] == "G")):
            new_colors.append("R")
        elif ((colors[i] == "R" and colors[i+1] == "G") or (colors[i+1] == "R" and colors[i] == "G")) or (colors[i] == "B" and colors[i+1] == "B"):
            new_colors.append("B")
        elif ((colors[i] == "R" and colors[i+1] == "B") or (colors[i+1] == "R" and colors[i] == "B")) or (colors[i] == "G" and colors[i+1] == "G") :
            new_colors.append("G")
        i+=1

    print(new_colors)
    return mix(new_colors)

colors = ["R", "R", "G", "B", "R", "G", "B", "B"]
result =mix(colors)

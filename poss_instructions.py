def poss_instructions(color, includeTetris = False, hasHoles = False):
    if not hasHoles: #has no holes, thus not placing in the far lane
        instructions = []
        if color == "purple":
            for x in range(4): #4 poss rotns
                if x == 0:
                    for y in range(1,8): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 1:
                    for y in range(0,8): #7-9 pos lanes
                        instructions.append([x,y])                
                elif x == 2:
                    for y in range(1,8): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 3:
                    for y in range(1,9): #7-9 pos lanes
                        instructions.append([x,y])
        elif color == "red":
            for x in range(2):
                if x == 0:
                    for y in range(1,8): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 1:
                    for y in range(0,8): #7-9 pos lanes
                        instructions.append([x,y])   
        elif color == "green":
            for x in range(2):
                if x == 0:
                    for y in range(1,8): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 1:
                    for y in range(0,8): #7-9 pos lanes
                        instructions.append([x,y])   
        elif color == "blue":
            for x in range(4): #4 poss rotns
                if x == 0:
                    for y in range(1,8): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 1:
                    for y in range(0,8): #7-9 pos lanes
                        instructions.append([x,y])                
                elif x == 2:
                    for y in range(1,8): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 3:
                    for y in range(1,9): #7-9 pos lanes
                        instructions.append([x,y]) 
        elif color == "orange":
            for x in range(4): #4 poss rotns
                if x == 0:
                    for y in range(1,8): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 1:
                    for y in range(0,8): #7-9 pos lanes
                        instructions.append([x,y])                
                elif x == 2:
                    for y in range(1,8): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 3:
                    for y in range(1,9): #7-9 pos lanes
                        instructions.append([x,y])
        elif color == "light blue":
            for x in [0,3]: #4 poss rotns
                if x == 0:
                    for y in range(1,7): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 3:
                    if includeTetris:
                        for y in range(0,10):
                            instructions.append([x,y])
                    else:
                        for y in range(0,9):
                            instructions.append([x,y])
                                            
        elif color == "yellow":
            for x in range(1): #4 poss rotns
                for y in range(0,8): #7-9 pos lanes
                    instructions.append([x,y])

        return instructions #in form of list of [rotns, lane]
    
    else: #has holes, placement everywhere is fair game
        instructions = []
        if color == "purple":
            for x in range(4): #4 poss rotns
                if x == 0:
                    for y in range(1,9): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 1:
                    for y in range(0,9): #7-9 pos lanes
                        instructions.append([x,y])                
                elif x == 2:
                    for y in range(1,9): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 3:
                    for y in range(1,10): #7-9 pos lanes
                        instructions.append([x,y])
        elif color == "red":
            for x in range(2):
                if x == 0:
                    for y in range(1,9): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 1:
                    for y in range(0,9): #7-9 pos lanes
                        instructions.append([x,y])   
        elif color == "green":
            for x in range(2):
                if x == 0:
                    for y in range(1,9): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 1:
                    for y in range(0,9): #7-9 pos lanes
                        instructions.append([x,y])   
        elif color == "blue":
            for x in range(4): #4 poss rotns
                if x == 0:
                    for y in range(1,9): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 1:
                    for y in range(0,9): #7-9 pos lanes
                        instructions.append([x,y])                
                elif x == 2:
                    for y in range(1,9): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 3:
                    for y in range(1,10): #7-9 pos lanes
                        instructions.append([x,y]) 
        elif color == "orange":
            for x in range(4): #4 poss rotns
                if x == 0:
                    for y in range(1,9): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 1:
                    for y in range(0,9): #7-9 pos lanes
                        instructions.append([x,y])                
                elif x == 2:
                    for y in range(1,9): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 3:
                    for y in range(1,10): #7-9 pos lanes
                        instructions.append([x,y])
        elif color == "light blue":
            for x in [0,3]: #4 poss rotns
                if x == 0:
                    for y in range(1,8): #7-9 pos lanes
                        instructions.append([x,y])
                elif x == 3:
                    if includeTetris:
                        for y in range(0,10):
                            instructions.append([x,y])
                    else:
                        for y in range(0,10):
                            instructions.append([x,y])
                                            
        elif color == "yellow":
            for x in range(1): #4 poss rotns
                for y in range(0,9): #7-9 pos lanes
                    instructions.append([x,y])

        return instructions #in form of list of [rotns, lane]
if __name__ == "__main__":
    print(poss_instructions("purple"))
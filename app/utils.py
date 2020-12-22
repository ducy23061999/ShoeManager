

def getShoeWithMax(shoes):
    maxItems = []
    for i in range(0, 12):
        if i < len(shoes):
            maxItems.append(shoes[i])
        else:
            break
    return maxItems
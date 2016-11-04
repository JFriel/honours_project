
def entityFinder(chunkedList):
    entities = []
    actions = []
    for chunk in chunkedList:
        if(chunk[1] == 'ORG' or chunk[1] == 'PLACE' or chunk[1] == 'NP'):
            entities.append(chunk[0])
        elif( chunk[1] == 'ACTION'):
            actions.append(chunk[0])

    return [entities,actions]

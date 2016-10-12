def traverse(t):
    try:
        t.label()
    except AttributeError:
        return []
    else:
        grammer=['NP','PLACE','ORG','ACTION']
        data = []
        if(t.label() in grammer):
            data.append([" ".join([a for (a,b) in t.leaves()]), t.label()])
        else:
            for child in t:
                data += traverse(child)

    return data

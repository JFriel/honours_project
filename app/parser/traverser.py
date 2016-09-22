def traverse(t):
    grammer=['NP','PLACE','ORG','ACTION']
    try:
        t.label()
    except AttributeError:
        return
    else:
        if (t.label() in grammer):
            print t#can be changed
        else:
            for child in t:
                traverse(child)

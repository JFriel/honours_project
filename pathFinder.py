import datetime
paths = eval(open('pathway','r').readlines()[0])
data = open('data/todayinhistory.txt','r').readlines()
start = [None,0]
data2 = {}
for item in data:
    data2[item[11:]] = item[0:10]

keys = paths.keys()

for k in keys:
    before = len(paths[k])
    if before > start[1]:
        start = [k,before]

#print sorted([len(paths[x]) for x in keys])

#print start
maxPath = []
#
#print paths
ordering = []
for k in sorted(paths, key=lambda k: len(paths[k]), reverse=True):
    ordering.append(k)


orderingDates = []
for item in ordering:
    try:
        orderingDates.append(data2[item])
    except:
        print item


#correctOrder =  sorted(orderingDates, key=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d'))
concordent = 0
discordent = 0

for i in range(0,len(orderingDates)):
    for j in range(i+1,len(orderingDates)):
        print datetime.datetime.strptime(orderingDates[i],'%Y-%m-%d') < datetime.datetime.strptime(orderingDates[j],'%Y-%m-%d')
        if datetime.datetime.strptime(orderingDates[i],'%Y-%m-%d') < datetime.datetime.strptime(orderingDates[j],'%Y-%m-%d'):
            concordent += 1
        else:
            discordent += 1

print concordent
print discordent
print len(orderingDates)
tau = (concordent - discordent) / (len(orderingDates) * (len(orderingDates)-1) /2)

print tau

"""
for k in range(len(keys)):
    newPaths =  find_all_paths(paths,start[0],keys[k])
    print k
    for path in newPaths:
        print len(path)
        if( len(path) >= len(maxPath)):
            maxPath = path
#maxPath = max(p for p in paths)
print maxPath
print len(maxPath)"""

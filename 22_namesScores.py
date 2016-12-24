names = {}                      #dictionary containing the value for each name
listNames = []                  #List of names

#Reading the values
n = int(raw_input())
for i in xrange(n):
    listNames.append(raw_input())
listNames.sort()

#Setting the dictionary with the proper value for each name
for i in range(1, len(listNames)+1):
    name = listNames[i-1]
    names[name] = (i) * reduce(lambda x, y: x+y, map(lambda x: x-64, map(ord, list(name))))

num = int(raw_input())
for i in xrange(num):
    print names[raw_input()]

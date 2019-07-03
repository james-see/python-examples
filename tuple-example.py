# tuple sort example
# author: James Campbell
# date: 2015-05-28
# Date Updated: 2 July 2019
valued = []
lettered = []
plusone = []
listed = [(('d', 0), ('g', 0)), (('d', 0), ('d', 1)), (('i', 0), ('g', 0))]
for (x, y) in listed:
    for subx, suby in x, y:
        valued.append(int(suby))
        lettered.append(subx)
for value in valued:
    value = value + 1
    plusone.append(int(value))
# print plusone
coolness = zip(lettered, plusone)
print(coolness)

print(map(list, zip(lettered, plusone)))

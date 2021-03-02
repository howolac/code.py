def displayInventory(item):
    count = 0
    for k, v in item.items():
        print(k + ' ' + str(v))
        count = count + v


def addedItems(inv, item):
    sum = 0
    for j in inv.values():
        sum += j
    for i in item:
        if i in inv.keys():
            inv[i] += 1
            sum += 1

        else:
            inv.setdefault(i, 1)
            sum += 1

    print(sum)
    return inv


item = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}

inv = addedItems(inv, item)

displayInventory(inv)
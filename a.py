item = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(ie):
    count = 0
    for k, v in ie.items():
        print(str(v) + ' ' + k)
        count = count + v
    return count


print(displayInventory(item))

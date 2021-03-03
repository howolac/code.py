def picnic(a, lw, rw):
    print('Picnic items'.center(lw + rw, '='))
    for k, v in a.items():
        print(k.ljust(lw, '.') + ' ' + str(v).ljust(rw))


picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

picnic(picnicItems, 10, 10)
picnic(picnicItems, 20, 10)

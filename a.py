allguests = {
    'alice': {
        'apple': 5,
        'banana': 12
    },
    'Bob': {
        'ham': 13,
        'chicken': 99
    },
    'mike': {
        'soup': 10,
        'banana': 6
    }
}


def totalbrought(guest, item):
    number = 0
    for k, v in guest.items():
        number = number + v.get(item, 0)
    return number


print('apple=', str(totalbrought(allguests, 'apple')))

print('banana=', str(totalbrought(allguests, 'banana')))

print('chicken=', str(totalbrought(allguests, 'chicken')))

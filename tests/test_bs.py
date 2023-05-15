from BinarySearch.bs import locate_card

test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'numb_query': 7
    },
    'output': 3
}

locate_card(**test['input']) == test['output']
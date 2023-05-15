#Linear Search Algorithm

def locate_card(cards, numb_query):
    position = 0
    while position < len(cards):
        if cards[position] == numb_query:
            return position
        position += 1
    return -1
        
        
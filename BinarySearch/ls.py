#Linear Search Algorithm

# Problem: ALICE'S CARDS
# Alice has some cards with numbers written on them.
# She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
# She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
# Write a function to help Bob locate the card.

# We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order.
# We also need to minimize the number of times we access elements from the list.

def locate_card(cards, numb_query):
    position = 0
    while position < len(cards):
        if cards[position] == numb_query:
            return position
        position += 1
    return -1
        
        
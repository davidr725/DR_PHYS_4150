import numpy as np

def build_deck():
    deck = []
    suites = ['\u2661','\u2662', '\u2663', '\u2664']
    values = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    for val in values:
        for suit in suites:
            deck.append([val,suit])
    return deck
def draw_hand(n=5):
    deck = build_deck()
    hand = []
    for i in range(n):
        draw = np.random.randint(0,len(deck),1)
        draw = int(draw[0])
        hand.append(deck[draw])
        deck.pop(draw)
    return hand, deck
def find_dups():
    hand, deck = draw_hand()
    new_hand = []
    for i in range(0,len(hand)):
        for j in range(i+1,len(hand)):
            for k in range(j+1,len(hand)):
                if hand[i][0] == hand[j][0] and hand[j][0] == hand[k][0]:
                    new_hand.append(hand[i])
                    new_hand.append(hand[j])
                    new_hand.append(hand[k])
    if len(new_hand) == 0:
        for i in range(0,len(hand)):
            for j in range(i+1,len(hand)):
                if hand[i][0] == hand[j][0]:
                    new_hand.append(hand[i])
                    new_hand.append(hand[j])
                if len(new_hand) > 0:
                    break
            if len(new_hand) > 0:
                break
    if len(new_hand) == 0:
        hand.pop(4)
        hand.pop(3)
        hand.pop(2)
    return new_hand, hand, deck
def find_dups_2(hand):
    for i in range(0,len(hand)):
        for j in range(i+1,len(hand)):
            for k in range(j+1,len(hand)):
                if hand[i][0] == hand[j][0] and hand[j][0] == hand[k][0]:
                    #print('test1')
                    return 1
                else:
                    #print('test2')
                    return 0
def re_draw():
    new_hand, hand, deck = find_dups()
    if len(new_hand) >= 3:
        #print('test3')
        return 1
        
    if len(new_hand) == 2:
        for i in range(3):
            draw = np.random.randint(0,len(deck),1)
            draw = int(draw[0])
            new_hand.append(deck[draw])
            deck.pop(draw)
        for j in range(2,5):
            if new_hand[j][0] == new_hand[0][0]:
                #print('test4')
                return 1
            else:
                #print('test5')
                return 0

    if len(hand) == 2:
        for i in range(3):
            draw = np.random.randint(0,len(deck),1)
            draw = int(draw[0])
            hand.append(deck[draw])
            deck.pop(draw)
        return find_dups_2(hand)

answer = sum([re_draw() for k in range(50000)])/500
print('The probability of drawing 3 of a kind ' + 
'by redrawing up to 3 cards is: ' + str(answer) + '%' )




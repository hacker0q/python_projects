import random
Q='''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_
      |  \/ K|                            _/ |                
      '------'                           |__/ 
'''

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def compare(u_score,c_score):
    if u_score==c_score:
        return "draw"
    elif c_score==0:
        return "you lose,opponent has a black jack"
    elif u_score==0:
        return "win with a black jack"
    elif u_score>21:
        return "you went over you lose"
    elif c_score>21:
        return "opponent went over,you win"
    elif u_score>c_score:
        return "you win"
    else:
        return "you lose"
def deal_cards():
    card=random.choice(cards)
    return card
def calculated_score(Cards):
    if sum(Cards)==21 and len(Cards)==2:
        return 0
    if 11 in Cards and sum(Cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(Cards) 
def playgame():
    user_score=[]
    computer_score=[]
    is_game_over=False

    for i in range(2):
        user_score.append(deal_cards())
        computer_score.append(deal_cards())
    while not is_game_over:
        user_cards=calculated_score(user_score)
        computer_cards=calculated_score(computer_score)
        print(f"your cards:{user_score},current score:{user_cards}")
        print(f"computer's first card:{computer_score[0]}")
        if user_cards==0 or computer_cards==0 or user_cards > 21:
            is_game_over=True
        else:
            Continue=input("type 'y' to get another card,type 'n' to end  the game")
            if Continue=="y":
                user_score.append(deal_cards())
            if Continue=="n":
                is_game_over=True
    while computer_cards !=0 and computer_cards<17:
        computer_score.append(deal_cards())
        computer_cards=calculated_score(computer_score)
    print("your cards are: ",user_score,user_cards)
    print("computer cards are: ",computer_score,computer_cards)
    print(compare(user_cards,computer_cards))
hi=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if hi=="y":
    print(Q)
    playgame()


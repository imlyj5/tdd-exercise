VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    total_score = 0
    ace_count = 0

    # Check if the hand has more than 5 cards
    if len(hand) > 5:
        return "Invalid"
    
    # Check if all cards in hand are valid
    for card in hand:
        if card not in VALID_CARDS:
            return "Invalid"
    
    # Process non-Ace cards first to determine the initial total score
    for card in hand:
        if card in ['Jack', 'Queen', 'King']:
            total_score += 10  # Face cards worth 10 points
        elif card == 'Ace': 
            total_score += 0
            ace_count += 1  # Count the amount of Ace cards separately
        else:
            total_score += card  # Number cards add their face value
    
    # Calculate the remaining buffer space before reaching 21 (excluding Aces for now)
    buffer = 21 - total_score 

    # Determine how to count Aces based on the buffer space
    if ace_count == 1 and buffer >= 11:
        # If there's only one Ace and the buffer allows, count this Ace as 11
        total_score += 11

    elif ace_count > 1 and buffer >= 11:
        # If there are multiple Aces and enough buffer space, try counting the first Ace as 11
        if total_score + 11 + (ace_count -1) > 21:
            # If this strategy would exceed 21, count all Ace cards as 1
            total_score = total_score + ace_count 
        else:
            # Otherwise, count the first Ace as 11 and the rest as 1
            total_score = total_score + 11 + (ace_count -1) 

    else:
        # If there's not enough room, count all Aces as 1
        total_score += ace_count  


    if total_score >21: 
        # If the total exceeds 21, return "Bust"
        return "Bust"

    return total_score


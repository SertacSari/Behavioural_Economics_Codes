#Author: Ahmet Sertaç Sarı
# Chances of winning the game, the randomness come from calculations of winning

import random

def play_game(rounds=10):
    results = []
    
    for round_num in range(rounds):
        # Calculate probabilities for this round
        prob_first = (round_num + 1) / 10  # Increases from 1/10 to 10/10
        prob_second = 1 - prob_first       # Decreases from 9/10 to 0/10
        
        # Let player choose option
        print(f"\nRound {round_num + 1}")
        print(f"Current probabilities:")
        print(f"First outcome: {prob_first:.1f}")
        print(f"Second outcome: {prob_second:.1f}")
        
        while True:
            choice = input("Choose option A ($2.00/$1.60) or B ($3.85/$0.10): ").upper()
            if choice in ['A', 'B']:
                break
            print("Invalid choice! Please choose A or B.")
        
        # Determine outcome
        random_num = random.random()
        
        if choice == 'A':
            if random_num < prob_first:
                outcome = 2.00
                print(f"You won ${outcome:.2f}!")
            else:
                outcome = 1.60
                print(f"You won ${outcome:.2f}!")
        else:  # choice == 'B'
            if random_num < prob_first:
                outcome = 3.85
                print(f"You won ${outcome:.2f}!")
            else:
                outcome = 0.10
                print(f"You won ${outcome:.2f}!")
                
        results.append(outcome)
        
        # Show running total
        print(f"Total winnings so far: ${sum(results):.2f}")
    
    # Final results
    print("\nGame Over!")
    print(f"Total winnings: ${sum(results):.2f}")
    print(f"Average per round: ${sum(results)/len(results):.2f}")

def calculate_expected_value(round_num):
    prob_first = (round_num + 1) / 10
    prob_second = 1 - prob_first
    
    ev_a = (2.00 * prob_first) + (1.60 * prob_second)
    ev_b = (3.85 * prob_first) + (0.10 * prob_second)
    
    return ev_a, ev_b

def show_expected_values():
    print("\nExpected Values for each round:")
    print("Round | Option A  | Option B")
    print("-" * 30)
    
    for round_num in range(10):
        ev_a, ev_b = calculate_expected_value(round_num)
        print(f"{round_num + 1:5d} | ${ev_a:7.2f} | ${ev_b:7.2f}")

def ai_play_game(rounds=10, show_details=False):
    results = []
    ai_choices = []
    
    for round_num in range(rounds):
        # Calculate probabilities for this round
        prob_first = (round_num + 1) / 10
        prob_second = 1 - prob_first
        
        # AI makes choice based on expected value
        ev_a, ev_b = calculate_expected_value(round_num)
        ai_choice = 'A' if ev_a > ev_b else 'B'
        ai_choices.append(ai_choice)
        
        # Determine outcome
        random_num = random.random()
        
        if ai_choice == 'A':
            if random_num < prob_first:
                outcome = 2.00
            else:
                outcome = 1.60
        else:  # choice == 'B'
            if random_num < prob_first:
                outcome = 3.85
            else:
                outcome = 0.10
                
        results.append(outcome)
        
        # Show round details if requested
        if show_details:
            print(f"\nRound {round_num + 1}")
            print(f"Probabilities: First: {prob_first:.1f}, Second: {prob_second:.1f}")
            print(f"Expected Values: A: ${ev_a:.2f}, B: ${ev_b:.2f}")
            print(f"AI chose: {ai_choice}")
            print(f"Outcome: ${outcome:.2f}")
            print(f"Running total: ${sum(results):.2f}")
    
    # Return summary statistics
    return {
        'total_winnings': sum(results),
        'average_per_round': sum(results)/len(results),
        'choices': ai_choices,
        'results': results
    }

def simulate_multiple_games(num_games=100, rounds=10):
    total_winnings = []
    
    for game in range(num_games):
        result = ai_play_game(rounds, show_details=False)
        total_winnings.append(result['total_winnings'])
    
    avg_winnings = sum(total_winnings) / len(total_winnings)
    min_winnings = min(total_winnings)
    max_winnings = max(total_winnings)
    
    print(f"\nSimulation Results ({num_games} games):")
    print(f"Average total winnings: ${avg_winnings:.2f}")
    print(f"Best game: ${max_winnings:.2f}")
    print(f"Worst game: ${min_winnings:.2f}")

if __name__ == "__main__":
    print("Welcome to the AI Probability Game!")
    
    # Show one detailed game
    print("\nPlaying one game with detailed output:")
    result = ai_play_game(show_details=True)
    print("\nGame Summary:")
    print(f"Total winnings: ${result['total_winnings']:.2f}")
    print(f"Average per round: ${result['average_per_round']:.2f}")
    print("AI's choices:", ' '.join(result['choices']))
    
    # Simulate multiple games
    print("\nSimulating multiple games...")
    simulate_multiple_games(100) 
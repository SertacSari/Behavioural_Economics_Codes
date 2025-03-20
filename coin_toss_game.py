#Author: Ahmet Sertaç Sarı
# Toss coin game played according to input of rounds, each round cost $4
import random

GWP=int(input("Round: ")) # The input of how many rounds will be played in game

def play_single_round():
    """
    Play a single round of the coin toss game.
    Returns the winnings for this round.
    """
    consecutive_heads = 0
    
    while True:
        toss = random.choice(['H', 'T'])
        if toss == 'H':
            consecutive_heads += 1
        else:  # toss is Tail
            # Calculate winnings: 2^number_of_heads
            winnings = 2 ** consecutive_heads - 4 # should pay 4$ to play the game each
            return winnings, consecutive_heads

def play_game(num_rounds=GWP):
    """
    Play multiple rounds and track results
    """
    total_winnings = 0
    round_results = []
    
    print("Starting the St. Petersburg Coin Toss Game!")
    print("Rules: Get heads to continue doubling your money.")
    print("      Get tails to cash out at 2^n dollars where n is the number of heads.\n")
    
    for round_num in range(num_rounds):
        winnings, heads = play_single_round()
        round_results.append({
            'round': round_num + 1,
            'heads': heads,
            'winnings': winnings
        })
        total_winnings += winnings
        
        print(f"\nRound {round_num + 1}:")
        print(f"Number of heads: {heads}")
        print(f"Round winnings: ${winnings}")
        print(f"Running total: ${total_winnings}")

    # Display final statistics
    print("\n=== Final Results ===")
    print(f"Total games played: {num_rounds}")
    print(f"Total winnings: ${total_winnings}")
    print(f"Average winnings per round: ${total_winnings/num_rounds:.2f}")
    
    # Find the best and worst rounds
    best_round = max(round_results, key=lambda x: x['winnings'])
    worst_round = min(round_results, key=lambda x: x['winnings'])
    
    print(f"\nBest round: Round {best_round['round']} with ${best_round['winnings']} ({best_round['heads']} heads)")
    print(f"Worst round: Round {worst_round['round']} with ${worst_round['winnings']} ({worst_round['heads']} heads)")
    
    return round_results

if __name__ == "__main__":
    # Set random seed for reproducibility (optional)
    random.seed()
    
    # Play 10 rounds
    results = play_game(GWP)
    
    # Show sequence of all results
    print("\nSequence of results:")
    for result in results:
        print(f"Round {result['round']}: {result['heads']} heads = ${result['winnings']}") 
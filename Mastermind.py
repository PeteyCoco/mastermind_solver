###############################################################
#
#   The following program solves a 'n' games of Mastermind using
#   a random guessing algorithm. Results of games are stored
#   in a csv in the locatio of this script.
#
###############################################################

import sys
import numpy as np
import itertools
import pandas as pd
import os

MAX_ATTEMPT = 20

#   Turns a guess into a frequency count of colours
def colour_freq(guess):
    counts = np.histogram(guess, bins=np.arange(7))[0]
    return counts

#   Counts colours in 'guess' and 'code' with matching colour and location
def loc_match(guess, code):
    n_loc = np.sum(np.array(guess) == np.array(code))
    return n_loc

#   Counts colours in 'guess' and 'code' with matching colour
def col_match(guess, code):
    guess_col = colour_freq(guess)
    code_col = colour_freq(code)
    
    n_col = np.sum(np.minimum(guess_col, code_col))
    return n_col

#
#   Given a guess and the number of matching colours 'n_col' and
#   matching locations 'n_loc', reduce the pool of potentially
#   correct codes
#
def reduce_pool(guess, guess_pool, n_col, n_loc):
    # Remove location matches
    pool_loc_match = [loc_match(guess, i) for i in guess_pool]
    idx_match = [i == n_loc for i in pool_loc_match]
    guess_pool = list(itertools.compress(guess_pool,idx_match))
    # Remove colour matches
    pool_col_match = [col_match(guess, i) for i in guess_pool]
    idx_match = [i == n_col for i in pool_col_match]
    guess_pool = list(itertools.compress(guess_pool,idx_match))

    return guess_pool
    
#
#   Generate the code
#
def create_code():
    code = np.random.randint(low = 0, high = 6, size = 4)
    return code


#
#   Compare 'guess' and 'code' and return matching statistics
#
def evaluate_guess(guess, code):
    n_col = col_match(guess, code)
    n_loc = loc_match(guess, code)
    return n_col, n_loc



#
#   The random solving algorithm takes a code and attempts to solve
#   it by random guesses. Returns a list 'game_hist' detailing the
#   steps taken in solving
#
def random_solver(game_num, code):
    
    game_hist = []
    
    guess_pool = list(itertools.product(np.arange(6),repeat=4))
    attempt = 1

    #
    #   At each step chose a random code from the guess_pool, evaluate,
    #   and reduce the guess_pool
    #
    while attempt <= MAX_ATTEMPT:
        size_pool = len(guess_pool)
        if size_pool > 0:
            idx = np.random.randint(low = 0, high=size_pool)
        else:
            idx = 0
            
        guess = guess_pool[idx]
        
        n_col, n_loc = evaluate_guess(guess, code)
        
        game_hist.append([game_num, attempt] + list(guess) + [n_col - n_loc] + [n_loc])
        
        guess_pool = reduce_pool(guess, guess_pool, n_col, n_loc)

        if n_loc == 4:
            print("Game: ", game_num, "solved in ", attempt, " tries")
            break
        
        attempt += 1
    
    return game_hist

##############
# Main method
##############
def main():
    n = int(sys.argv[1])    # Take simulation number 'n' from command line
    
    print("Simulations: ", n )

    #   Record games in a dataframe
    col_names = ['game', 'attempt', 'X1', 'X2','X3','X4', 'n_col', 'n_loc']
    df = pd.DataFrame(columns=col_names)
    
    #   Run 'random_solver' 'n' times
    for i in range(n):
        code = create_code()
        result = random_solver(i, code)
        result = pd.DataFrame(result, columns = col_names)
        df = df.append(result)

    #   Save results
    root_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = root_dir + "\game_data.csv"
    df.to_csv(file_path)
    print(file_path)
        

if __name__ == "__main__":
    main()






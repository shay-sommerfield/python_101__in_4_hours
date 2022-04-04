def determine_winner(player_1_input,player_2_input,winning_throw):
    if player_1_input == winning_throw:
        return 1
    else:
        return 2

###-------------------------------this is our main script-----------------------------------##
if __name__ == "__main__": # called in python so you don't accidentally run a library.
                           # Not absoluetely necessary, but good practice
    player_1_input = "rock"
    player_2_input = "paper"

    # put the inputs together for easy comparison later
    inputs = [player_1_input,player_2_input]

    # cover the tie situation first
    if player_1_input == player_2_input:
        print("Both players tied!")
    # and then any scenario where there is a winner
    else:
        # determine the win in a throw since we know someone win
        if "rock" in inputs and "scissors" in inputs:
            throw_that_won = "rock"

        elif "paper" in inputs and "scissors" in inputs:
            throw_that_won = "scissors"
        else:
            throw_that_won = "paper"

        # this is a dictionary
        # when I input a value I want to get the corresponding losing value
        # so rps_dict["rock"] returns "paper"
        rps_dict = {"rock":"scissors","scissors":"paper","paper":"rock"} # curly braces mean this is a dictionary

        # grab the losing throw because we know the winning throw.
        throw_that_lost = rps_dict[throw_that_won]

        # call our function to determine the winner by checking if their throw matches the winning throw
        winner = determine_winner(player_1_input,player_2_input,throw_that_won)

        # This is a function string. where you can embed variables or even functions 
        # by putting an f right in front of the string
        print(f"{throw_that_won} beats {throw_that_lost}\nPlayer {winner} wins!")
            # ^ Like this f
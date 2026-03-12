def sum_scores(score_strings):
    # define starting total 
    total = 0
    
    # loop through given list of strings 
    for score in score_strings:
        # use the input to convert that might fail, if no error was caught, count the total
        try:
            score_converted = int(score)
        # catch the invalid input (not convertable)
        except ValueError:
            raise ValueError(f"invalid score: {score}")
            
        # catch the negative converted score
        if score_converted < 0:
            raise ValueError(f"score cannot be negative: {score_converted}")

        total = total + score_converted
        
    return total

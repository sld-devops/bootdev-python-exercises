def filter_valid_scores(scores):

    if not isinstance(scores, list): # terminate if input is not a list, raise an error
        raise TypeError("scores must be a list")

    valid_scores = []   
    for score in scores: # iterate trough inputed list
        if (isinstance(score, int) or isinstance(score, float)) and (score >= 0 and score <= 100): # is the item int or float and is that number between 0 and 100?
        # OR if isinstance(score, (int, float)) and 0 <= score <= 100:
            valid_scores.append(score) # if yes, then add item to list
            
    if valid_scores == []:
        raise ValueError("no valid scores") # after loop, if it ends up empty, raise an error
        
    return valid_scores 

def calculate_class_summary(scores):
    valid_scores = filter_valid_scores(scores) # take list from helper and create variable to calculate
    count = len(valid_scores)
    lowest = min(valid_scores)
    highest = max(valid_scores)
    total = sum(valid_scores)
    avg = total / count
    return {
        "count": count,
        "min": lowest,
        "max": highest,
        "avg": avg
}

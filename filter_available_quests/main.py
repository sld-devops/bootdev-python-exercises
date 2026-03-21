def filter_available_quests(quests, min_difficulty):
    # Initialize an empty list to store the names of quests that match our criteria
    quests_matched = []
    # Loop through each quest dictionary in the quests list
    for quest in quests:
        # Check that the quest hasn't been completed AND meets the minimum difficulty requirement
        if not quest["completed"] and quest["difficulty"] >= min_difficulty:
            # Add the quest's name to our results list
            quests_matched.append(quest["name"])
    # Return the final list of matching quest names
    return quests_matched

# Compact comprehension (AI built)

def filter_available_quests(quests, min_difficulty):
    return [q["name"] for q in quests if not q["completed"] and q["difficulty"] >= min_difficulty]

    # [q["name"] - grab the quest's name
    # for q in quests - loop through every quest
    # if not q["completed"] - skip completed quests
    # and q["difficulty"] >= min_difficulty] - skip quests below min difficulty


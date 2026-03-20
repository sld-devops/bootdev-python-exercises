def build_team_scores(plays):
    # what I want to return?
    teams_total_pts = {}
    for item in plays:
        # setting variables for keys to update them later
        team = item[0]   # team name
        score = item[1]  # score
        # if seen first time, add that key's name into dict
        if team not in teams_total_pts:
            teams_total_pts[team] = 0
        # if team is already present, add up this score whats already counted
        teams_total_pts[team] += score
    # get whole dict after no more inputs is given
    return teams_total_pts
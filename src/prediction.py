def generate_prediction(match_data):
    # Check if data is available
    if not match_data:
        return "No data available to make a prediction."

    predictions = []

    for match in match_data:
        home_team = match['homeTeam']
        away_team = match['awayTeam']
        home_stats = match['homeTeamStats']
        away_stats = match['awayTeamStats']

        # Simple logic for predicting a match outcome
        if home_stats.get('wins', 0) > away_stats.get('wins', 0):
            prediction = f"Prediction: {home_team} to win against {away_team}."
        else:
            prediction = f"Prediction: {away_team} to win against {home_team}."

        # Example logic for over/under goals
        total_goals = home_stats.get('goals', 0) + away_stats.get('goals', 0)
        if total_goals > 2.5:
            prediction += " Expect over 2.5 goals."
        else:
            prediction += " Expect under 2.5 goals."

        predictions.append(prediction)

    return predictions

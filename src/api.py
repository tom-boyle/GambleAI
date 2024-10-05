import requests

def fetch_match_data():
    # Replace with your actual SofaScore API key and the correct endpoint
    api_key = 'your_api_key'
    url = 'https://api.sofascore.com/v1/soccer/matches/date/2024-10-05'

    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # Filter and return relevant match data, such as team stats
        matches = []
        for match in data['matches']:
            if 'Liverpool' in match['homeTeam']['name'] or 'Crystal Palace' in match['awayTeam']['name']:
                matches.append({
                    "homeTeam": match['homeTeam']['name'],
                    "awayTeam": match['awayTeam']['name'],
                    "homeTeamStats": match.get('homeTeamStats', {}),
                    "awayTeamStats": match.get('awayTeamStats', {}),
                    "date": match['startTime'],
                })
        return matches

    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return None
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

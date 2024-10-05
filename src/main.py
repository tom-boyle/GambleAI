from src.api import fetch_match_data
from src.prediction import generate_prediction

def main():
    # Fetch match data
    match_data = fetch_match_data()

    # Generate and print predictions
    predictions = generate_prediction(match_data)
    for prediction in predictions:
        print(prediction)

if __name__ == "__main__":
    main()


# Gambler AI – Sports Betting Recommendation System

**Gambler AI** is a sports betting recommendation system that uses live data from the **SofaScore API** to generate predictions for football matches. The AI analyzes recent team performance, head-to-head matchups, and other key stats to provide betting tips in real time. This project was developed live, in one night, and tested during the ongoing football matches on October 5, 2024.

## Project Overview

The goal of Gambler AI is to help users make more informed betting decisions by using AI-driven insights. The system will eventually be expanded to cover multiple sports, but for tonight’s live build, we are focusing on English Premier League (EPL) matches.

### Features
- Real-time data fetching from SofaScore API.
- Predicts match outcomes based on team form and performance.
- Provides betting tips (win/loss, over/under goals).
- Integrated with Discord for future expansion (coming soon).

## How It Works

1. **Data Collection**: Gambler AI fetches live data from the SofaScore API for upcoming football matches.
2. **Data Processing**: The AI processes recent team stats, goals, and head-to-head performance.
3. **Prediction**: Based on the data, the AI generates a betting recommendation (e.g., "Liverpool win, over 2.5 goals").
4. **Live Testing**: Tonight, Gambler AI's predictions will be tested in real-time during EPL matches.

## Tech Stack

- **Python**: Core programming language.
- **SofaScore API**: Data source for live football stats.
- **Tweepy (Twitter Integration)**: For sharing real-time predictions on Twitter.
- **Discord Bot (Coming Soon)**: Will deliver betting tips to subscribers in a Discord server.

## Follow Along

This project is being developed live and promoted tonight. Follow the progress on [Twitter]([https://twitter.com/your-twitter-handle](https://x.com/tomlikestocode/status/1842511866494685453) where I’ll be sharing updates and predictions as the matches unfold.

### To Do:
- [x] SofaScore API integration
- [ ] Basic prediction model
- [ ] Discord bot integration
- [ ] Subscription model setup

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tom-boyle-au/gambler-ai.git
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the AI**:
   ```bash
   python main.py
   ```

4. **Twitter Integration (Optional)**:
   To enable Twitter integration, add your API keys to `config.py` and use the `tweet_update()` function to post predictions live.

## Roadmap

- **Tonight**: Focus on EPL matches for testing and live predictions.
- **Upcoming**: Expand to other sports and integrate a subscription model for premium tips via Discord.

## License

This project is licensed under the MIT License.

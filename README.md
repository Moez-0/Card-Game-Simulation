# Card Game Simulation
![image](https://github.com/Moez-0/Card-Game-Simulation/assets/86966266/3b07568f-a368-46b0-bd02-e30881c8d672)

This Python code simulates several card games using Monte Carlo simulations. The code defines a set of card games and calculates the win probability and expected winnings per play for each game. 

## Table of Contents
- [Game Descriptions](#game-descriptions)
- [Simulation Results](#simulation-results)
- [Usage](#usage)
- [Requirements](#requirements)
- [License](#license)

## Game Descriptions

The code simulates the following card games:

1. **Sahara Ace**: A game where you draw a card, and if it's an Ace, you win.
2. **Tunisian Twins**: A game where you draw two cards, and to win, they must have the same rank and suit.
3. **Medina Biggie**: A game where you draw two cards, and to win, the second card must have a higher rank than the first.
4. **Desert Hearts**: A game where you draw three cards, and you win for each Hearts suit card drawn.
5. **Oasis Runny**: A game where you draw five cards and win if you find a subset of three or more cards with consecutive ranks.
6. **Student Game**: A game where you draw two cards, and to win, they must have the same suit.

## Simulation Results

Here are the results of running simulations for each game with 100,000 iterations:

- **Sahara Ace**:
   - Win Probability: 7.72%
   - Expected Winnings per Play: 0.77 Dinars per play

- **Tunisian Twins**:
   - Win Probability: 0.0%
   - Expected Winnings per Play: 0.0 Dinars per play

- **Medina Biggie**:
   - Win Probability: 47.05%
   - Expected Winnings per Play: 0.94 Dinars per play

- **Desert Hearts**:
   - Win Probability: 58.81%
   - Expected Winnings per Play: 0.75 Dinars per play

- **Oasis Runny**:
   - Win Probability: 35.77%
   - Expected Winnings per Play: 1.79 Dinars per play

- **Student Game**:
   - Win Probability: 23.36%
   - Expected Winnings per Play: 2.34 Dinars per play

## Usage

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Run the code by executing the `main.py` script. You'll be prompted to enter the number of iterations for the simulations.
4. The code will calculate and display the win probability and expected winnings per play for each game.

## Requirements

- Python 3.x

## License

This code is available under the [MIT License](LICENSE).

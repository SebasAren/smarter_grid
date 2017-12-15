# smarter_grid

Authors: Casper van Velzen, Jelle den Haan, Sebastiaan Arendsen

## Description
placeholder: http://heuristieken.nl/wiki/index.php?title=SmartGrid

## Installation

### Requirements
* Python 3.6.3
* pip 9.0.1

### Python packages
run: pip install -r requirements.txt

## Usage

### Hill Climber
run: python main.py hill 1/2/3 [iterations]

### Simulated Annealing
run: python main.py sim 1/2/3 [cooling scheme] [iterations] [extra]

Cooling schemes:
* interest: inter (extra: interest rate)
* log: ln
* damped oscillator: damp
* linear: lin
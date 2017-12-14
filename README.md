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
run: python main.py wijk1/wijk2/wijk3 hillclimber

### Simulated Annealing
run: python main.py wijk1/wijk2/wijk3 sim [cooling scheme]

Cooling schemes:
* exponential: ex
* power: pow
* log: ln
* dampened oscillator: damp

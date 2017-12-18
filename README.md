# smarter_grid

## Description of the case
The goal of this case is to connect houses to batteries. There are 3 departments, each one contains 5 batteries 
and 150 houses. Every house has a unique output and every battery has a fixed capacity. The goal is to connect the 
houses to the batteries with cables, without exceding the capacity of the battery. Connecting cables is expensive. 
Therefore, connecting all the houses with a minimum number of cables is desired. Later on, batteries can be placed at different positions and different kind of batteries can be used. For more information about the Smart grid case, click on the link below:
http://heuristieken.nl/wiki/index.php?title=SmartGrid

## Installation

### Requirements
* Python 3.6.3
* pip 9.0.1

### Python packages
run: pip install -r requirements.txt

## Layout

### smarter_grid
the whole project can be found in the map smarter_grid, the map contains a couple of other maps and files

### data
all data that is needed to run the code can be found in the map data

### grids
the grids map contains the visualizations of the network cables 

### sim_plots
the visualizations of the score functions can be found in the map sim_plots

### src
the actual code, including main.py can be found in the src map. This map contains two other maps, one for the algorithms and one 
for the visualizations. 

## Usage

### Hill Climber
run: python main.py hill 1/2/3 [iterations]

### Example
python main.py hill 3 55000

### Simulated Annealing
run: python main.py sim 1/2/3 [cooling scheme] [iterations] [extra]

### Example
python main.py sim 2 ln 55000

Cooling schemes:
* exponential: interest (extra: interest rate; needs interest rate to work)
* log: ln
* damped oscillator: damp
* linear: lin


## Authors: 
Sebastiaan Arendsen
Jelle den Haan
Casper van Velzen
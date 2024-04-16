# README

## Bertrand Paradox Simulation

This Python code simulates Bertrand's paradox, a classic problem in probability theory and geometric probability. The paradox revolves around the question of how to properly define the probability of randomly selecting a chord of a circle that is longer than a side of an inscribed equilateral triangle. The paradox arises because there are different interpretations of what constitutes a "randomly selected" chord.

## How to Run the Code:

### Prerequisites:

- `Python 3` should be installed on your system.
- Required Python packages: `matplotlib`, `numpy`.

### Installing matplotlib and numpy
- Depending on your operating system, open a terminal (Linux/Mac) or command prompt (Windows).
- Run the following: 
pip install numpy 
pip install matplotlib
- Verify the installation:
import numpy
import matplotlib
### Running the Code:

1. Save the provided Python code in a file, e.g., `bertrand_simulation.py`.
2. Open your terminal.
3. Navigate to the directory where `bertrand_simulation.py` is saved.
4. Run the code using the command: `python3 bertrand_simulation.py`.
5. A `plots.png` file is created in the same directory. Open this file to see the plots of different strategies.

## Understanding the Code:

- The code is organized into a Python class named `Bertrand`, which encapsulates the simulation methods and plotting functions.
- Three methods are implemented to simulate different approaches to selecting random chords:
  - Method 1: Randomly select one endpoint of the chord on the circle's circumference and test if it forms a chord longer than the triangle's side.
  - Method 2: On the radius joining the center of the circle and one of the triangle vertices, choose a point and draw a chord perpendicular to the radius passing through this point. Test if this chord is longer than the triangle's side.
  - Method 3: Randomly select a point in the circle. Test if this point lies inside the incircle of the equilateral triangle. 
- Each method generates random points or chords and evaluates whether they satisfy the condition of being longer than the side of the inscribed equilateral triangle.
- The results are plotted using `matplotlib`, with each method's simulation results displayed in separate subplots.
- Green lines/points represent chords longer than the triangle's side, while red lines/points represent chords that are not.

## Output:

- After running the code, the program will display the simulation results in three subplots, each illustrating one method's outcomes.
- The console will print the ratio of favorable outcomes to the total number of simulations for each method.
- Additionally, the plots will be saved as `plots.png` in the current directory.

## Interpreting the Results:

- The simulation results demonstrate the different probabilities obtained through each method, highlighting Bertrand's paradox.
- We can observe how the probability of selecting a chord longer than the side of the equilateral triangle varies depending on the method of selection.

## Note:

- Adjustments to parameters such as the number of iterations (`self.n`) or the radius of the circle (`self.r`) can be made within the code to modify the simulation behavior.
## Team-members:

- Apoorv Tandon (220192)
- Daksh Kumar Singh (220322)
- Himanshu Shekhar (220454)
- Swayamsidh Pradhan (221117)
- Tanishq Maheshwari (221128)

# Bayesian Analysis with Beta-Binomial Model

This Python code calculates the posterior distribution of a Beta-Binomial model and plots it using Tkinter for user interaction and Matplotlib for visualization.

## How to Run the Code

### Prerequisites

- Python 3 should be installed on your system.
- Required Python packages: `tkinter`, `numpy`, `matplotlib`, `scipy`.

### Installing required packages

Depending on your operating system, open a terminal (Linux/Mac) or command prompt (Windows) and run the following commands:
```
pip install tkinter
pip install numpy
pip install matplotlib
pip install scipy
```
### Running the Code

1. Save the provided Python code in a directory.
2. Open your terminal or command prompt.
3. Navigate to the directory where the file is saved.
4. Run the code using the command: `python3 Bayesian_Analysis.py`.
5. The program will open a Tkinter window.
6. Enter the alpha and beta prior values in the respective entry fields.
7. Click on the "Plot Posterior" button to visualize the posterior distribution.
8. The plot will display the prior and posterior distributions, along with Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP) estimates.

## Understanding the Code

### Functions

1. **`plot_default()`:**
   - Plots the posterior distributions for four predefined sets of prior parameters.
   - Calculates the number of heads and tails from the observed data.
   - Calculates the posterior distributions for each set of prior parameters.
   - Plots the posterior distributions, MLE, and MAP estimates.

2. **`plot_posterior()`:**
   - Calculates the posterior distribution based on user-provided alpha and beta prior values.
   - Plots the prior and posterior distributions using Matplotlib.
   - Calculates and plots the Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP) estimates.

### Variables

- `observed_data`: Represents the observed data used for inference.

### Tkinter GUI

- Creates a Tkinter window with entry fields for alpha and beta prior values.
- Provides a button to trigger the plotting of the posterior distribution.

## Code Execution

- Upon running the script, a Tkinter window opens.
- Users can input alpha and beta prior values.
- Clicking on the "Plot Posterior" button generates the posterior distribution plot.

## Output

- The program outputs a graphical representation of the prior and posterior distributions.
- It also displays MLE and MAP estimates on the plot.

## Interpreting the Results

- Users can observe how the prior distribution is updated to the posterior distribution based on observed data.
- MLE and MAP estimates provide point estimates based on the data and prior information.

## Note

- Ensure that the observed data and parameter inputs are appropriate for your specific use case.
- Users can modify the observed data and prior parameters according to their needs.
- For any issues or further inquiries, please refer to the code comments or contact the developer team.
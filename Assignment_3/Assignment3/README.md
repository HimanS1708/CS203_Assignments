# Monty Hall Simulation

This Python code simulates the Monty Hall Problem, a probability puzzle. It assesses the probability of winning for switching (W) versus sticking (T) to the original decision.

## How to Run the Code

Prerequisites:

- Python 3 should be installed on your system.
- Required Python packages: numpy, matplotlib.

__Installing numpy and matplotlib:__

- Depending on your operating system, open a terminal (Linux/Mac) or command prompt (Windows).
- Run the following commands:
    ```
    pip install numpy
    pip install matplotlib
    ```

- Verify the installation:
    ```
    import numpy
    import matplotlib
    ```

__Running the Code:__

1. Unzip the zip file.
2. Open your terminal or command prompt.
3. Navigate to the directory where monty_hall_simulation.py is saved.
4. Run the code using the command: ```python3 monty_hall_simulation.py```.
5. The program will open a tkinter window and prompt you to enter the number of doors (n), the number of doors with cars (k), and the number of samples.
6. After entering the values, click the "Run Simulation" button.
7. The program will display the probability of winning for switching and sticking, along with surface plots illustrating the relationship between n, k, and the ratio of P(win|W) to P(win|T).
8. To exit, close the plot and tkinter window.

## Understanding the Code:

1. __simulate(n, k, samples):__

    - This function simulates the Monty Hall Problem for a given number of doors (n) and a given number of doors with cars (k). It runs the simulation for a specified number of samples and calculates the number of wins for both switching and sticking strategies and returns the number of wins for both cases.

2. __run_simulation():__

    - This function is called when the user clicks the "Run Simulation" button in the Tkinter GUI. It reads the values entered by the user for the number of doors (n), the number of doors with cars (k), and the number of samples. Then, it calls the simulate function to run the simulation with these parameters. Finally, it updates the Tkinter labels to display the results of the simulation.

3. __plot_simulation():__

    - This function generates surface plots illustrating the probability ratios for different configurations of n and k. It uses matplotlib to create the plots and numpy to calculate the probability ratios. It plots the probability ratios for varying values of n (number of doors) and k (number of doors with cars) on two separate subplots.

4. __mainloop():__

    - This function starts the Tkinter event loop, which listens for events such as button clicks and updates to the GUI elements. It keeps the GUI responsive and interactive.
  
    - These functions work together to simulate the Monty Hall Problem, display the results in the Tkinter GUI, and generate surface plots to visualize the probability ratios.

__Output:__

- The program outputs the probabilities of winning for switching and sticking, along with surface plots illustrating the relationship between n, k, and the probability ratio.
- The plots provide insights into how the probability ratio (P(win|W) / P(win|T)) changes with different values of n and k.

__Interpreting the Results:__

- Users can observe how the probability ratio (P(win|W) / P(win|T)) changes with different values of n and k.
- From this plot, we could infer the conditions under which switching is more advantageous than sticking, and vice versa.
- The probability of winning when switching is always higher than the probability of winning when sticking.
- This is because switching takes advantage of the host's revelation, which provides additional information that can be used to make a more informed decision. 
- Mathematically, the probability of winning under no switch is $k/n$ and under switch is $k(n-1)/n(n-2)$. So the ratio $P(win|W)/P(win|T)$ is $(n-1)/(n-2)$ which is independent of $k$. This result can also be seen in the plots where the variation with $k$ is almost negligible and for variation with $n$, as $n$ takes up large values the ratio tends to $1$.

Note:
- Users can modify parameters such as the number of doors, the number of doors with cars, and the number of samples to analyze different scenarios.


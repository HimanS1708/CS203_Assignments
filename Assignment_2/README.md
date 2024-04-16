# README

## Birthday Paradox Calculator

This Python code calculates the probability of two people sharing the same birthday within a group, also known as the birthday paradox. The paradox highlights the counterintuitive nature of probability when considering a relatively small group of people.

## How to Run the Code:

### Prerequisites:

- `Python 3` should be installed on your system.
- Required Python packages: `matplotlib`.

### Installing matplotlib and numpy
- Depending on your operating system, open a terminal (Linux/Mac) or command prompt (Windows).
- Run the following: ```pip install matplotlib```
- Verify the installation: ```import matplotlib```


### Running the Code:

1. Save the provided Python code in a file, e.g., `birthday_paradox.py`.
2. Open your terminal.
3. Navigate to the directory where `birthday_paradox.py` is saved.
4. Run the code using the command: `python3 birthday_paradox.py`.
5. The program will prompt you to enter a probability value (between 0 and 1).
6. It will then calculate and display the minimum number of people needed for the given probability of two people sharing the same birthday.
7. The program will generate a plot illustrating the relationship between the number of people and the corresponding probabilities.
8. To exit, enter `-1` when prompted for the probability.

## Understanding the Code:

1. **myfunc(students):**
   - Computes the difference between logarithmic values to determine the probability of two students not sharing a birthday in a group of a specified size.

2. **myfunc1():**
   - Iterates through a range of possible group sizes(0-365) and computes the probability using the `myfunc()` function.
   - Stores the calculated probabilities in a list for future reference.

3. **myfunc2(probability):**
   - Determines the minimum number of people needed for a given probability of shared birthdays.
   - Utilizes the stored probabilities and iterates to find the minimum number of people satisfying the condition.

4. **myfunc3():**
   - Computes probabilities for various group sizes using the `myfunc()` function.
   - Generates a plot illustrating the relationship between the number of people and the corresponding probabilities.

5. **main():**
   - Orchestrates the flow of the program.
   - Calls `myfunc1()` and `myfunc3()` to compute probabilities and generate plot.
   - Prompts the user to input a desired probability and calculates the minimum number of people needed accordingly using `myfunc2()`.

### Code Execution:

- Upon running the script, it prompts the user to enter a probability value between 0 and 1.
- It then calculates and displays the minimum number of people needed for the specified probability.
- The program generates a plot depicting how the probability changes with the number of people in the group.

## Output:

- The program outputs the minimum number of people required for a specified probability of shared birthdays.
- It generates a plot depicting how the probability changes with the number of people in the group.
- The plots are saved as `plots.png` in the current directory for future reference.

## Interpreting the Results:

- Users can observe how the probability of shared birthdays increases as the group size grows.
- Also an important observation is that a group a size of only 23 members leads to a 50% probability that two members of the group will share the same birthday.
- This demonstrates the counterintuitive nature of the Birthday Paradox, where a relatively small number of people can lead to a high likelihood of shared birthdays.

## Note:

- Users can modify parameters such as the desired probability or the range of people to analyze by adjusting input values or code variables.
- For any issues or further inquiries, please refer to the code comments or contact the developer team.

## Team-members:

- Apoorv Tandon (220192)
- Daksh Kumar Singh (220322)
- Himanshu Shekhar (220454)
- Swayamsidh Pradhan (221117)
- Tanishq Maheshwari (221128)

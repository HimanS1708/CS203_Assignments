import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import StringVar, Label, Tk, Entry, Button

def simulate(n, k, samples):
    same_choice_wins = 0
    switched_choice_wins = 0
    for _ in range(samples):
        doors = ["car"] * k + ["goat"] * (n - k)
        random.shuffle(doors)
        first_choice = random.randint(0, n - 1)
        show = random.randint(0, n - 1)
        while show == first_choice:
            show = random.randint(0, n - 1)
        if doors[first_choice] == "goat":
            if doors[show] == "goat":
                same_choice_wins += 1
            else:
                switched_choice_wins += 1
        else:
            if doors[show] == "car":
                switched_choice_wins += 1
    return same_choice_wins / samples, switched_choice_wins / samples

def plot_simulation():
    plt.figure(figsize=(12, 6))

    # Create a 3D plot
    ax = plt.subplot(1, 2, 1, projection='3d')

    # Create a meshgrid for n and k values
    N, K = np.meshgrid(n_values, k_values)

    # Calculate the success ratio for each combination of n and k
    X, Y = N.ravel(), K.ravel()
    Z = np.zeros(X.shape)
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            z1, z2 = simulate(int(x), int(y), 50)
            Z[i] = (z1 + z2) / 2

    # Reshape Z to a 2-dimensional array
    Z = Z.reshape(N.shape)

    # Plot the surface
    ax.plot_surface(N, K, Z, cmap='viridis')
    ax.set_xlabel('Number of Doors (n)')
    ax.set_ylabel('Number of Cars (k)')
    ax.set_zlabel('Success Ratio')
    ax.set_title('Variation with n and k')

    # Create a 2D plot for the variation with n
    plt.subplot(1, 2, 2)
    for k in k_values:
        win_ratios_n = [simulate(n, k, 50)[1] / simulate(n, k, 50)[0] for n in n_values]
        plt.plot(n_values, win_ratios_n, label=f"k = {k}")
    plt.ylabel("P(win|W) / P(win|T)")
    plt.xlabel("Number of Doors (n)")
    plt.title("Variation with n")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Tkinter GUI setup
n_values = np.arange(3, 20)
k_values = np.arange(1, 6)
window = Tk()
window.geometry("400x300")
window.title("Monty Hall Simulation")
window.resizable(0, 0)

same_choice = StringVar()
switched_choice = StringVar()
same_choice.set(0)
switched_choice.set(0)

Label(text="Same choice").place(x=80, y=8)
Label(text="Switched choice").place(x=80, y=40)
Label(textvariable=same_choice, font=(15)).place(x=180, y=8)
Label(textvariable=switched_choice, font=(15)).place(x=180, y=40)

Label(window, text="Number of Doors (n):").place(x=10, y=80)
Label(window, text="Number of Cars (k):").place(x=10, y=110)

n_value = Entry(window)
n_value.place(x=150, y=80)

k_value = Entry(window)
k_value.place(x=150, y=110)

no_sample = Entry(window)
no_sample.place(x=150, y=140)

Label(window, text="Number of Samples:").place(x=10, y=140)

run_button = Button(window, text="Run Simulation", command=plot_simulation)
run_button.place(x=300, y=135)

window.mainloop()
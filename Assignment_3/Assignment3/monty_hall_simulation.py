import random
import numpy as np
import matplotlib.pyplot as plt
from tkinter import StringVar, Label, Tk, Entry, Button

def simulate(n, k, samples):
    same_choice_wins = 0
    switched_choice_wins = 0
    for __ in range(samples):
        doors = ["car"] * k + ["goat"] * (n - k)
        random.shuffle(doors)
        ind = np.arange(0,n)

        # Players choice
        first_choice = np.random.choice(ind)

        # The host now opens one of the unchosen doors that contains goat
        if(len([x for x in ind if x != first_choice and doors[x]=="goat"])==0):
            return 1, 1
        show = np.random.choice([x for x in ind if x != first_choice and doors[x]=="goat"])

        # First case when the player does not switch
        if(doors[first_choice]=="car"):
            same_choice_wins+=1
        
        # Second case when the player switches
        second_choice = np.random.choice([x for x in ind if x!=first_choice and x!=show])
        if(doors[second_choice]=="car"):
            switched_choice_wins+=1
    
    return same_choice_wins, switched_choice_wins

def run_simulation():
    samples = int(no_sample.get())
    n = int(n_value.get())
    k = int(k_value.get())
    if(n==k+1):
        same_choice_result = k/n
        switched_choice_result = 1
    else:
        same_choice_result, switched_choice_result = simulate(n, k, samples)
        same_choice_result /= samples
        switched_choice_result /= samples
    same_choice.set(same_choice_result)
    switched_choice.set(switched_choice_result)
    plot_simulation()

def plot_simulation():

    ax = plt.axes(projection="3d")

    X, Y = np.meshgrid(n_values, k_values)
    size = X.shape[0]
    win1 = 0
    win2 = 0
    Hratio=np.zeros((size,size))
    for i in range(size):
        for j in range(size):
            result = simulate(X[i][j],Y[i][j],500)
            win1 += result[1]
            win2 += result[0]
            if(win2==0): Hratio[i][j]=100000000000
            else: Hratio[i][j]=win1/win2

    ax.plot_surface(X, Y, Hratio, cmap="plasma")
    ax.set_xlabel("Number of cars(k)")
    ax.set_ylabel("Number of doors(n)")
    ax.set_zlabel("P(win|W) / P(win|T)")
    plt.title("Variation of P(win|W)/P(win|T) with n and k")
    plt.show()

# Tkinter GUI setup
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

run_button = Button(window, text="Run Simulation", command=run_simulation)
run_button.place(x=150, y=205)

# Values for plotting
n_values = range(3, 20)
k_values = range(1, 18)

window.mainloop()

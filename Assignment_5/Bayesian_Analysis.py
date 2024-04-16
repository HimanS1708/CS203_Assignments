import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

def plot_default():
    priors = [(2, 5), (5, 2), (1, 1), (2, 2)]
    prior_labels = ['Beta(2,5)', 'Beta(5,2)', 'Beta(1,1)', 'Beta(2,2)']

    # Calculate the number of heads and tails from the data
    num_heads = sum(1 for toss in observed_data if toss == 'H')
    num_tails = len(observed_data) - num_heads

    # Calculate posterior distributions
    posterior_params = [(prior[0] + num_heads, prior[1] + num_tails) for prior in priors]

    pastel_colors = ['#FFD1DC', '#BDFCC9', '#AEEEEE', '#C8A2C8']

    # Plot posterior distributions for each case
    x = np.linspace(0, 1, 100)

    plt.figure(figsize=(12, 10))

    for i, params in enumerate(posterior_params):
        posterior_dist = beta(params[0], params[1])
        plt.subplot(2, 2, i+1)
        # plt.fill_between(x, posterior_dist.pdf(x), color=pastel_colors[i])
        plt.plot(x, posterior_dist.pdf(x), label=prior_labels[i], color=pastel_colors[i], linewidth=2)

        # Maximum Likelihood Estimation (MLE)
        mle = num_heads / (num_heads + num_tails)
        plt.axvline(x=mle, color='black', linestyle='--', label='MLE')

        # Maximum A Posteriori (MAP) estimates
        map_estimate = (params[0] - 1) / (params[0] + params[1] - 2)
        plt.axvline(x=map_estimate, color='red', linestyle='-.', label='MAP')

        plt.title(f'Posterior Distribution: {prior_labels[i]}', fontsize=12)
        plt.xlabel('Bias', fontsize=10)
        plt.ylabel('Density', fontsize=10)
        plt.legend(prop={'size': 8})
        plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig("plots.png")
    plt.clf()

def plot_posterior():
    try:
        # Get alpha and beta prior values from entry fields
        alpha_prior = float(alpha_entry.get())
        beta_prior = float(beta_entry.get())
        
        # Check if alpha and beta are positive real numbers
        if alpha_prior <= 0 or beta_prior <= 0:
            messagebox.showerror("Error", "Alpha and beta must be positive real numbers.")
            return

        # Calculate the number of heads and tails from the data
        num_heads = sum(1 for toss in observed_data if toss == 'H')
        num_tails = len(observed_data) - num_heads

        # Calculate alpha and beta parameters for the posterior distribution
        alpha_posterior = alpha_prior + num_heads
        beta_posterior = beta_prior + num_tails

        # Generate x values for plotting
        x = np.linspace(0, 1, 1000)

        # Plot the prior distribution
        prior = beta.pdf(x, alpha_prior, beta_prior)
        plt.plot(x, prior, label='Prior', color='red')
        
        # Plot the posterior distribution
        posterior = beta.pdf(x, alpha_posterior, beta_posterior)
        plt.plot(x, posterior, label='Posterior', color='blue')

        # Calculate MLE and MAP estimates
        alpha_mle = num_heads
        beta_mle = num_tails
        mle_estimate = alpha_mle / (alpha_mle + beta_mle)

        alpha_map = alpha_posterior
        beta_map = beta_posterior
        map_estimate = (alpha_map - 1) / (alpha_map + beta_map - 2)

        # Plot lines for MLE and MAP estimates
        plt.axvline(x=mle_estimate, linestyle='--', color='green', label='MLE Estimate')
        if map_estimate >= 0 and map_estimate <= 1:
            plt.axvline(x=map_estimate, linestyle='--', color='red', label='MAP Estimate')
        else:
            messagebox.showwarning("Warning", "MAP estimate is not between 0 and 1. Mode at boundary.")
        
        plt.xlabel('Probability of Heads')
        plt.ylabel('Density')
        plt.title('Posterior Distribution')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Input must be a number.")

observed_data = ['H', 'H', 'H', 'T', 'T', 'T', 'H', 'H', 'H', 'T']  # Observed data

def main():
    plot_default()

if __name__ == '__main__':
    main()

# Create Tkinter window
root = tk.Tk()
root.title("Posterior Distribution Plot")

# Create alpha prior label and entry field
alpha_label = ttk.Label(root, text="Alpha Prior:")
alpha_label.grid(row=0, column=0, padx=50, pady=20)
alpha_entry = ttk.Entry(root)
alpha_entry.grid(row=0, column=1, padx=50, pady=20)

# Create beta prior label and entry field
beta_label = ttk.Label(root, text="Beta Prior:")
beta_label.grid(row=1, column=0, padx=50, pady=20)
beta_entry = ttk.Entry(root)
beta_entry.grid(row=1, column=1, padx=50, pady=20)

# Create button to plot posterior distribution
plot_button = ttk.Button(root, text="Plot Posterior", command=plot_posterior)
plot_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
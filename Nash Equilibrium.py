import numpy as np
from scipy.optimize import linprog

# Define the payoff matrix for two players (Player A and Player B)
# Each player has two strategies: Buy (B) and Sell (S)
payoff_matrix_A = np.array([[1, -1],
                            [-1, 1]])  # Payoff matrix for Player A

payoff_matrix_B = np.array([[1, -1],
                            [-1, 1]])  # Payoff matrix for Player B (negative of Player A's)

# Combine the payoff matrices into one for linear programming
c = np.zeros(4)  # Objective function coefficients (not used)
A_eq = np.array([[1, 1, 0, 0],
                 [0, 0, 1, 1],
                 [1, 0, 1, 0],
                 [0, 1, 0, 1]])  # Constraints for probabilities summing to 1 and strategies
b_eq = np.array([1, 1, 0, 0])  # Right-hand side of the constraints

# Solve the linear programming problem to find the mixed strategy Nash Equilibrium
res = linprog(c, A_eq=A_eq, b_eq=b_eq, method='simplex')
mixed_strategy = res.x[:2]  # Mixed strategy probabilities for Player A

print("Mixed Strategy Nash Equilibrium for Player A:")
print("Probability of Buy:", mixed_strategy[0])
print("Probability of Sell:", mixed_strategy[1])

# Assuming the mixed strategy for Player B is the same
mixed_strategy_B = mixed_strategy

# Predict the stock price movement based on the mixed strategy
if mixed_strategy[0] > mixed_strategy[1]:
    prediction = "Stock price likely to increase"
else:
    prediction = "Stock price likely to decrease"

print("Prediction for Nifty50 stock price movement:", prediction)

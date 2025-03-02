from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
from scipy.optimize import minimize
from scipy.optimize import minimize, linprog


df = pd.read_csv("tco_dataset.csv")
features = ["procurement_cost", "operational_cost", "Usage_Per_Hour_Per_Day"]
target = "Total_Cost"
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")


# Function for TCO optimization
def optimize_tco():
    def objective_function(x):
        procurement_cost = x[0]
        operational_cost = x[1]
        return procurement_cost + operational_cost

    constraints = {"type": "ineq", "fun": lambda x: x[0] + x[1] - 1000}  # Example constraint
    result = minimize(objective_function, x0=[500, 500], constraints=constraints)
    print("Optimal TCO solution:", result.x)


# ------------------------- Bandwidth Allocation Module -------------------------

# Function for bandwidth allocation optimization
def optimize_bandwidth():
    # Define the cost coefficients for bandwidth allocation
    cost = [1, 2, 3]  # Example: Device 1 is cheaper than Device 3

    # Define the inequality constraints matrix
    A = [[1, 1, 1]]  # x1 + x2 + x3 <= 100

    # Define the inequality constraints vector
    b = [100]  # Total bandwidth limit

    # Define the bounds for each variable
    x_bounds = [(10, None), (10, None), (10, None)]

    # Solve the optimization problem
    result = linprog(cost, A_ub=A, b_ub=b, bounds=x_bounds, method="highs")

    # Print the results
    if result.success:
        print("Optimal bandwidth allocation:")
        print(f"Device 1: {result.x[0]:.2f} units")
        print(f"Device 2: {result.x[1]:.2f} units")
        print(f"Device 3: {result.x[2]:.2f} units")
        print(f"Total cost: {result.fun:.2f}")
    else:
        print("Bandwidth optimization failed:", result.message)

# Call the bandwidth allocation optimization function
optimize_bandwidth()



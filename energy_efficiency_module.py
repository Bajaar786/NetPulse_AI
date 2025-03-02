import numpy as np

# Define states and actions
states = ["low_traffic", "medium_traffic", "high_traffic"]
actions = ["reduce_power", "maintain_power", "increase_power"]

# Define rewards
rewards = {
    ("low_traffic", "reduce_power"): 10,  
    ("high_traffic", "reduce_power"): -10,  
    ("medium_traffic", "maintain_power"): 5,  
}

# Network Environment Class
class NetworkEnvironment:
    def __init__(self):
        self.state = "low_traffic"

    def step(self, action):
        if self.state == "low_traffic" and action == "reduce_power":
            reward = 10
            next_state = "low_traffic"
        elif self.state == "high_traffic" and action == "reduce_power":
            reward = -10
            next_state = "high_traffic"
        else:
            reward = 5
            next_state = "medium_traffic"
        return next_state, reward

    def reset(self):
        self.state = "low_traffic"
        return self.state

# ⬇️ The function is now properly placed OUTSIDE the class
def optimize_energy(traffic_load, temperature):
    # Initialize Q-table
    q_table = np.zeros((len(states), len(actions)))

    # Hyperparameters
    alpha = 0.1  # Learning rate
    gamma = 0.9  # Discount factor
    epsilon = 1.0  # Exploration rate
    epsilon_decay = 0.995
    epsilon_min = 0.01

    # Training loop
    env = NetworkEnvironment()
    for episode in range(1000):
        state = env.reset()
        done = False
        steps = 0

        while not done:
            if np.random.rand() < epsilon:
                action = np.random.choice(actions)  # Explore
            else:
                action = actions[np.argmax(q_table[states.index(state)])]  # Exploit

            next_state, reward = env.step(action)
            q_table[states.index(state), actions.index(action)] += alpha * (
                reward + gamma * np.max(q_table[states.index(next_state)]) - q_table[states.index(state), actions.index(action)]
            )
            state = next_state
            steps += 1

            if steps > 10:  # Break after a max number of steps per episode
                done = True

        epsilon = max(epsilon * epsilon_decay, epsilon_min)
    return q_table



# Train the Q-learning model and get the Q-table
q_table = optimize_energy(traffic_load=50, temperature=25)

# Testing the trained Q-table
state = "low_traffic"
action = actions[np.argmax(q_table[states.index(state)])]
print(f"\n🔹 Optimal action for {state}: {action}")


# --- Predictive Maintenance Section ---

# Define backup systems
backup_systems = {
    "Router": "Backup_Router_001",
    "Switch": "Backup_Switch_001",
    "Server": "Backup_Server_001",
}

# Simulate network devices
network_devices = {
    "Router_001": {"status": "working", "traffic_load": 60},
    "Switch_001": {"status": "working", "traffic_load": 40},
    "Server_001": {"status": "working", "traffic_load": 80},
}

# Simulate predictive maintenance output
predictive_maintenance_output = {
    "Router_001": {"maintenance_needed": 1},  # Maintenance needed
    "Switch_001": {"maintenance_needed": 0},  # No maintenance needed
    "Server_001": {"maintenance_needed": 0},  # No maintenance needed
}

# Update network devices status based on predictive maintenance output
for device_name, device_info in network_devices.items():
    if predictive_maintenance_output[device_name]["maintenance_needed"] == 1:
        device_info["status"] = "failed"
    else:
        device_info["status"] = "working"

# Function to check for failures and switch to backup
def switch_to_backup(devices, backups):
    failed_devices = list(devices.keys())  # Create a list of keys to avoid dictionary modification issues
    
    for device_name in failed_devices:
        device_info = devices[device_name]
        if device_info["status"] == "failed":
            print(f"⚠️ {device_name} has failed. Switching to backup...")
            device_type = device_name.split("_")[0]  # Extract device type (e.g., Router, Switch)
            backup_device = backups.get(device_type)
            
            if backup_device:
                print(f"✅ Switching to {backup_device}.")
                # Add backup device only if it doesn't already exist
                if backup_device not in devices:
                    devices[backup_device] = {"status": "working", "traffic_load": device_info["traffic_load"]}
                # Mark failed device as under maintenance
                devices[device_name]["status"] = "under_maintenance"
            else:
                print(f"❌ No backup available for {device_name}.")
    
    return devices


# Function to redistribute traffic
def redistribute_traffic(devices):
    total_traffic = sum(device["traffic_load"] for device in devices.values() if device["status"] == "working")
    num_devices = sum(1 for device in devices.values() if device["status"] == "working")
    avg_traffic = total_traffic / num_devices if num_devices > 0 else 0

    print("\n🔄 Redistributing traffic...")
    for device_name, device_info in devices.items():
        if device_info["status"] == "working":
            device_info["traffic_load"] = avg_traffic
            print(f"📊 {device_name} new traffic load: {avg_traffic:.2f}")

    return devices

# Check for failures and switch to backup
network_devices = switch_to_backup(network_devices, backup_systems)

# Redistribute traffic
network_devices = redistribute_traffic(network_devices)

# Print updated network status
print("\n✅ Final Network Status After Predictive Maintenance and Backup Switching:")
for device_name, device_info in network_devices.items():
    print(f"{device_name}: {device_info}")


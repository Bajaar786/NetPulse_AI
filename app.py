import streamlit as st
from predictive_module import predict_failure
from energy_efficiency_module import optimize_energy
from tco_module import optimize_tco, optimize_bandwidth

# Initialize session state for in-memory data storage
if "network_data" not in st.session_state:
    st.session_state.network_data = []

st.title("PulseNet AI Dashboard")

# Add network data
st.header("Add Network Data")
temperature = st.number_input("Temperature", value=0.0)
usage_percentage = st.number_input("Usage Percentage", value=0.0)
error_rate = st.number_input("Error Rate", value=0.0)
if st.button("Add Data"):
    st.session_state.network_data.append({
        "temperature": temperature,
        "usage_percentage": usage_percentage,
        "error_rate": error_rate
    })
    st.success("Data added successfully!")

# Predict maintenance
st.header("Predict Maintenance")
if st.button("Predict Maintenance"):
    if st.session_state.network_data:
        latest_data = st.session_state.network_data[-1]
        prediction = predict_failure(
            latest_data["temperature"],
            latest_data["usage_percentage"],
            latest_data["error_rate"]
        )
        st.write(f"Prediction: {prediction}")
    else:
        st.warning("No data available. Please add data first.")

# Optimize energy efficiency
st.header("Optimize Energy Efficiency")
traffic_load = st.number_input("Traffic Load", value=0.0)
temperature_energy = st.number_input("Temperature for Energy Optimization", value=0.0)
if st.button("Optimize Energy"):
    recommendation = optimize_energy(traffic_load, temperature_energy)
    st.write(f"Recommendation: {recommendation}")

# Optimize total cost
st.header("Optimize Total Cost")
if st.button("Optimize Cost"):
    optimized_cost = optimize_tco()
    st.write(f"Optimized Cost: {optimized_cost}")

# Optimize bandwidth allocation
st.header("Optimize Bandwidth Allocation")
if st.button("Optimize Bandwidth"):
    result = optimize_bandwidth()
    st.write(f"Optimized Bandwidth: {result}")

# Fetch all data
st.header("Network Data")
if st.button("Fetch Data"):
    if st.session_state.network_data:
        st.write(st.session_state.network_data)
    else:
        st.warning("No data available. Please add data first.")
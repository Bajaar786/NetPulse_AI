// src/App.js
import React, { useEffect, useState } from "react";
import axios from "axios";

const App = () => {
    const [networkStatus, setNetworkStatus] = useState({});
    const [resourceAllocation, setResourceAllocation] = useState(null);

    // Function to fetch network status
    const fetchNetworkStatus = async () => {
        try {
            const response = await axios.get("http://localhost:5000/api/network-status");
            setNetworkStatus(response.data);
        } catch (error) {
            console.error("Error fetching network status:", error);
        }
    };

    // Function to fetch resource allocation
    const fetchResourceAllocation = async () => {
        try {
            const response = await axios.get("http://localhost:5000/api/optimize-resources");
            setResourceAllocation(response.data);
        } catch (error) {
            console.error("Error fetching resource allocation:", error);
        }
    };

    useEffect(() => {
        // Fetch network status immediately
        fetchNetworkStatus();

        // Fetch network status every 5 seconds
        const networkInterval = setInterval(fetchNetworkStatus, 5000);

        // Fetch resource allocation immediately
        fetchResourceAllocation();

        // Fetch resource allocation every 10 seconds
        const resourceInterval = setInterval(fetchResourceAllocation, 10000);

        // Cleanup intervals on component unmount
        return () => {
            clearInterval(networkInterval);
            clearInterval(resourceInterval);
        };
    }, []);

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-4">SmartNet AI Dashboard</h1>

            <h2 className="text-xl font-bold mb-4">Network Status</h2>
            <table className="w-full border-collapse border border-gray-300 mb-8">
                <thead>
                    <tr className="bg-gray-200">
                        <th className="border border-gray-300 p-2">Device</th>
                        <th className="border border-gray-300 p-2">Status</th>
                        <th className="border border-gray-300 p-2">Traffic Load</th>
                    </tr>
                </thead>
                <tbody>
                    {Object.entries(networkStatus).map(([device, info]) => (
                        <tr key={device} className="hover:bg-gray-100">
                            <td className="border border-gray-300 p-2">{device}</td>
                            <td className="border border-gray-300 p-2">{info.status}</td>
                            <td className="border border-gray-300 p-2">{info.traffic_load}</td>
                        </tr>
                    ))}
                </tbody>
            </table>

            <h2 className="text-xl font-bold mb-4">Optimal Resource Allocation</h2>
            {resourceAllocation ? (
                <div>
                    <p>Device 1: {resourceAllocation.optimal_allocation.Device_1.toFixed(2)} units</p>
                    <p>Device 2: {resourceAllocation.optimal_allocation.Device_2.toFixed(2)} units</p>
                    <p>Device 3: {resourceAllocation.optimal_allocation.Device_3.toFixed(2)} units</p>
                    <p>Total cost: {resourceAllocation.total_cost.toFixed(2)}</p>
                </div>
            ) : (
                <p>Loading resource allocation...</p>
            )}
        </div>
    );
};

export default App;

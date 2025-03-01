// src/components/Sidebar.js
import React from "react";

const Sidebar = () => {
    return (
        <aside className="bg-gray-800 text-white w-64 p-4">
            <ul>
                <li className="mb-2"><a href="#predictive-maintenance">Predictive Maintenance</a></li>
                <li className="mb-2"><a href="#energy-efficiency">Energy Efficiency</a></li>
                <li className="mb-2"><a href="#tco">Total Cost Optimization</a></li>
            </ul>
        </aside>
    );
};

export default Sidebar;
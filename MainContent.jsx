// src/components/MainContent.js
import React from "react";
import EnergyChart from "./EnergyChart";
import CostChart from "./CostChart";

const MainContent = () => {
    return (
        <main className="flex-1 p-4">
            <h2 className="text-xl font-bold mb-4">Energy Efficiency</h2>
            <EnergyChart />
            <h2 className="text-xl font-bold mb-4 mt-8">Cost Forecasts</h2>
            <CostChart />
        </main>
    );
};

export default MainContent;
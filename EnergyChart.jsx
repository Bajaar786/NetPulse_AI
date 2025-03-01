// src/components/EnergyChart.js
import React, { useRef, useEffect } from "react";
import Chart from "Chart.js/auto";

const EnergyChart = () => {
    const chartRef = useRef(null);

    useEffect(() => {
        const ctx = chartRef.current.getContext("2d");
        new Chart(ctx, {
            type: "line",
            data: {
                labels: ["00:00", "01:00", "02:00", "03:00", "04:00"],
                datasets: [{
                    label: "Energy Usage (kWh)",
                    data: [0.5, 0.6, 0.4, 0.7, 0.3],
                    borderColor: "blue",
                    fill: false,
                }],
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: true },
                },
            },
        });
    }, []);

    return <canvas ref={chartRef}></canvas>;
};

export default EnergyChart;
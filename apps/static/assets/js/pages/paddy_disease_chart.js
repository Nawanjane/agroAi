// Ensure the DOM is fully loaded before executing the script
document.addEventListener('DOMContentLoaded', function() {
    // Fetch the data for the paddy disease chart from the Flask route
    fetch('/paddy-disease-data')
        .then(response => response.json())
        .then(data => {
            // Call the function to render the chart with the fetched data
            renderPaddyDiseaseChart(data.series, data.labels);
        })
        .catch(error => console.error('Error fetching data:', error));
});

// Function to render the paddy disease donut chart
function renderPaddyDiseaseChart(series, labels) {
    var options = {
        chart: {
            height: 320,
            type: 'donut',
        },
        series: series, // The series data from the Flask route
        labels: labels, // The labels data from the Flask route
        colors: ["#4099ff", "#0e9e4a", "#00bcd4", "#FFB64D", "#FF5370"], // Customize colors as needed
        fill: {
            type: 'gradient',
            gradient: {
                shade: 'light',
                inverseColors: true,
            }
        },
        legend: {
            show: true,
            position: 'bottom',
        },
        plotOptions: {
            pie: {
                donut: {
                    labels: {
                        show: true,
                        name: {
                            show: true
                        },
                        value: {
                            show: true
                        }
                    }
                }
            }
        },
        dataLabels: {
            enabled: true,
            dropShadow: {
                enabled: false,
            }
        },
        responsive: [{
            breakpoint: 480,
            options: {
                legend: {
                    position: 'bottom'
                }
            }
        }]
    };

    // Select the chart container and initialize the chart
    var chart = new ApexCharts(document.querySelector("#pie-chart-2"), options);
    // Render the chart
    chart.render();
}

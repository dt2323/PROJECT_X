var dataPointsCtx = document.getElementById("data-points-chart");

var dataPointsChart = new Chart(dataPointsCtx,{
    type: 'pie',
    data: {
        datasets: [{
            data: [10, 20, 30]
        }],    
        labels: [
            'Red',
            'Yellow',
            'Blue'
        ]
    }
});

var cntributorsCtx = document.getElementById("contributors-chart");

var contributorsChart = new Chart(cntributorsCtx,{
    type: 'pie',
    data: {
        datasets: [{
            data: [10, 20, 30, 50]
        }],    
        labels: [
            'Red',
            'Yellow',
            'Blue',
            'Green'
        ]
    }
});

var categoriesChartCtx = document.getElementById("categories-chart");

var categoriesChart = new Chart(categoriesChartCtx,{
    type: 'bar',
    data: {
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        datasets: [{
            label: 'Categories analysis',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255,99,132,1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});


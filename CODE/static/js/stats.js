var ctx1 = document.getElementById('myChart1').getContext('2d');
var chart1 = new Chart(ctx1, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: {{ stat1['labels'] }},
datasets: [{
    label: 'statistics',
    // backgroundColor: 'rgb(0,0,0)',
    borderColor: 'rgb(165, 212, 178)',
    data: {{ stat1['data'] }},
    order: 2,
    fill: false,
    pointHoverRadius: 10,
    pointStyle: 'rectRounded'
            // tension: 0.5
                },
{
    label: 'threshold',
    // backgroundColor: 'rgb(0,0,0)',
    borderColor: 'rgb(165, 212, 178)',
    data: {{ stat1['threshold']}},
    order: 1,
    pointRadius: 0,
    borderWidth: 2,
    fill: false,
    borderDash: [3],
                }]
            },

// Configuration options go here
options: {
    labels: {
        fontColor: 'black'
    }
}
        });

var ctx2 = document.getElementById('myChart2').getContext('2d');
var chart2 = new Chart(ctx2, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: {{ stat2['labels'] }},
datasets: [{
    label: 'year',
    backgroundColor: 'rgb(0,0,0)',
    borderColor: 'rgb(165, 212, 178)',
    data: {{ stat2['data'] }}
                        }]
                    },

// Configuration options go here
options: {
}
        });

var ctx3 = document.getElementById('myChart3').getContext('2d');
var chart3 = new Chart(ctx3, {
    // The type of chart we want to create
    type: 'doughnut',

    // The data for our dataset
    data: {
        labels: {{ stat3['labels'] | tojson }},
datasets: [{
    backgroundColor: ['rgb(252, 186, 3)', 'rgb(11, 155, 212)', 'rgb(252, 103, 3)', 'rgb(212, 11, 95)', 'rgb(105, 6, 191)', 'rgb(256,256,256)'],
    borderColor: 'rgb(165, 212, 178)',
    data: {{ stat3['data'] }}
        }]
                    },

// Configuration options go here
options: {
    title: {
        display: true,
            text: 'pie chart',
                position: 'bottom'
    }
}
        });

var ctx41 = document.getElementById('myChart41').getContext('2d');
var chart41 = new Chart(ctx41, {
    // The type of chart we want to create
    type: 'doughnut',

    // The data for our dataset
    data: {
        labels: {{ stat41['labels'] | tojson }},
datasets: [{
    backgroundColor: ['rgb(252, 186, 3)', 'rgb(11, 155, 212)', 'rgb(252, 103, 3)', 'rgb(212, 11, 95)', 'rgb(105, 6, 191)', 'rgb(256,256,256)'],
    borderColor: 'rgb(165, 212, 178)',
    data: {{ stat41['data'] }}
        }]
                    },

// Configuration options go here
options: {
    title: {
        display: true,
            text: 'pie chart',
                position: 'bottom'
    }
}
        });

var ctx42 = document.getElementById('myChart42').getContext('2d');
var chart42 = new Chart(ctx42, {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
        labels: {{ stat42['labels'] | tojson }},
datasets: [{
    backgroundColor: 'rgb(0,0,0)',
    borderColor: 'rgb(165, 212, 178)',
    data: {{ stat42['data'] }},
                },
{
    label: 'threshold',
    // backgroundColor: 'rgb(0,0,0)',
    borderColor: 'rgb(165, 212, 178)',
    data: {{ stat42['threshold']}},
    type: 'line',
    order: 1,
    pointRadius: 0,
    borderWidth: 2,
    fill: false,
    borderDash: [3],
                }]
            },

// Configuration options go here
options: {
    labels: {
        fontColor: 'black'
    }
}
        });


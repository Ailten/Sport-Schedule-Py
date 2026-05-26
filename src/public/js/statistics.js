
window.addEventListener('load', _ => {

    // get data from hidden input.
    kcalDays = Array.prototype.map.call(
        document.getElementsByClassName('kcal-day-value'),
        inputHidden => inputHidden.value
    );

    // send data to graph chart.
    generateGraph(
        kcalDays
    );

});



function generateGraph(data) {

    const canva = document.getElementById('calorie-chart');
    const ctx = canva.getContext('2d');

    const calorieChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            datasets: [{
                label: 'Calories (Kcal)',
                data: data,
                backgroundColor: 'rgba(13, 110, 253, 0.6)',
                borderColor: 'rgb(13, 110, 253)',
                borderWidth: 1,
                borderRadius: 5
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Calories'
                    }
                }
            }
        }
    });

}
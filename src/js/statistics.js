
window.addEventListener('load', _ => {

    generateGraph(
        [2100, 1850, 2400, 1900, 2250, 2600, 2000]
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
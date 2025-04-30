// static/js/chart-init.js
document.addEventListener('DOMContentLoaded', () => {
    const dataEl = document.getElementById('chart-data');
    
    // Get labels and temps from the data attributes set in the DOM
    const labels = JSON.parse(dataEl.dataset.labels);
    const temps  = JSON.parse(dataEl.dataset.temps);
  
    const ctx = document.getElementById('tempChart').getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: 'Temp (°C)',
          data: temps,
          fill: false,
          borderColor: 'rgba(75, 192, 192, 1)',
          tension: 0.1
        }]
      },
      options: {
        responsive: true,
        scales: {
          y: { beginAtZero: false }
        }
      }
    });
  });
  
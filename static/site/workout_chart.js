function showChart(data) {
    for (i=0; i<data.length; i++) {
        document.getElementById('chart').innerHTML += (String(data[i]) + "</br>");
    }
}
function showChart(data, labels, sums) {
    console.log(data);
    console.log(labels);
    console.log(sums);
    // First I want to add all my workouts to a table. 
    html = "";
    html += "<table class=\"table is-fullwidth is-striped is-hoverable\>\
                <thead class=\"thead\">\
                <th class=\"th\">Date</th>\
                <th class=\"th\">Duration</th>\
                <th class=\"th\">Type</th>\
                </thead>";
    for (i=0; i<data.length; i++) {
        html += "<tr class=\"tr\">";
        for(j=0; j<data[i].length; j++) {
            html += ("<td class=\"td\">" + String(data[i][j]) + "</td>");
        }
        html += "</tr>";
    }
    html += "</table>";
    document.getElementById('chart').innerHTML += html;

    // Next we want to table the sum of all of our workouts. 
    html = "";
    html += "<table class=\"table is-fullwidth is-striped is-hoverable\>\
                <thead class=\"thead\">\
                <th class=\"th\">Workout</th>\
                <th class=\"th\">Total Duration</th>\
                </thead>";
    for (i=0; i<labels.length; i++) {
        html += "<tr class=\"tr\">";
        html += ("<td class=\"td\">" + String(labels[i]).toUpperCase() + "</td>" + "<td class=\"td\">" + String(sums[i]) + "</td>");
        html += "</tr>";
    }
    html += "</table>";
    document.getElementById('chart').innerHTML += html;
    console.log("butt");
}
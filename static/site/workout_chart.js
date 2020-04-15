function showChart(data, labels) {
    console.log(data);
    console.log(labels);
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
}
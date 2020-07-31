// from data.js
var tableData = data;

// YOUR CODE HERE!
var tbody = d3.select("tbody");

// Function to display Full Table
function completeTable(sighting) {
    tbody.text("")
    sighting.forEach((data_entry) => {
      var table_row = tbody.append("tr");
      Object.entries(data_entry).forEach(([key, value]) => {
        var cell = table_row.append("td").text(value);
    })
})}

// Full Table
completeTable(tableData);  

// Filter Button
var filter_button = d3.select("#filter-btn");

// Function to filter table based on user input
filter_button.on("click", function() {

    d3.event.preventDefault();
    var input = d3.select("#datetime").property("value");
    var new_table = tableData.filter(data_entry => data_entry.datetime === input.trim());

    // Message when nothing found, else show requested results
    if (new_table.length === 0) {
        tbody.text("")
        d3.select("tbody").append("tr").append("td").attr("colspan", 7).html("<h4>Try Another Date</h4>");
    } else {
        completeTable(new_table);
    }
});

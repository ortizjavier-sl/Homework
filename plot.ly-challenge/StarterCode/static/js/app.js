// Fill dropdown list
d3.json("samples.json").then((buttonData) => {
  var buttonIds = buttonData.names;
  for (var i = 0; i < buttonIds.length; i++) {
    listSelect = d3.select("#selDataset");
    listSelect.append("option").text(buttonIds[i]);
  }

// Create inital chart based on non filtered data
  var samplePlaceholder = buttonIds[0];
  barbubbleChart(samplePlaceholder);
  gaugeChart(samplePlaceholder);
});

// Create Guage Chart
function gaugeChart(sample) {
  d3.json("samples.json").then((buttonData) => {
    var filteredMetadata = buttonData.metadata.filter(sampleObject => sampleObject.id == sample)[0];
    var metadataSelect = d3.select("#sample-metadata").html("");
    Object.entries(filteredMetadata).forEach(([key, value]) => {
      metadataSelect.append("h6").text(`${key} : ${value}`)
      });

    // Gauge Chart data
    var data = [
      {
        domain: { 'x': [0, 1], 'y': [0, 1] },
        title: 'Belly Button Washing Frequency<br> Scrubs per Week',
        value: filteredMetadata.wfreq,
        type: "indicator",
        mode: "gauge+number",
        gauge: { 
          axis: { range: [0, 9] ,tickwidth: .5 },
          bar: { color: "#337005" },
          borderwidth: 0,
          steps: [
            { range: [0, 1], color: "#fffdf6" },
            { range: [1, 2], color: "#fffbea" },
            { range: [2, 3], color: "fff8dc" },
            { range: [3, 4], color: "f5efb0" },
            { range: [4, 5], color: "#ebe684" },
            { range: [5, 6], color: "#e0eb9a" },
            { range: [6, 7], color: "#c9d78f" },
            { range: [7, 8], color: "#a3bf58" },
            { range: [8, 9], color: "75a316" }
            ]
          }
        }
      ];

    // Gauge Chart layout
    var layout = {
      width: 400,
      height: 400,
      margin: { t: 55, r: 25, l: 35, b: 15 },
      font: { color: "black" }
    };
    
    Plotly.newPlot("gauge", data, layout);
  })
};

// Creating Buble and Bar Chart 
function barbubbleChart(sample) {    
  d3.json("samples.json").then((buttonData) => {
    var filteredSamples = buttonData.samples.filter(sampleObject => sampleObject.id == sample)[0];
    var sample_values = filteredSamples.sample_values;
    var otu_ids = filteredSamples.otu_ids;
    var otu_labels = filteredSamples.otu_labels;

    // Create bar chart
    var trace1 = [{
      x: sample_values.slice(0,10).reverse(),
      y: otu_ids.slice(0,10).map(otuID => "OTU " + otuID).reverse(),
      text: otu_labels.slice(0,10).reverse(),
      marker: {color: '009999'},
      type: "bar",
      orientation: "h"
    }];
    var layout = {
      title: "Top OTUs",
      margin: {l: 140, r: 90, t: 30, b: 20}
    };

    Plotly.newPlot("bar", trace1, layout);

    // Bubble Chart
    var trace1 = [{
      x: otu_ids ,
      y: sample_values,
      mode: 'markers',
      marker: {
        size: sample_values,
        color: otu_ids,
        colorscale:"Earth"
        }
      }
    ];

    var layout = {
      xaxis: {title:"OTU ID " },
      margin: {t:50, b: 75}
    };

    Plotly.newPlot('bubble', trace1, layout); 

  })
};

// Update data based on user selection
function optionChanged(userSelection) {
  barbubbleChart(userSelection);
  gaugeChart(userSelection);
};
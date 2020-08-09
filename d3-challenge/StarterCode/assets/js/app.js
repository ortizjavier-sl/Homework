
function makeResponsive() {
    // resize chart according to window size
    var svgArea = d3.select("body").select("svg");
    if (!svgArea.empty()) {
        svgArea.remove();
    }
    
    // svg params
    var svgHeight = window.innerHeight;
    var svgWidth = window.innerWidth;
    
    var margin = {
        top: 100,
        right: 300,
        bottom: 450,
        left: 100
    };
    
    var chartwidth = svgWidth - margin.left - margin.right;
    var chartheight = svgHeight - margin.top - margin.bottom;
    
    var chartCircle = (chartwidth * chartheight) * 0.000035; 
    var chartText = (chartwidth * chartheight) * .00003;

    // SVG wrapper 
    var svg = d3
    .select("body")
    .append("svg")
    .attr("width", svgWidth)
    .attr("height", svgHeight);
    
    var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

    // Import CSV Data
    d3.csv("assets/data/data.csv", function( healthData) {
        healthData.forEach(function(data) {
            data.poverty = +data.poverty;
            data.obesity = +data.obesity;
        });
        
        // Create scale
        var xLinearScale = d3.scaleLinear()
        .domain([d3.min(healthData, d=> d.poverty) * .9, 
            d3.max(healthData, d=> d.poverty) * 1.1  
        ])
        .range([0, chartwidth]);
        
        var yLinearScale = d3.scaleLinear()
        .domain([d3.min(healthData, d => d.obesity) * .9, 
            d3.max(healthData, d => d.obesity) * 1.1
        ])
        .range([chartheight, 0]);
        
        // Create axis
        var bottomAxis = d3.axisBottom(xLinearScale);
        var leftAxis = d3.axisLeft(yLinearScale);
        
        // Append Axes to the chartGrooup
        chartGroup.append("g")
        .attr("transform", `translate(0, ${chartheight})`)
        .call(bottomAxis);
        
        chartGroup.append("g")
        .call(leftAxis);

        // Create Circles
        var circlesGroup = chartGroup.selectAll("circle")
        .data(healthData)
        .enter()
        .append("circle")
        .attr("cx", d => xLinearScale(d.poverty ))
        .attr("cy", d => yLinearScale(d.obesity ))
        .attr("r", chartCircle)
        .attr("class", "stateCircle")

        chartGroup.selectAll("text")
        .exit()
        .data(healthData)
        .enter()
        .append("text")
        .text(d => d.abbr)
        .attr("x", d => xLinearScale(d.poverty))
        .attr("y", d => yLinearScale(d.obesity))
        .attr("font-size", chartText+"px")
        .attr("class","stateText");

        // Initialize Tooltip
        var toolTip = d3.tip()
        .attr("class", "d3-tip")
        .offset([80, 0])
        .html(function(d) {
            return (`${d.state} <br>
            Poverty: ${d.poverty}% <br>
            Obesity: ${d.obesity}%`);
        });

        // Create tooltip
        chartGroup.call(toolTip);

        // Create event listeners
        circlesGroup.on("mouseover", function(data) {
            toolTip.show(data,this);
          })

        // onmouseout event
        .on("mouseout", function(data, index) {
            toolTip.hide(data);
        });
        
        // Create axes labels
        chartGroup.append("text")
        .attr("transform", `translate(${chartwidth / 2}, ${chartheight + margin.top + 10})`)
        .attr("class", "axisText")
        .attr("font-size", chartText+ 10 +"px")
        .text("In Poverty (%)");
        
        // Create axes labels
        chartGroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left + 20)
        .attr("x", 0 - (chartheight / 2))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .attr("font-size", chartText+ 10 + "px")
        .text("Lacks Healthcare (%)");
    });
}

makeResponsive();

// Window resize
d3.select(window).on("resize", makeResponsive);

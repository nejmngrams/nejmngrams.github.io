function capConvert(s){
    return s.replace(/([A-Z])/g, "$1_").toLowerCase(); 
}

var svg = d3.select("svg"),
    margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom,
    g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var parseTime = d3.timeParse("%Y");

var x = d3.scaleTime()
    .rangeRound([0, width]);

var y = d3.scaleLinear()
    .rangeRound([height, 0]);

var line = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.freq); });

window.plotnum = 0;
window.colors = ["#98abc5", "#ff8c00", "#8a89a6", "#d0743c", "#7b6888", "#a05d56", "#6b486b"];

function plot(){
  var ng = document.getElementById("ngram").value;
  ng = capConvert(ng);
  console.log(ng);
  console.log(plotnum);
  d3.csv("http://nejmngrams.github.io/ngramcsv/"+ng+".csv", function(d) {
    d.date = parseTime(d.date);
    d.freq = +d.freq;
    return d;
  }, function(error, data) {
    if (error) throw error;

    x.domain(d3.extent(data, function(d) { return d.date; }));
    if (plotnum<2){
        y.domain(d3.extent(data, function(d) { return d.freq; }));
    }

    g.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x))
      .select(".domain")
        .remove();

    g.append("g")
        .call(d3.axisLeft(y))
      .append("text")
        .attr("fill", "#000")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", "0.71em")
        .attr("text-anchor", "end")
        .text("word frequency");

    g.append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "white").transition().duration(2000).attr("stroke",colors[plotnum])
        .attr("stroke-linejoin", "round")
        .attr("stroke-linecap", "round")
        .attr("stroke-width", 1.5)
        .attr("d", line);

    g.append("text")
        .attr("transform", "translate(" + (width-30) + "," + y(data[0].freq) + ")")
        .attr("dy", ".71em")
        .attr("text-anchor", "start")
        .style("fill", colors[plotnum])
        .text(document.getElementById("ngram").value);
   });
   plotnum = plotnum+1
}


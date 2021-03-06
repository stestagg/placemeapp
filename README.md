ó
Qc           @   s   d  d l  Z  d  d l Z d   Z d   Z d   Z d   Z d   Z d e j f d     YZ e j	 d	 e f g d
 e
 Z d S(   iÿÿÿÿNc           C   s   i d d 6d d 6d d 6S(   Nt   Londont   connurbations   EC2A 4PEt   postcodet   Bunhillt   name(    (    (    (    s/   /Users/sstagg/src/placemeapp/placeme/placeme.pyt   get_location   s    c           C   s   i d d 6d d 6d d 6S(   Nt   pngt   typet   Crimet   titles(   http://dia.offsetdesign.co.uk/crimeb.pngt   content(    (    (    (    s/   /Users/sstagg/src/placemeapp/placeme/placeme.pyt	   get_crime   s    c           C   s   i d d 6d d 6d d 6S(   NR   R   s   Marital StatusR	   s*   http://dia.offsetdesign.co.uk/marriedc.pngR
   (    (    (    (    s/   /Users/sstagg/src/placemeapp/placeme/placeme.pyt   get_marital
   s    c           C   s   i d d 6d d 6d d 6d  S(   NR   R   s   Pay GapR	   s&   http://dia.offsetdesign.co.uk/payb.pngR
   (    (    (    (    s/   /Users/sstagg/src/placemeapp/placeme/placeme.pyt   get_pay   s    c           C   s   i d d 6d d 6d d 6S(   Nt   htmlR   s   HTML ExampleR	   sÐ  <!DOCTYPE html>
<meta name="viewport" content="width=device-width">
<meta charset="utf-8">
<style>

body {
  font-family: sans-serif-light, "Helvetica Neue", Helvetica, Arial, sans-serif;
  margin: auto;
  position: relative;
}
h1{
  color: #9933cc;
  font-size: 24px;
}
text {
  font: 10px sans-serif;
}

.axis path,
.axis line {
  fill: none;
  stroke: #000;
  shape-rendering: crispEdges;
}

form {
  position: absolute;
  right: 10px;
  top: 10px;
}

</style>
<h1>HTML Example</h1>
<form>
  <label><input type="radio" name="mode" value="grouped"> Grouped</label>
  <label><input type="radio" name="mode" value="stacked" checked> Stacked</label>
</form>
<script src="http://d3js.org/d3.v3.min.js"></script>
<script>

var n = 4, // number of layers
    m = 58, // number of samples per layer
    stack = d3.layout.stack(),
    layers = stack(d3.range(n).map(function() { return bumpLayer(m, .1); })),
    yGroupMax = d3.max(layers, function(layer) { return d3.max(layer, function(d) { return d.y; }); }),
    yStackMax = d3.max(layers, function(layer) { return d3.max(layer, function(d) { return d.y0 + d.y; }); });

var margin = {top: 40, right: 10, bottom: 20, left: 10},
    width = 360 - margin.left - margin.right,
    height = 180 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .domain(d3.range(m))
    .rangeRoundBands([0, width], .08);

var y = d3.scale.linear()
    .domain([0, yStackMax])
    .range([height, 0]);

var color = d3.scale.linear()
    .domain([0, n - 1])
    .range(["#aad", "#556"]);

var xAxis = d3.svg.axis()
    .scale(x)
    .tickSize(0)
    .tickPadding(8).tickFormat(function(d){ return "";})
    .orient("bottom");

var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var layer = svg.selectAll(".layer")
    .data(layers)
  .enter().append("g")
    .attr("class", "layer")
    .style("fill", function(d, i) { return color(i); });

var rect = layer.selectAll("rect")
    .data(function(d) { return d; })
  .enter().append("rect")
    .attr("x", function(d) { return x(d.x); })
    .attr("y", height)
    .attr("width", x.rangeBand())
    .attr("height", 0);

rect.transition()
    .delay(function(d, i) { return i * 10; })
    .attr("y", function(d) { return y(d.y0 + d.y); })
    .attr("height", function(d) { return y(d.y0) - y(d.y0 + d.y); });

svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(xAxis);

d3.selectAll("input").on("change", function change() {
  if (this.value === "grouped") transitionGrouped();
  else transitionStacked();
});

function transitionGrouped() {
  y.domain([0, yGroupMax]);

  rect.transition()
      .duration(500)
      .delay(function(d, i) { return i * 10; })
      .attr("x", function(d, i, j) { return x(d.x) + x.rangeBand() / n * j; })
      .attr("width", x.rangeBand() / n)
    .transition()
      .attr("y", function(d) { return y(d.y); })
      .attr("height", function(d) { return height - y(d.y); });
}

function transitionStacked() {
  y.domain([0, yStackMax]);

  rect.transition()
      .duration(500)
      .delay(function(d, i) { return i * 10; })
      .attr("y", function(d) { return y(d.y0 + d.y); })
      .attr("height", function(d) { return y(d.y0) - y(d.y0 + d.y); })
    .transition()
      .attr("x", function(d) { return x(d.x); })
      .attr("width", x.rangeBand());
}

// Inspired by Lee Byron's test data generator.
function bumpLayer(n, o) {

  function bump(a) {
    var x = 1 / (.1 + Math.random()),
        y = 2 * Math.random() - .5,
        z = 10 / (.1 + Math.random());
    for (var i = 0; i < n; i++) {
      var w = (i / n - y) * z;
      a[i] += x * Math.exp(-w * w);
    }
  }

  var a = [], i;
  for (i = 0; i < n; ++i) a[i] = o + o * Math.random();
  for (i = 0; i < 5; ++i) bump(a);
  return a.map(function(d, i) { return {x: i, y: Math.max(0, d)}; });
}

</script>
R
   (    (    (    (    s/   /Users/sstagg/src/placemeapp/placeme/placeme.pyt   get_html   s    t
   GetContentc           B   s   e  Z d    Z RS(   c         C   s   d |  j  j d <|  j j d d  } |  j j d d  } i t   d 6t   t   t   t   g d 6} |  j  j	 t
 j | d	 d
  d  S(   Ns
   text/plains   Content-Typet   lats	   52.629729t   longs	   -1.131592t   locationt   datasetst   indenti   (   t   responset   headerst   requestt   getR   R   R   R   R   t   writet   jsont   dumps(   t   selfR   t   lont   body(    (    s/   /Users/sstagg/src/placemeapp/placeme/placeme.pyR      s    
(   t   __name__t
   __module__R   (    (    (    s/   /Users/sstagg/src/placemeapp/placeme/placeme.pyR      s   s   /api/data.json/?t   debug(   R   t   webapp2R   R   R   R   R   t   RequestHandlerR   t   WSGIApplicationt   Truet   app(    (    (    s/   /Users/sstagg/src/placemeapp/placeme/placeme.pyt   <module>   s   					
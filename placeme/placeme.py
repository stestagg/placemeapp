import json
import webapp2

def get_location():
	return {"connurbation":"London","postcode":"EC2A 4PE","name":"Bunhill"}

def get_crime():
	return {"type":"png","title":"Crime","content":"http://dia.offsetdesign.co.uk/crimeb.png"}

def get_marital():
	return {"type":"png","title":"Marital Status","content":"http://dia.offsetdesign.co.uk/marriedc.png"}

def get_pay():
	return {"type":"png","title":"Pay Gap","content":"http://dia.offsetdesign.co.uk/payb.png"}

def get_html():
	return {"type":"html","title":"HTML Example",
			"content":"<!DOCTYPE html>\n<meta name=\"viewport\" content=\"width=device-width\">\n<meta charset=\"utf-8\">\n<style>\n\nbody {\n  font-family: sans-serif-light, \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n  margin: auto;\n  position: relative;\n}\nh1{\n  color: #9933cc;\n  font-size: 24px;\n}\ntext {\n  font: 10px sans-serif;\n}\n\n.axis path,\n.axis line {\n  fill: none;\n  stroke: #000;\n  shape-rendering: crispEdges;\n}\n\nform {\n  position: absolute;\n  right: 10px;\n  top: 10px;\n}\n\n</style>\n<h1>HTML Example</h1>\n<form>\n  <label><input type=\"radio\" name=\"mode\" value=\"grouped\"> Grouped</label>\n  <label><input type=\"radio\" name=\"mode\" value=\"stacked\" checked> Stacked</label>\n</form>\n<script src=\"http://d3js.org/d3.v3.min.js\"></script>\n<script>\n\nvar n = 4, // number of layers\n    m = 58, // number of samples per layer\n    stack = d3.layout.stack(),\n    layers = stack(d3.range(n).map(function() { return bumpLayer(m, .1); })),\n    yGroupMax = d3.max(layers, function(layer) { return d3.max(layer, function(d) { return d.y; }); }),\n    yStackMax = d3.max(layers, function(layer) { return d3.max(layer, function(d) { return d.y0 + d.y; }); });\n\nvar margin = {top: 40, right: 10, bottom: 20, left: 10},\n    width = 360 - margin.left - margin.right,\n    height = 180 - margin.top - margin.bottom;\n\nvar x = d3.scale.ordinal()\n    .domain(d3.range(m))\n    .rangeRoundBands([0, width], .08);\n\nvar y = d3.scale.linear()\n    .domain([0, yStackMax])\n    .range([height, 0]);\n\nvar color = d3.scale.linear()\n    .domain([0, n - 1])\n    .range([\"#aad\", \"#556\"]);\n\nvar xAxis = d3.svg.axis()\n    .scale(x)\n    .tickSize(0)\n    .tickPadding(8).tickFormat(function(d){ return \"\";})\n    .orient(\"bottom\");\n\nvar svg = d3.select(\"body\").append(\"svg\")\n    .attr(\"width\", width + margin.left + margin.right)\n    .attr(\"height\", height + margin.top + margin.bottom)\n  .append(\"g\")\n    .attr(\"transform\", \"translate(\" + margin.left + \",\" + margin.top + \")\");\n\nvar layer = svg.selectAll(\".layer\")\n    .data(layers)\n  .enter().append(\"g\")\n    .attr(\"class\", \"layer\")\n    .style(\"fill\", function(d, i) { return color(i); });\n\nvar rect = layer.selectAll(\"rect\")\n    .data(function(d) { return d; })\n  .enter().append(\"rect\")\n    .attr(\"x\", function(d) { return x(d.x); })\n    .attr(\"y\", height)\n    .attr(\"width\", x.rangeBand())\n    .attr(\"height\", 0);\n\nrect.transition()\n    .delay(function(d, i) { return i * 10; })\n    .attr(\"y\", function(d) { return y(d.y0 + d.y); })\n    .attr(\"height\", function(d) { return y(d.y0) - y(d.y0 + d.y); });\n\nsvg.append(\"g\")\n    .attr(\"class\", \"x axis\")\n    .attr(\"transform\", \"translate(0,\" + height + \")\")\n    .call(xAxis);\n\nd3.selectAll(\"input\").on(\"change\", function change() {\n  if (this.value === \"grouped\") transitionGrouped();\n  else transitionStacked();\n});\n\nfunction transitionGrouped() {\n  y.domain([0, yGroupMax]);\n\n  rect.transition()\n      .duration(500)\n      .delay(function(d, i) { return i * 10; })\n      .attr(\"x\", function(d, i, j) { return x(d.x) + x.rangeBand() / n * j; })\n      .attr(\"width\", x.rangeBand() / n)\n    .transition()\n      .attr(\"y\", function(d) { return y(d.y); })\n      .attr(\"height\", function(d) { return height - y(d.y); });\n}\n\nfunction transitionStacked() {\n  y.domain([0, yStackMax]);\n\n  rect.transition()\n      .duration(500)\n      .delay(function(d, i) { return i * 10; })\n      .attr(\"y\", function(d) { return y(d.y0 + d.y); })\n      .attr(\"height\", function(d) { return y(d.y0) - y(d.y0 + d.y); })\n    .transition()\n      .attr(\"x\", function(d) { return x(d.x); })\n      .attr(\"width\", x.rangeBand());\n}\n\n// Inspired by Lee Byron's test data generator.\nfunction bumpLayer(n, o) {\n\n  function bump(a) {\n    var x = 1 / (.1 + Math.random()),\n        y = 2 * Math.random() - .5,\n        z = 10 / (.1 + Math.random());\n    for (var i = 0; i < n; i++) {\n      var w = (i / n - y) * z;\n      a[i] += x * Math.exp(-w * w);\n    }\n  }\n\n  var a = [], i;\n  for (i = 0; i < n; ++i) a[i] = o + o * Math.random();\n  for (i = 0; i < 5; ++i) bump(a);\n  return a.map(function(d, i) { return {x: i, y: Math.max(0, d)}; });\n}\n\n</script>\n"}

class GetContent(webapp2.RequestHandler):
  	def get(self):
		#urlhttp://dia.offsetdesign.co.uk?lat=xxx&long=yyy&cat=xxx
		self.response.headers['Content-Type'] = 'text/plain'
		lat = self.request.get("lat", "52.629729")
		lon = self.request.get("long", "-1.131592")

		body = {
			"location": get_location(),
			"datasets": [
				get_crime(),
				get_marital(),
				get_pay(),
				get_html()
			]
			
		}
		self.response.write(json.dumps(body, indent=2))

app = webapp2.WSGIApplication([('/api/data.json/?', GetContent)], debug=True)

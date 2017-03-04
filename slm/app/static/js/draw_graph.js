var w = 1300;
var h = 600;
var linkDistance=220;

var colors =  d3.scale.category10();
//
//var dataset = {
//
//    nodes: [
//        {id:"0",name: "Adam Adam Adam","group":0},
//        {id:"1",name: "Bob ","group":1},
//        {id:"2",name: "Carrie","group":1},
//        {id:"3",name: "Donovan","group":1}
//
//    ],
//    edges: [
//        {relation:"Defined in",source: 0, target: 1,"group":1},
//        {relation:"Defined in",source: 0, target: 2,"group":1},
//        {relation:"Defined in",source: 0, target: 3,"group":1}
//
//
//    ]
//};
var svg = ''

function showGraph(dataset) {
    svg = d3.select("#container").append("svg").attr({"width": w, "height": h});

    svg.append("rect")
        .attr("width", "100%")
        .attr("height", "100%")
        .attr("fill", "#e0e0e0");

    var force = d3.layout.force()
        .nodes(dataset.nodes)
        .links(dataset.edges)
        .size([w, h])
        .linkDistance([linkDistance])
        .charge([-500])
        .theta(0.1)
        .gravity(0.05)
        .start();


    var edges = svg.append("g")
        .selectAll("line")
        .data(dataset.edges)
        .enter()
        .append("line")
        .attr("id", function (d, i) {
            return 'edge' + i
        })
        .attr('marker-end', 'url(#arrowhead)')
        .style("stroke", function (d, i) {
            return colors(d.group);
        })
        .style("pointer-events", "none");


    var nodesLenght = dataset.nodes.length;
    var radius = 25;
    var arrowDistance = 18;
    if (nodesLenght <= 10) {
        var radius = 50;
        var arrowDistance = 60;
    }
    else if (nodesLenght > 10) {
        var radius = 35;
        var arrowDistance = 42;
    }

// Define the div for the tooltip
    var div = d3.select("#container").append("div")
        .attr("class", "tooltip");


//    var nodes = svg.selectAll("circle")
    var nodes = svg.append("g")
        .selectAll("circle")
        .data(dataset.nodes)
        .enter()
        .append("circle")
        .attr({"r": radius})
        .attr('fill-opacity', 1)
        .style("fill", function (d, i) {
            return colors(d.group);
        })
        .style("stroke", function (d, i) {
            return colors(d.group);
        })
        .call(force.drag)
        .on("mouseover", function (d) {
            div.transition()
                .duration(200)
                .style("opacity", .9);
            div.html('<div class="completeTitle">' + d.id + ' : ' + d.name + "</div><br/>")
                .style("left", (d3.event.pageX) + "px")
                .style("top", (d3.event.pageY - 28) + "px");
        })
        .on("mouseout", function (d) {
            div.transition()
                .duration(500)
                .style("opacity", 0.5);
        });
    nodes.append("title")
        .text(function (d) {
            return d.id + "\n" + d.name
        });

    var nodelabels = svg.selectAll(".nodelabel")
        .data(dataset.nodes)
        .enter()
        .append("text")
        .attr({
            "x": function (d) {
                return d.x;
            },
            "y": function (d) {
                return d.y;
            },
            "class": "nodelabel"
        })
        //            .style("fill",function(d,i){return colors(d.group)})
        .style("fill", "#fff")
        //            .style("stroke",function(d,i){return colors(d.group)})
        //            .style("stroke","#fff")
        .style("font-size", 12 + "px")
        .text(function (d) {
            if (d.name.length > 10)
                return d.id + ' ' + d.name.substring(0, 7) + '..';
            else
                return d.id + ' ' + d.name;
        });
    nodelabels.append("title")
        .text(function (d) {
            return d.id + "\n" + d.name
        });

    var edgepaths = svg.selectAll(".edgepath")
        .data(dataset.edges)
        .enter()
        .append('path')
        .attr({
            'd': function (d) {
                return 'M ' + d.source.x + ' ' + d.source.y + ' L ' + d.target.x + ' ' + d.target.y
            },
            'class': 'edgepath',
            'fill-opacity': 0,
            'stroke-opacity': 0,
            'fill': 'blue',
            'stroke': 'red',
            'id': function (d, i) {
                return 'edgepath' + i
            }
        })
        .style("pointer-events", "none");

    var edgelabels = svg.selectAll(".edgelabel")
        .data(dataset.edges)
        .enter()
        .append('text')
        .style("pointer-events", "none")
        .attr({
            'class': 'edgelabel',
            'id': function (d, i) {
                return "edge" + i
            },
            'dx': 80,
            'dy': 0,
            'font-size': 10,
            'fill': '#000'
        });

    edgelabels.append('textPath')
        .attr('xlink:href', function (d, i) {
            return '#edgepath' + i
        })
        .style("pointer-events", "none")
        .text(function (d, i) {
            return d.relation;
        });


    svg.append('defs').append('marker')
        .attr({
            'id': 'arrowhead',
            'viewBox': '-0 -5 10 10',
            'refX': arrowDistance,
            'refY': 0,
            //'markerUnits':'strokeWidth',
            'orient': 'auto',
            'markerWidth': 10,
            'markerHeight': 10,
            'xoverflow': 'visible'
        })
        .append('svg:path')
        .attr('d', 'M 0,-5 L 10 ,0 L 0,5')
        .attr('fill', '#ccc')
        .attr('stroke', '#ccc');


    force.on("tick", function () {

        edges.attr({
            "x1": function (d) {
                return d.source.x;
            },
            "y1": function (d) {
                return d.source.y;
            },
            "x2": function (d) {
                return d.target.x;
            },
            "y2": function (d) {
                return d.target.y;
            }
        });

        nodes.attr({
            "cx": function (d) {
                return d.x;
            },
            "cy": function (d) {
                return d.y;
            }
        });

        nodelabels.attr("x", function (d) {
                return d.x - 15;
            })
            .attr("y", function (d) {
                return d.y + 5;
            });

        edgepaths.attr('d', function (d) {
            var path = 'M ' + d.source.x + ' ' + d.source.y + ' L ' + d.target.x + ' ' + d.target.y;
            //console.log(d)
            return path
        });

        edgelabels.attr('transform', function (d, i) {
            if (d.target.x < d.source.x) {
                bbox = this.getBBox();
                rx = bbox.x + bbox.width / 2;
                ry = bbox.y + bbox.height / 2;
                return 'rotate(180 ' + rx + ' ' + ry + ')';
            }
            else {
                return 'rotate(0)';
            }
        });
    });
}
var taiwan;

var map;
var map_options;

var marker_cluster;
var marker_cluster_options = { gridSize: 150, maxZoom: 15,
  // set customize calculator
  calculator: function (markers, numStyles) {
    var count = markers.length.toString();
    return {
      text: count,
      index: 1 + Math.floor(Math.random() * numStyles),
      title: ""
    };
  }
};

Template.map_canvas.rendered = function () {
  initialize_map();

  Meteor.call('get_icon_styles', function (error, styles) {
    marker_cluster_options["styles"] = styles;
    Meteor.call('get_locations', function (error, locations) {
      add_markers(locations);
    });
  });
};

// initialize google map
function initialize_map() {
  taiwan = new google.maps.LatLng(23.5989353, 121.0173534);
  map_options = { zoom: 8, center: taiwan };
  map = new google.maps.Map(document.getElementById('map-canvas'), map_options);
}

function add_markers(locations) {
  var markers = [];
  for (var i = 0; i < locations.length; i++) {
    var position = new google.maps.LatLng(locations[i].lat, locations[i].lng);
    var marker = new google.maps.Marker({ position: position });
    markers.push(marker);
  }
  marker_cluster = new MarkerClusterer(map, markers, marker_cluster_options);
  //marker_cluster = new MarkerClusterer(map, markers);
}

var map;
var taiwan;

Template.map_canvas.rendered = function () {
  taiwan = new google.maps.LatLng(23.5989353, 121.0173534);
  google.maps.event.addDomListener(window, 'load', initialize);

  Meteor.call('get_locations', function (error, locations) {
    if (error) {
      console.log(error);
    } else {
      for (var i = 0; i < locations.length; i++) {
        var position = new google.maps.LatLng(locations[i].lat,
                                              locations[i].lng);
        add_marker(position);
      }
    }
  });
};

// initialize google map
function initialize() {
  var mapOptions = {
    zoom: 8,
    center: taiwan
  };
  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
}

function add_marker(position) {
  var marker = new google.maps.Marker({
    position: position,
    map: map,
  });
}

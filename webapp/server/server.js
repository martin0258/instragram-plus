var fs = Npm.require('fs');
var path = Npm.require('path');

Meteor.methods({
  get_locations: function (count_min, count_max) {
    var filepath ='location.csv';

    // DEBUG: Know current directory
    //console.log(path.resolve("."));
    
    var locations = [];
    var lines = Assets.getText(filepath).toString().split("\n");
    for (row in lines) {
      var line = lines[row];

      var data = line.split(',');
      var location = {
        id: data[0],
        lat: parseFloat(data[1]),
        lng: parseFloat(data[2]),
        name: data[3],
        img_count: parseInt(data[4], 10)
      };

      if (location.img_count >= count_min &&
          location.img_count <= count_max) {
        locations.push(location);
      }
    }

    // sort locations based on image count (descending)
    var compare = function (a, b) {
      if (a > b) return 1;
      else if (a < b) return -1;
      else return 0;
    };
    locations.sort(function(a, b) {
      return compare(b.img_count, a.img_count);
    });
    return locations;
  },

  get_location: function (location_id) {
    var filepath ='location.csv';

    // DEBUG: Know current directory
    //console.log(path.resolve("."));

    var lines = Assets.getText(filepath).toString().split("\n");
    for (var i = 0; i < lines.length; i++) {
      var data = lines[i].split(',');
      var location = {
        id: data[0],
        lat: parseFloat(data[1]),
        lng: parseFloat(data[2]),
        name: data[3],
        img_count: parseInt(data[4], 10)
      };
      if (location.id == location_id) return location;
    }
    return null;
  },

  get_images: function (location_id, topN) {
    var img_folder_path = 'imgs/finalresult/';
    var images = [];
    var location_filepath = img_folder_path + 'img_' + location_id + '.txt';
    var lines = Assets.getText(location_filepath).toString().split("\n");

    topN = (topN==null) ? lines.length : topN;

    for (var i = 0; i < lines.length && i < topN; i++) {
      var data = lines[i].split(',');
      var image = {
        rank: i + 1,
        website_url: data[0],
        img_url: data[1]
      };
      images.push(image);
    }
    return images;
  }
});

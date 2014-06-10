var fs = Npm.require('fs');
var path = Npm.require('path');

Meteor.methods({
  get_locations: function () {
    var filepath ='../client/app/img_list.txt';

    // DEBUG: Know current directory
    //console.log(path.resolve("."));
    
    var exist = fs.existsSync(filepath);
    if (exist) {
      // file exists
      var locations = [];
      var lines = fs.readFileSync(filepath).toString().split("\n");
      for (row in lines) {
        var line = lines[row];

        // workaround of skipping error lines
        if (line.indexOf(':') == -1) continue;

        var location = line.split(':')[1];
        location = location.split(',');
        var lat_lng = {
          lat: parseFloat(location[0]),
          lng: parseFloat(location[1])
        };
        locations.push(lat_lng);
      }
      return locations;
    }
    else {
      // file does not exist
      var err_msg = filepath + " not found.";
      console.log(err_msg);
      throw new Meteor.Error(500, err_msg);
    }
  },

  get_icon_styles: function () {
    var img_folder_path = '../client/app/img';
    var exist = fs.existsSync(img_folder_path);
    if (exist) {
      // folder exists
      var styles = [];
      var files = fs.readdirSync(img_folder_path);
      for (var i = 0; i < files.length; i++) {
        var style = {
          url: 'img/' + files[i],
          height: 150,
          width: 150
        }
        styles.push(style);
      }
      return styles;
    }
    else {
      // file does not exist
      var err_msg = filepath + " not found.";
      console.log(err_msg);
      throw new Meteor.Error(500, err_msg);
    }
  }
});

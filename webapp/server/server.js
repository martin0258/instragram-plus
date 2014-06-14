var fs = Npm.require('fs');
var path = Npm.require('path');

Meteor.methods({
  get_locations: function () {
    var filepath ='location.txt';

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
      locations.push(location);
    }
    return locations;
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

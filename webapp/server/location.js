/*
 * Purpose: 
 *   (1) Fix invalid csv format caused by some location names.
 *   (2) Filter out locations with no image at all (count = 0).
 */

var fs = require('fs');
var path = require('path');

var filepath ='../private/location.csv';
var outfile = '../private/location_processed.csv';

// DEBUG: Know current directory
console.log(path.resolve("."));

var lines = fs.readFileSync(filepath).toString().split("\n");

// create new file
fs.writeFileSync(outfile, 'Id,Lat,Lng,Name,Count' + '\n');
for (row in lines) {
  var line = lines[row];

  var data = line.split(',');
  data[4] = parseInt(data[4], 10);
  if (data[4] > 0) {
    var re = new RegExp('"', 'g');
    data[3] = '"' + data[3].replace(re, '""') + '"';
    fs.appendFileSync(outfile, data.join() + '\n');
  }
}

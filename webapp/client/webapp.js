var taiwan;

var map;
var map_options;

var marker_cluster;
var marker_cluster_options = { gridSize: 150, maxZoom: 15 };

// fusion table layer
var layer;
var table_id = '1sndvh01p2Ab3hSlIu7s7IW0Ifn-bDd0juFWNToFC';
var location_column = 'Lat';

// image sliders
var img_slider;
var img_slider_options = {
  //mode: 'vertical',
  slideWidth: 200,
  minSlides: 3,
  maxSlides: 5,
  moveSlides: 1,
  slideMargin: 10,
  captions: true,
  controls: true
};

Template.filter.rendered = function () {
  initialize_filter();
};

Template.map_canvas.rendered = function () {
  initialize_map();
  set_click_listener();
};

Template.images.rendered = function () {
  img_slider = $('.bxslider').bxSlider({controls: false});
  $('.bx-wrapper').css({position: 'absolute',
                        bottom: '0px',
                        left: '20px'}).hide();
};

function initialize_filter() {
  $( "#slider-range" ).slider({
    range: true,
    min: 0,
    max: 12500,
    values: [ 1000, 10000 ],
    slide: function( event, ui ) {
      $( "#range" ).val( ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      set_layer();  // update fusion layer
    }
  });
  $( "#range" ).val( $( "#slider-range" ).slider( "values", 0 ) +
                     " - " + $( "#slider-range" ).slider( "values", 1 ) );
}

// initialize google map
function initialize_map() {
  taiwan = new google.maps.LatLng(23.5989353, 121.0173534);
  taipei = new google.maps.LatLng(25.0854062, 121.5615012);
  map_options = { zoom: 8, center: taiwan };
  map = new google.maps.Map(document.getElementById('map-canvas'), map_options);

  // set layer
  layer = new google.maps.FusionTablesLayer();
  set_layer();
  layer.setMap(map);
}

// set fusion table layer option
function set_layer() {
  var val1 = $( "#slider-range" ).slider( "values", 0 );
  var val2 = $( "#slider-range" ).slider( "values", 1 );
  var where_clause = 'Count >= ' + val1 + ' AND Count <= ' + val2;
  layer.setOptions({
    query: {
      select: location_column,
      from: table_id,
      where: where_clause
    },
    styles: [{
      markerOptions: {
        iconName: 'small_red'
        //iconName: 'large_red'
      }
    }]
  });
}

// handle google map event click
function set_click_listener() {
  var topN = 20;
  google.maps.event.addListener(layer, 'click', function(e) {
    var location_id = e.row["Id"].value;
    Meteor.call('get_images', location_id, topN, function (err, images) {
      display_images(images);
    });
  });  
}

// display images at bottom
function display_images(images) {
  // We hope not to let users see updating flash.
  $('.bx-wrapper').hide();

  // remove all previous slides
  $('.bxslider').find('.slide').remove();

  // add slides
  for (var i = 0; i < images.length; i++) {
    var image = images[i];
    var src = '<div class="slide">' +
              '<img src="' + image.img_url + 
              '" data-website="' + image.website_url +
              '" title="' + image.rank + '" />' +
              '</div>';
    $('.bxslider').append(src);
  }

  $('.bxslider').find('.slide').find('img').click(function(){
    var url = $(this).attr('data-website');
    open_website(url);
  });
 
  // reload image slider
  img_slider.reloadSlider(img_slider_options);

  // add close button
  var close_btn_html = '<button class="close-button">' +
                       '<span class="ui-icon ui-icon-close"></span>' +
                       '</button>';
  // FIXME: duplicate code
  $('.bx-wrapper').css({position: 'absolute',
                        bottom: '0px',
                        left: '20px'})
                  .prepend(close_btn_html);
  // add close button handler
  $('.close-button').click(function(){
    $('.bx-wrapper').hide();
  });

  // hotfix of overlapping issue
  $('.bx-next').css({'z-index':99});
  $('.bx-wrapper').show();
}

function open_website(url) {
  var website_link_html = '<div><a class="website-url" target="_blank" ' +
                          'href="' + url + '">View on Instagram</a></div>';
  var iframe_html = '<iframe id="frame" src="' + url + '/embed/' +
                    '" width="612" height="710" frameborder="0" ' +
                    'allowtransparency="true" scrolling="no"></iframe>';
  var $dialog = $("<div></div>")
                .append(iframe_html)
                .append(website_link_html)
                .dialog({
    autoOpen: false,
    modal: true,
    width: 'auto',
    height: 'auto',
  });

  $dialog.dialog('open');
}

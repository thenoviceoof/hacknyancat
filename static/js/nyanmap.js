function initialize(lat,lng) {
    cat_location = new google.maps.LatLng(lat,lng);
    var myOptions = {
        center: cat_location,
        zoom: 14,
        mapTypeId: google.maps.MapTypeId.SATELLITE
    };
    map = new google.maps.Map(document.getElementById("map_canvas"),
				  myOptions);

    //remove all this hardcoded stuff later, it's just for testing getting the JSON info
    var radius = 500;
    var types = "food";
    var places_url = "http://nyancat.ninjapiraterockstardeveloper.com/google/places?location="+lat+","+lng+"&radius="+radius+"&types="+types+"&sensor=true&key=AIzaSyDVlmhMFLkex9hygFh8POvX7JwUAvdyX9s";
    var location_data = $.getJSON(places_url);
    console.log(location_data);




//updates center when user drags the map

    google.maps.event.addListener(map, 'center_changed', function() {
	cat_location = map.getCenter();
	console.log(cat_location);
	nearby_locations = [] //clear stored json

	var radius = 500; //meters
	var types = "points_of_interest";
	var lat = cat_location.lat;
	var lng = cat_location.lng;
	var places_url = "http://nyancat.ninjapiraterockstardeveloper.com/google/places?location="+lat+","+lng+"&radius="+radius+"&types="+types+"&sensor=true&key=AIzaSyDVlmhMFLkex9hygFh8POvX7JwUAvdyX9s";//don't put actual api key
	nearby_locations = $.getJSON(places_url).results;//ask server for json data, stores in nearby in api.js
	console.log(nearby_locations);
	//function that loads markers from json data
    });
}


var place_markers = function()
{

}


//deprecated
var panToCat = function()
{
    var lat = 10;
    var lng = 10;
    while(true) {
	var cat_location = new google.maps.LatLng(lat,lng);
	map.panTo(cat_location);
	lat++;
	console.log(lat);
	setTimeout(console.log('hi'),3000);
    }
}

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

    google.maps.event.addListener(map, 'mouseup', function() {
	cat_location = map.getCenter();
	console.log(cat_location);
	nearby_locations = []; //clear stored json

	var radius = 500; //meters
	var types = "food";
	var lat = cat_location.Ua;
	var lng = cat_location.Va;
	var places_url = "http://nyancat.ninjapiraterockstardeveloper.com/google/places?location="+lat+","+lng+"&radius="+radius+"&types="+types+"&sensor=true&key=AIzaSyDVlmhMFLkex9hygFh8POvX7JwUAvdyX9s";//don't put actual api key
	console.log($.getJSON(places_url));
	nearby_locations_json = $.getJSON(places_url);//ask server for json data, stores in nearby in api.js
	console.log(nearby_locations_json);
	a=nearby_locations_json_results;//just to play with
	nearby_locations_json_results = nearby_locations_json.responseText.results;
	console.log(nearby_locations_json_results);
	if(nearby_locations_json_results != undefined){
	    for(var i=0; i<nearby_locations_json_results.length; i++){
		console.log("adding a nearby_location");
		nearby_locations.append({
		    "lat": nearby_locations_json_results[i].geometry.location.lat,
		    "lng": nearby_locations_json_results[i].geometry.location.lng,
		    "name":nearby_locations_json_results[i].name,
		});
	    };

	    console.log(nearby_locations);

	    place_markers(nearby_locations);//actually places markers
	};
    });
}

//function that loads markers from json data
var place_markers = function(nearby_locations)
{
    for(var i=0; i<nearby_locations.length; i++){
	console.log("placing a marker");
	var marker = new google.maps.Marker({
	    position: new google.maps.LatLng(nearby_locations[i].lat,nearby_locations[i].lng),
	    map: map,
	    title: nearby_locations[i].name
	});
    };
};


//deprecated
/*
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
*/
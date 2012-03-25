function initialize(lat,lng) {
    var cat_location = new google.maps.LatLng(lat,lng);

    var myOptions = {
        center: cat_location,
        zoom: 14,
        mapTypeId: google.maps.MapTypeId.SATELLITE
    };
    map = new google.maps.Map(document.getElementById("map_canvas"),
				  myOptions);

    https://nyancat.ninjapiraterockstardeveloper.com/google/places/?location=-33.8670522,151.1957362&radius=500&types=food&name=harbour&sensor=false&key=AddYourOwnKeyHere
    var radius = 500;
    var types = "food";
    var places_url = "https://nyancat.ninjapiraterockstardeveloper.com/google/places?location="+lat+","+lng+"&radius="+radius+"&types="+types+"&sensor=true&key=AIzaSyDVlmhMFLkex9hygFh8POvX7JwUAvdyX9s";

    var location_data = $.getJSON(places_url);

    console.log(location_data);

//updates center when user drags the map

    



}

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

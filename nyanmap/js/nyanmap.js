function initialize(lat,lng) {
    var myOptions = {
        center: new google.maps.LatLng(lat,lng),
        zoom: 8,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map_canvas"),
				  myOptions);
}

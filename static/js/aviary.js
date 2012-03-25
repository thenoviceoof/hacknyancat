$(function () {
    AviaryJS.init();
});

var AviaryJS = AviaryJS || {};

AviaryJS.init = function () {
    AviaryJS.bindLightbox();
}

AviaryJS.setImagePath = function(path) {
		AviaryJS.imagePath=path;
	}	

AviaryJS.bindLightbox = function () {
    $('.light_box').click(function () {
        $(this).hide();
    });
};

AviaryJS.featherLoaded = false;
AviaryJS.featherReady = false;
AviaryJS.showFeather = function () {
	
    var launch = function () {
        if (AviaryJS.featherReady) {
            var imgSrc = $('#feather_demo').attr('src');
            AviaryJS.featherEditor.launch({
                image: 'feather_demo', 
                url: imgSrc
            });
        }
    }

    if (!AviaryJS.featherLoaded) {
        AviaryJS.featherLoaded = true;
        AviaryJS.loadScript('http://feather.aviary.com/js/feather.js', function () {

            AviaryJS.featherEditor = new Aviary.Feather({
                apiKey: '34d070728',
                apiVersion: 2,
                //maxSize: '400',
                onSave: function (imageID, newUrl) {
                    //console.log(newUrl);
                    //console.log(imageID);
                    //window.location = '/share?img=' + encodeURI(newUrl);
                },
                onLoad: function () {
                    AviaryJS.featherReady = true;
                    $('.avpw_close_button').click(function () {
                        AviaryJS.featherEditor.close();
                        return false;
                    });
                    launch();
                }
            });
        });
    } else {
        launch();
    }
}

AviaryJS.loadScript = function (url, callback) {
    var head = document.getElementsByTagName("head")[0];
    var script = document.createElement("script");
    script.src = url;

    /* Attach handlers for all browsers */
    var done = false;
    script.onload = script.onreadystatechange = function () {
        if (!done && (!this.readyState || this.readyState == "loaded" || this.readyState == "complete")) {
            done = true;

            /* Continue your code */
            if (callback != undefined) {
                callback();
            }

            /* Handle memory leak in IE */
            script.onload = script.onreadystatechange = null;
            head.removeChild(script);
        }
    };

    head.appendChild(script);
}
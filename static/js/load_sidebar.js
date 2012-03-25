$(document).ready(function() {
    (function($) {
        // load up data into appropriate sections
        load_sidebar();
    })(jQuery);
});

function load_sidebar() {
    // etsy
    $.ajax({
        url: '/etsy-results/',
        dateType: "html",
        success: function(data, textStatus) {
            $("#etsy-sidebar").html(data);
        }
    });

    // dc
    $.ajax({
        url: '/dc-results/',
        dateType: "html",
        success: function(data, textStatus) {
            $("#dc-sidebar").html(data);
        }
    });

    // dc
    $.ajax({
        url: '/static/longtail.html',
        dateType: "html",
        success: function(data, textStatus) {
            $("#dc-sidebar").html(data);
        }
    });
}
$(document).ready(function() {
    (function($) {
        // load up data into appropriate sections

        // etsy
        $.ajax({
            url: '/etsy-results/',
            dateType: "text",
            success: function(data, textStatus) {
                $("#etsy-sidebar").text(data);
            }
        });

        // dc
        $.ajax({
            url: '/dc-results/',
            dateType: "text",
            success: function(data, textStatus) {
                $("#dc-sidebar").text(data);
            }
        });

        // longtail
        $.ajax({
            url: '/static/longtail.html',
            dateType: "text",
            success: function(data, textStatus) {
                $("#longtail-sidebar").text(data);
            }
        });
    })(jQuery);
});
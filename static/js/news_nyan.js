/* live inside the closure */
$(document).ready(function() {
    (function($) {
        $("body").append($("<div>").attr("id","ticker-tape"));
        var ticker = $("#ticker-tape");
        ticker.append($("<p>"));

        var ticker_interval = setTimeout(move_ticker, 1);
        var refresh_interval = setTimeout(refresh_ticker, 1);

        function move_ticker() {
            console.log("cool");
            ticker.find("p").animate({
                'marginLeft': "-=20px"
            }, 1000, "linear");
            ticker_interval = setTimeout(move_ticker, 1000);
        }
        function refresh_ticker() {
            $.ajax({
                url: '/newswire',
                dateType: "text",
                success: function(data, textStatus) {
                    // clear ticker, repopulate
                    ticker.html("");
                    ticker.append($("<p>").html(data));
                }
            });
            refresh_interval = setTimeout(refresh_ticker, 90*1000);
        }
    })(jQuery);
});
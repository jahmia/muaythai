$(document).ready( function() {
    if ( window.location.hash ) scroll(0,0);
    // void some browsers issue
    setTimeout( function() { scroll(0,0); }, 1);
    $(function() {
        // your current click function
        $('.scroll').on('click', function(e) {
            e.preventDefault();
            $('html, body').animate({
                scrollTop: int($($(this).attr('href')).offset().top) + 'px'
            }, 2000, 'swing');
        });

        // *only* if we have anchor on the url
        if(window.location.hash) {
            new_v_position = $(window.location.hash).offset().top - 100;

            // smooth scroll to the anchor id
            $('html, body').animate({
                scrollTop: new_v_position + 'px'
            }, 2000, 'swing');
        }
    })
});

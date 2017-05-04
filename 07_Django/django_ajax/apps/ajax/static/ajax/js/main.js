// When document is ready:
$( document ).ready(function() {
    console.log( "Ready!" );
    /*
    Note: We're going to use two nested jQuery methods below. The first is the
    `.submit()` method, by which we provide a `<form>` id, of which the function
    will only fire upon form submission. The second method we use, is the `.ajax()`
    method. Tge `.done(), .fail(), .always()` functions are chained additions to
    the primary `ajax()` method, which give us more control and fine tuning. See
    the comments beneath each section for more information on how they function
    and how to configure them.
    */
    $( "#message_form" ).submit(function( event ) { // `#message_form` is the `id` of our `<form>`
        alert( "Handler for .submit() called. Pinging API from server..." );
        // Using the core $.ajax() method (https://learn.jquery.com/ajax/jquery-ajax-methods/)
        $.ajax({
            // The URL for the request
            url: "/message",

            // Omitted data to send (an option)
            // See: https://learn.jquery.com/ajax/jquery-ajax-methods/

            // Whether this is a POST or GET request
            type: "GET",

            // The type of data we expect back
            dataType : "json",
        })
        // Code to run if the request succeeds (is done);
        // The response is passed to the function
        .done(function( response ) {
            $( "<h1>" ).text( response.message ).appendTo( "body" );
        })
        // Code to run if the request fails; the raw request and
        // status codes are passed to the function
        .fail(function( xhr, status, errorThrown ) {
            alert( "Sorry, there was a problem!" );
            console.log( "Error: " + errorThrown );
            console.log( "Status: " + status );
            console.dir( xhr );
        })
        // Code to run regardless of success or failure;
        .always(function( xhr, status ) {
            alert( "The request is complete! Appending returned message to this page via jQuery! This page will update without a refresh!" );
            console.log(status);
        });
        event.preventDefault(); // This prevents the actual form from submitting.
    });
});

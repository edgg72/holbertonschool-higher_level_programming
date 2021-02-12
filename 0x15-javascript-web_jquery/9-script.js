$.getJSON( "https://fourtonfish.com/hellosalut/?lang=fr", function( data ) {
  $('#hello').append('<p>'+ data.hello + '</p>');
});
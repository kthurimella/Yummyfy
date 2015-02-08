//show one question at a time
$( "#next" ).click(function() {
  $( "div" ).first().show( "fast", function showNext() {
    $( this ).next( "div" ).show( "fast", showNext );
  });
});


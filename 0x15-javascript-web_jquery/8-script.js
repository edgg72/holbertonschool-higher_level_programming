$.getJSON( "https://swapi-api.hbtn.io/api/films/?format=json", function( data ) {
  const movies = data.results;
  for (let i in movies) {
    $('#list_movies').append('<li>'+ movies[i].title + '</li>');
  }
});
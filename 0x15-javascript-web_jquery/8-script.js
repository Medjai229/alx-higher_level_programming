$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (response) {
  const results = response.results;
  for (const i in results) {
    $('#list_movies').append('<li>' + results[i].title + '</li>');
  }
});

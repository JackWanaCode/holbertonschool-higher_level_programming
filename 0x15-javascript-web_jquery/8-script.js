$.get('https://swapi.co/api/films/?format=json', function (data) {
  let result = data.results;
  for (let i = 0; i < result.length; i++) {
    let name = $('<li></li>').text(result[i].title);
    $('#list_movies').append(name);
  }
});

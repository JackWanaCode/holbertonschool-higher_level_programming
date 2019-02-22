$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  $('#character').replaceWith(data.name + '<br />');
});

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  $.each(data.results, function (i, episode) {
    $('<li></li>').text(episode.title).appendTo('#list_movies');
    console.log(episode.title);
  });
});

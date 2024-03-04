$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
      const films = data.results;
      const filmsList = $('UL#list_movies');
      $.each(films, function (index, film) {
        filmsList.append('<LI>film.title</LI>');
      });
    }
  });
});

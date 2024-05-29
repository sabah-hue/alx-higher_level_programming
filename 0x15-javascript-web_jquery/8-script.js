$(document).ready(function() {
    var url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    $.getJSON(url, function(data) {
        console.log();
        $.each($(data.results), function (i, e){
            movieName = e.title;
            item = $('<li>').text(movieName);
            $('#list_movies').append(item);
        });
    });
});

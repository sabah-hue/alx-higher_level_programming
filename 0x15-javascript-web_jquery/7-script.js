$(document).ready(function() {
    var url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
    $.getJSON(url, function(data) {
        $('#character').text(data.name);
    });
});

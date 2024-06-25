$(document).ready(function() {
    $("#registration-link").on("click", function(event) {
        event.preventDefault();
        window.location.href = "{% url 'stud_reg' %}";
    });
});
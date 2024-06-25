// Redirect to compdash.html when the login button is clicked
document.addEventListener("DOMContentLoaded", function() {
    var loginButton = document.getElementById("loginButton");
    loginButton.addEventListener("click", function(event) {
        event.preventDefault(); // Prevent the form from submitting
        window.location.href = "compdash.html"; 
    });
});

// Redirect to compreg.html when the registration link is clicked
document.addEventListener("DOMContentLoaded", function() {
    var registrationLink = document.getElementById("newRegistration");
    registrationLink.addEventListener("click", function(event) {
        event.preventDefault(); // Prevent link navigation
        window.location.href = "compreg.html";
    });
});
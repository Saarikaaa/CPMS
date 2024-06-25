document.addEventListener("DOMContentLoaded", function() {
    var loginForm = document.getElementById("login-form");
    loginForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent the form from submitting

        // Get the selected user type
        var userTypeSelect = document.getElementById("user-type");
        var selectedUserType = userTypeSelect.value;

        // Determine the page to redirect based on the selected user type
        var redirectPage;
        switch(selectedUserType) {
            case "hod":
                redirectPage = "hodlogin.html";
                break;
            case "cgpu":
                redirectPage = "cgpulogin.html";
                break;
            default:
                // If no specific page is defined for the selected user type, redirect to a default page
                redirectPage = "default.html";
                break;
        }

        // Redirect to the determined page
        window.location.href = redirectPage;
    });
});
 // JavaScript for showing and hiding notification popup
 function showNotification() {
    var notification = document.getElementById("notification-popup");
    notification.style.display = "block";
}

function closeNotification() {
    var notification = document.getElementById("notification-popup");
    notification.style.display = "none";
}

// Attach click event to the "Notifications" link
document.getElementById("notifications-link").addEventListener("click", function() {
    showNotification();
});

document.getElementById("logout-button").addEventListener("click", function() {
    window.location.href = "users/logout.html"; 
});

document.getElementById("apply").addEventListener("click", function() {
    window.location.href = "applyjob.html"; 
});

document.getElementById("result").addEventListener("click", function() {
    window.location.href = "results.html"; 
});
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

// document.getElementById("logout-button").addEventListener("click", function() {
//     window.location.href = "logout.html"; 
// });

document.getElementById("dashb").addEventListener("click", function() {
    window.location.href = "studdash.html"; 
});

document.getElementById("applyj").addEventListener("click", function() {
    window.location.href = "applyjob.html"; 
});
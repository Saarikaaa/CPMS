
document.addEventListener('DOMContentLoaded', function() {
    const acceptForms = document.querySelectorAll('.accept-form');
    const rejectForms = document.querySelectorAll('.reject-form');

    acceptForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            const acceptBtn = form.querySelector('.accept-btn');
            acceptBtn.innerText = '✓ Accepted';
            acceptBtn.classList.add('accepted');
        });
    });

    rejectForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            const rejectBtn = form.querySelector('.reject-btn');
            rejectBtn.innerText = '✗ Rejected';
            rejectBtn.classList.add('rejected');
        });
    });
});

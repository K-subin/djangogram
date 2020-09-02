const toggleBtn = document.querySelector('.toggleBtn');
const postmodify = document.querySelector('.postmodify')
const postdelete = document.querySelector('.postdelete')

toggleBtn.addEventListener('click', () => {
    postmodify.classList.toggle('active');
    postdelete.classList.toggle('active');
});

$(document).ready(function() {
    $(".dropdown-toggle").dropdown();
});
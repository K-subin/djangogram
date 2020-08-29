const toggleBtn = document.querySelector('.toggleBtn');
const postmodify = document.querySelector('.postmodify')
const postdelete = document.querySelector('.postdelete')
const likebtn = document.querySelector('.btn-like')
const favoritebtn = document.querySelector('.btn-favorite')


toggleBtn.addEventListener('click', () => {
    postmodify.classList.toggle('active');
    postdelete.classList.toggle('active');
    likebtn.classList.toggle('active');
    favoritebtn.classList.toggle('active');
});

$(document).ready(function() {
    $(".dropdown-toggle").dropdown();
});
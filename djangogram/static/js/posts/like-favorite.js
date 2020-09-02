const like = document.querySelector('.like')
const likepush = document.querySelector('.likepush')
const favorite = document.querySelector('.favorite')
const favoritepush = document.querySelector('.favoritepush')

like.classList.toggle('active');
favorite.classList.toggle('active');

function likefavoritepush(toggle){
    if(toggle == like || toggle == likepush){
        toggle.addEventListener('click', () => {
            like.classList.toggle('active');
            likepush.classList.toggle('active');
        })
    }
    else{
        toggle.addEventListener('click', () => {
            favorite.classList.toggle('active');
            favoritepush.classList.toggle('active');
        })
    }
}

likefavoritepush(like);
likefavoritepush(likepush);
likefavoritepush(favorite);
likefavoritepush(favoritepush);
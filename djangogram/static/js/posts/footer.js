var Body = {
    setBackgroundColor:function(color){
        document.querySelector('body').style.backgroundColor=color;
    },
    setColor:function(color){
        document.querySelector('body').style.color=color;
    }
}
function nightDayHandler(toggle, color1, color2){
    toggle.addEventListener('click', () => {
        Body.setBackgroundColor(color1);
        Body.setColor(color2);
        day.classList.toggle('active');
        night.classList.toggle('active');
    })
}

const day = document.querySelector('.day');
const night = document.querySelector('.night');

day.classList.toggle('active');
nightDayHandler(day, '#263343', 'white');
nightDayHandler(night, 'white', '#263343');

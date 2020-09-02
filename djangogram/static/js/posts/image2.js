
const browseBtn = document.querySelector('.browse-btn');
const realInput = document.querySelector('.realInput');
const realimage = document.querySelector('div#file');
const Input = document.querySelector('form.image');

browseBtn.addEventListener('click', ()=>{
    //realInput.click();
    realInput.click();
    //realimage.click();
})


/*
function readURL(input) {
    if(input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            $(#image_section).attr('src', e.target.result);
            $('.bind-img-photo').css({display:"block"})
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$("#imgInput").change(function(){
    readURL(this);
});

function readInputFile(e){
    var sel_files = [];

    sel_files = [];
    $('#imagePreview').empty();

    var files = e.target.files;
    var fileArr = Array.phototype.slice.call(files);
    var index = 0;

    fileArr.forEach(function(f){
        if(!f.type.match("image/.*")){
            alert("이미지 확장자만 업로드 가능합니다.");
            return;
        };
        if(files.length < 11){
            sel_files.push(f);
            var reader = new FileReader();
            reader.onload = function(e){
                var html = '<a id=img_id_${index}><img src=${e.target.result} data-file=${f.name} /><a>';
                $('imagePreview').append(html);
                index++;
            };
            reader.readAsDataURL(f);
        }
    })
    if(files.length > 11){
        alert("최대 10장까지 업로드 할 수 있습니다.");
    }
}*/
function setThumbnail(event){
    for (var image of event.target.files){
        var reader = new FileReader();

        reader.onload = function(event){
            var img = document.createElement("img");
            img.setAttribute("src", event.target.result);
            document.querySelector("div#image_container").appendChild(img);
        };
        console.log(image);
        reader.readAsDataURL(image);
    }
}


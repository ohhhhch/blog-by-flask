document.getElementById('image-upload').addEventListener('change', function() {  
  var file = this.files[0];  
  if (file) {  
    var reader = new FileReader();  
    reader.onload = function(e) {  
      document.getElementById('preview-image').src = e.target.result;  
      document.getElementById('preview-image').style.display = 'block';  
    };  
    reader.readAsDataURL(file);  
  }  
});  
  
document.querySelector('.close-btn').addEventListener('click', function() {  
  var popup = document.getElementById('popup');  
  popup.classList.remove('active'); // 移除 active 类，使元素变为非 active 状态  
});

function toge(){
  let popup = document.getElementById('popup')
  popup.classList.toggle('active')
}
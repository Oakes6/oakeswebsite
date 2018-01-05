var i = 0;
var text = "Welcome, I'm Tanner, software undergraduate.";

function() typeWriter() {
   if (i < txt.length) {
      document.getElementById("welcomemessage").innerHTML += txt.charAt(i);
      i++;
      setTimeout(typeWriter, 50);
   }
}
typeWriter();

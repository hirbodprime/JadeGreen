function myFunction(x) {
    if (x.matches) { 
        document.getElementById("image1-slider").src = "../banner/img1-res.jpg" ;
        document.getElementById("image2-slider").src = "../banner/img2-res.jpg" ;
    } else {
        document.getElementById("image1-slider").src = "../banner/img1.jpg" ;
        document.getElementById("image2-slider").src = "../banner/img2.jpg" ;
    }
}
  
var x = window.matchMedia("(max-width: 768px)")
myFunction(x) 
x.addListener(myFunction) 

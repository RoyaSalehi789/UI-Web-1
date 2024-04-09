//tabs
function switchTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
  }

// modals
var loginclose = document.getElementsByClassName("close")[0];
var registerclose = document.getElementsByClassName("close")[1];
var otpclose = document.getElementsByClassName("close")[2];

function modals(modal, button){
  var modal = document.getElementById(modal);

  if(button == "log-in-btn") {
    modal.style.display = "block";
  }
  if(button == "register-btn") {
    document.getElementById("log-in-modal").style.display = "none";
    modal.style.display = "block";
  }
  if(button == "otp-btn") {
    document.getElementById("register-modal").style.display = "none";
    modal.style.display = "block";
  }
  if(button == "Successfull-btn") {
    document.getElementById("otp-modal").style.display = "none";
    modal.style.display = "block";
  }
  if(button == "back-login-btn") {
    document.getElementById("Successfull-modal").style.display = "none";
    modal.style.display = "block";
  }
  if(button == "cart-btn") {
    modal.style.display = "block";
  }
  if(button == "cart-btn") {
    modal.style.display = "block";
  }
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
  loginclose.onclick = function() {
    modal.style.display = "none";
  }
  registerclose.onclick = function() {
    modal.style.display = "none";
  }
  otpclose.onclick = function() {
    modal.style.display = "none";
  }
}

//otp-inputs
const inputs = document.getElementById("inputs");
 
inputs.addEventListener("input", function (e) {
    const target = e.target;
    const val = target.value;
 
    if (isNaN(val)) {
        target.value = "";
        return;
    }
 
    if (val != "") {
        const next = target.nextElementSibling;
        if (next) {
            next.focus();
        }
    }
});
 
inputs.addEventListener("keyup", function (e) {
    const target = e.target;
    const key = e.key.toLowerCase();
 
    if (key == "backspace" || key == "delete") {
        target.value = "";
        const prev = target.previousElementSibling;
        if (prev) {
            prev.focus();
        }
        return;
    }
});

// color-price
function changePriceByColor(button) {
  switch (button){
    case "gray-color":
      document.getElementById("product-price").innerHTML = "$1999.00"
      break;
    case "blue-color":
      document.getElementById("product-price").innerHTML = "$1899.00"
      break;
    case "black-color":
      document.getElementById("product-price").innerHTML = "$1799.00"
      break;
    case "purple-color":
      document.getElementById("product-price").innerHTML = "$1699.00"
      break;
  }
}

//cart-class
class Product {
  constructor(name, rate, reviewsCont, price, color, description, image) {
    this.name = name;
    this.rate = rate;
    this.reviewsCont = reviewsCont;
    this.price = price;
    this.color = color;
    this.description = description;
    this.image = image;
  }
}
//--iphone-14-pro--
const product1 = new Product(
  "Apple iPhone 14 Pro",
   5.0, 
   121,
   1999.00, 
   "#BEBEC6", 
"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution.", 
"images/image 16 (1).png"
);
const product2 = new Product(
  "Asus ROG Delta S",
   5.0, 
   121,
   250.00, 
   "#BEBEC6", 
"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution.", 
"images/image 16 (1).png"
);

var cartList = [];
cartList.push(product1);
cartList.push(product2);

//product-count-cart
function plusMinus(button) {
  var cont = parseInt(document.getElementById("product-counter").innerHTML);
  if (button == "plus") {
    document.getElementById("product-counter").innerHTML = `${cont + 1}`;
  }
  else {
    if(cont != 0) {
      document.getElementById("product-counter").innerHTML = `${cont - 1}`;
    }
  }
}

//add-to-cart
function addToCart() {
  var productName = document.getElementById("product-name");
  var productprice = document.getElementById("product-price");
  var productNum = document.getElementById("product-count");
  const iphoneNum = document.getElementById("item1");
  const rogNum = document.getElementById("item2");

  var newProduct = new Product(productName, 0, 0, productprice, "", "", "images/image 16 (1).png");

  for (let i = 0 ; i < cartList.length ; i++) {
    if(JSON.stringify(cartList[i]) === JSON.stringify(newProduct)) {
      


    }
    else {
      cartList.push(newProduct);
    }
  }
}




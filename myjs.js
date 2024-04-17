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
  var iphone = document.getElementsByClassName("price-item-cart")[0];
  var iphoneCount = parseInt(iphone.innerHTML.substring(5));
  var itemCount = parseInt(document.getElementById("product-counter").innerHTML);
  var icon = document.getElementById("cart-num");
  var cartNumber = parseInt(icon.innerHTML);
  icon.innerHTML = `${cartNumber + itemCount}`;
  iphone.innerHTML = `QTY: ${iphoneCount + itemCount}`;
}

// delete-item-cart
function deleteItemCart(index) {
  /*remove product*/
  var item = document.getElementsByClassName("delete")[index].parentElement.parentElement.parentElement;
  item.style.display = "none";
  item.nextElementSibling.style.display = "none";
  /*updating cart icon*/
  var product = document.getElementsByClassName("price-item-cart")[index];
  var productCount = parseInt(product.innerHTML.substring(5));
  var icon = document.getElementById("cart-num");
  var cartNumber = parseInt(icon.innerHTML);
  icon.innerHTML = `${cartNumber - productCount}`;
  /*updating cart text*/
  var numberText = parseInt(document.getElementById("item-cart-count-text").innerHTML.substring(0, 1));
  document.getElementById("item-cart-count-text").innerHTML = `${numberText - 1} items`;
}

//scoring
function scoring(index) {
  console.log("Your Rating: " + `${index + 1}`);
  var starBox = document.getElementsByClassName("star")[index];
  var stars = starBox.getElementsByTagName("img");
  var allStars = document.getElementsByClassName("rating")[0].getElementsByTagName("img");

  for (var j = 0 ; j < allStars.length ; j++) {
    allStars[j].src = "icons/star.png";
  }
  for (var j = 0 ; j < stars.length ; j++) {
    stars[j].src = 'icons/Star 2.png';
  }
}
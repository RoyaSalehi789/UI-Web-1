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

// log-in
function modals(modal, button){
  var modal = document.getElementById(modal);
  var btn = document.getElementById(button);

  var loginclose = document.getElementsByClassName("close")[0];
  var registerclose = document.getElementsByClassName("close")[1];
  var otpclose = document.getElementsByClassName("close")[2];


  btn.onclick = function() {
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

  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
}
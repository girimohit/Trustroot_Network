var LoginBtn = document.getElementById("LoginBtn");
var formDiv = document.getElementById("OuterFormDiv");
var innerFormDiv = document.getElementById("innerFormDiv");
var closebtn = document.getElementById("close");

//Toggle form
var signuplink = document.getElementById("SignUpLink");
var signupform = document.getElementById("SignUpForm");
var loginform = document.getElementById("LoginForm");

LoginBtn.addEventListener("click", function (e) {
  e.preventDefault();
  formDiv.style.display = "flex";
});
formDiv.addEventListener("click", function () {
  formDiv.style.display = "none";
});

innerFormDiv.addEventListener("click", function (e) {
  e.stopPropagation();
});

mobileNavIcon = document.getElementById("mobile-navbar-icon");
mobileNavIcon.addEventListener("click", function () {
  document.querySelector(".mobile-links").style.display =
    document.querySelector(".mobile-links").style.display === "flex"
      ? "none"
      : "flex";
});

signuplink.addEventListener("click", function (e) {
  e.preventDefault();
  toggleForms();
});

function toggleForms() {
  loginform.classList.toggle("hidden");
  signupform.classList.toggle("hidden");
}

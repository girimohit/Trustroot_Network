var LoginBtn = document.getElementById("login-signup-btn");
var formDiv = document.getElementById("outer-form-div");
var innerFormDiv = document.getElementById("inner-form-div");
var closebtn = document.getElementById("close");
//Toggle form
var signuplink = document.getElementById("SignUpLink");
var signupform = document.getElementById("signup-form");
var loginform = document.getElementById("login-form");
var textBelowForm = document.getElementById("is-account");

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

signuplink.addEventListener("click", function (e) {
  e.preventDefault();
  toggleForms();
  toggleLinkText();
});

function toggleForms() {
  loginform.classList.toggle("hidden");
  signupform.classList.toggle("hidden");
}

function toggleLinkText() {
  var linkText = signuplink.textContent;
  var innerText = textBelowForm.textContent;
  signuplink.textContent = linkText === "Sign Up" ? "Login" : "Sign Up";
  textBelowForm.textContent =
    innerText === "Don't have an account?" ? "Already have an Account?" : "Don't have an account?";
}

$(document).ready(function () {
  $('input[name="usertype"]').change(function (e) {
    e.preventDefault();
    var typeOfUser = $(this).val();
    var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    // alert(typeOfUser + " checked!");

    $.ajax({
      type: "POST",
      url: "auth/register/",
      data: {
        usertype: typeOfUser,
        csrfmiddlewaretoken: csrftoken,
      },
      dataType: "json",
      success: function (response) {
        $("#extra-fields").html(response.additional_fields);
      },
    });
  });
});

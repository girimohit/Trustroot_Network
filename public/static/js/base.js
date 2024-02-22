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
    innerText === "Don't have an account?"
      ? "Already have an Account?"
      : "Don't have an account?";
}

// mobileNavIcon = document.getElementById("mobile-navbar-icon");
// mobileNavIcon.addEventListener("click", function () {
//   document.querySelector(".mobile-links").style.display =
//     document.querySelector(".mobile-links").style.display === "flex"
//       ? "none"
//       : "flex";
// });







$(document).ready(function() {
  $('#signup-form').submit(function(e) {
      e.preventDefault(); // Prevent default form submission
      
      // Serialize form data
      var formData = $(this).serialize();
      
      // Send AJAX request
      $.ajax({
          type: 'POST',
          url: '{% url "register_user" %}', // Replace 'register_modal' with your actual URL name
          data: formData,
          success: function(response) {
              // Handle success response
              console.log(response);
              // Optionally, you can close the modal or show a success message here
          },
          error: function(xhr, status, error) {
              // Handle error response
              console.error(xhr.responseText);
              // Optionally, you can display an error message here
          }
      });
  });
});

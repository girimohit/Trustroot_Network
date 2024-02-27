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

/* --------------------- FOR DYNAMICALLY FORM RENDERING --------------------- */
// $(document).ready(function () {
//   // Initially hide all the additional fields
//   $(".additional-fields").hide();

//   // Show the fields based on the selected radio button
//   $('input[type="radio"][name="userType"]').change(function () {
//     var userType = $(this).val();
//     $(".additional-fields").hide();
//     $("#" + userType + "-fields").show();
//   });
// });

$(document).ready(function () {
  $(".user-specific-fields").hide();
  $('input[type="radio"][name="userType"]').change(function () {
    var userType = $(this).val();
    $(".user-specific-fields").hide();
    $("#" + userType + "-fields").show();
  });
});

/* -------------------------------------------------------------------------- */
/*                                FOR FAQ PAGE                                */
/* -------------------------------------------------------------------------- */
document.addEventListener("DOMContentLoaded", function () {
  const questions = document.querySelectorAll(".question");

  questions.forEach((question) => {
    question.addEventListener("click", function () {
      const answer = this.nextElementSibling;
      if (answer.style.display === "block") {
        answer.style.display = "none";
      } else {
        answer.style.display = "block";
      }
    });
  });
});

// $(document).ready(function () {
//   $(".user-specific-fields").hide();
//   $('input[type="radio"][name="userType"]').change(function () {
//     var userType = $(this).val();
//     $(".user-specific-fields").hide().find(':input').prop('disabled', true);
//     $("#" + userType + "-fields").show().find(':input').prop('disabled', false);
//   });
// });

// $(document).ready(function () {
//   $(".user-specific-fields").hide();

//   $('input[type="radio"][name="userType"]').change(function () {
//     var userType = $(this).val();
//     $(".user-specific-fields").hide();

//     $.ajax({
//       url: '{% url "base:fetchFields" %}',
//       type: "GET",
//       data: {
//         userType: userType,
//       },
//       success: function (data) {
//         // $("#" + userType + "-fields")
//         //   .html(data)
//         //   .show();
//         $("#get-field").htm(data);
//       },
//     });
//   });
// });

// document.getElementById("grassroot-fields").querySelector("#id_org_name").disabled = true;
// document.getElementById("grassroot-fields").querySelector("#id_description").disabled = true;

// // document.getElementById("donor-fields").querySelector("#id_phone").disabled = true;
// // document.getElementById("donor-fields").querySelector("#id_paymentMethod").disabled = true;
// // document.getElementById("donor-fields").querySelector("#id_firmName").disabled = true;

// document.getElementById("community-fields").querySelector("#id_fullName").disabled = true;
// document.getElementById("community-fields").querySelector("#id_age").disabled = true;
// document.getElementById("community-fields").querySelector("#id_location").disabled = true;

// Function to disable all user-specific fields
// function disableUserSpecificFields() {
//   document
//     .querySelectorAll(".user-specific-fields input")
//     .forEach(function (input) {
//       input.disabled = true;
//     });
// }

// // Function to enable fields based on userType
// function enableFieldsForUserType(userType) {
//   // First, disable all fields
//   disableUserSpecificFields();

//   // Then, enable fields based on userType
//   if (userType === "grassroot") {
//     document
//       .querySelectorAll("#grassroot-fields input")
//       .forEach(function (input) {
//         input.disabled = false;
//       });
//   } else if (userType === "donor") {
//     document.querySelectorAll("#donor-fields input").forEach(function (input) {
//       input.disabled = false;
//     });
//   } else if (userType === "community") {
//     document
//       .querySelectorAll("#community-fields input")
//       .forEach(function (input) {
//         input.disabled = false;
//       });
//   }
// }

// // Event listener for userType change
// document.querySelectorAll('input[name="userType"]').forEach(function (radio) {
//   radio.addEventListener("change", function () {
//     enableFieldsForUserType(this.value);
//   });
// });

// // Initially disable all fields
// disableUserSpecificFields();

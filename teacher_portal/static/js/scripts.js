// Toggle password visibility
togglePasswordBtn.addEventListener("click", () => {
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    togglePasswordBtn.innerHTML = '<i class="fa-solid fa-eye-slash"></i>';
  } else {
    passwordInput.type = "password";
    togglePasswordBtn.innerHTML = '<i class="fa-solid fa-eye"></i>';
  }
});

// Login form submission
loginForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  // Simple validation for demo
  if (username && password) {
    loginPage.style.display = "none";
    dashboard.style.display = "block";
    renderRecordsTable();
  } else {
    alert("Please enter both username and password");
  }
});

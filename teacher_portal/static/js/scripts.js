// Toggle Popup Modal
function togglePopup(id) {
  const popupId = id ? `recordModal-${id}` : "recordModal";
  const popup = document.getElementById(popupId);

  if (!popup) return;

  const isOpen = popup.style.display === "flex";
  popup.style.display = isOpen ? "none" : "flex";

  function handleOutsideClick(e) {
    if (e.target === popup) {
      popup.style.display = "none";
      document.removeEventListener("click", handleOutsideClick);
    }
  }

  if (!isOpen) {
    setTimeout(() => {
      document.addEventListener("click", handleOutsideClick);
    }, 0);
  }
}


// Login form submission
const loginForm = document.getElementById("loginForm");
if (loginForm) {
  loginForm.addEventListener("submit", (e) => {
    console.log("Login form submitted.");
    //   e.preventDefault();
    //   const username = document.getElementById("username").value;
    //   const password = document.getElementById("password").value;

    //   // Simple validation for demo
    //   if (username && password) {

    //   } else {
    //     alert("Please enter both username and password");
    //   }
  });
}
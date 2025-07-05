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
    // Show a loader
    // showLoader();
  });
}

// // Toast Notification Functions
// function showToast(type, message, duration = 5000) {
//   const toastContainer = document.getElementById("toastContainer");

//   // Create toast element
//   const toast = document.createElement("div");
//   toast.className = `toast ${type}`;
//   toast.innerHTML = `
//       <div class="toast-icon">
//           ${
//             type === "success"
//               ? '<i class="fas fa-check-circle"></i>'
//               : type === "error"
//               ? '<i class="fas fa-exclamation-circle"></i>'
//               : type === "warning"
//               ? '<i class="fas fa-exclamation-triangle"></i>'
//               : '<i class="fas fa-info-circle"></i>'
//           }
//       </div>
//       <div class="toast-content">
//           <div class="toast-message">${message}</div>
//       </div>
//       <button class="toast-close">&times;</button>
//   `;

//   // Add to container
//   // toastContainer.appendChild(toast);

//   // Trigger reflow to enable animation
//   void toast.offsetWidth;
//   toast.classList.add("show");

//   // Auto remove after duration
//   setTimeout(() => {
//     toast.classList.remove("show");
//     setTimeout(() => {
//       toast.remove();
//     }, 300);
//   }, duration);

//   // Close button functionality
//   const closeBtn = toast.querySelector(".toast-close");
//   closeBtn.addEventListener("click", () => {
//     toast.classList.remove("show");
//     setTimeout(() => {
//       toast.remove();
//     }, 300);
//   });
// }

// Loader Functions
function showLoader() {
  const loader = document.getElementById("loader");
  loader.classList.add("show");
}

// function hideLoader() {
//   const loader = document.getElementById("loader");
//   loader.classList.remove("show");
// }

// Show a success toast
// showToast('success', 'Login Successful');
// showToast("success", "You have been successfully logged in!");
// Show an error toast
// showToast('error', 'Invalid username or password');

// Show loader on form submit.
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("form").forEach((form) => {
    form.addEventListener("submit", showLoader);
  });
});

// Toast Notification Functions
function showToast(type, message, duration = 5000) {
  const toastContainer = document.getElementById("toastContainer");

  // Create toast element
  const toast = document.createElement("div");
  toast.className = `toast ${type}`;
  toast.innerHTML = `
        <div class="toast-icon">
            ${
              type === "success"
                ? '<i class="fas fa-check-circle"></i>'
                : type === "error"
                ? '<i class="fas fa-exclamation-circle"></i>'
                : type === "warning"
                ? '<i class="fas fa-exclamation-triangle"></i>'
                : '<i class="fas fa-info-circle"></i>'
            }
        </div>
        <div class="toast-content">
            <div class="toast-message">${message}</div>
        </div>
        <button class="toast-close">&times;</button>
    `;

  // Add to container
  toastContainer.appendChild(toast);

  // Trigger reflow to enable animation
  void toast.offsetWidth;
  toast.classList.add("show");

  // Auto remove after duration
  setTimeout(() => {
    toast.classList.remove("show");
    setTimeout(() => {
      toast.remove();
    }, 300);
  }, duration);

  // Close button functionality
  const closeBtn = toast.querySelector(".toast-close");
  closeBtn.addEventListener("click", () => {
    toast.classList.remove("show");
    setTimeout(() => {
      toast.remove();
    }, 300);
  });
}

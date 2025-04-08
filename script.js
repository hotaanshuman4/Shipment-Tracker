// LOGIN FUNCTION
function login() {
    const u = document.getElementById("username").value;
    const p = document.getElementById("password").value;
    const error = document.getElementById("login-error");
  
    if (users[u] && users[u] === p) {
      localStorage.setItem("loggedIn", "true");
      window.location.href = "chatbot.html";
    } else {
      error.textContent = "Invalid username or password.";
    }
  }
  
  // CHATBOT FUNCTION
  function sendTracking() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (message === "") return;
  
    displayMessage(message, "user");
  
    const response =
      trackingData[message] || "❌ Tracking ID not found!";
    setTimeout(() => displayMessage(response, "bot"), 500);
  
    input.value = "";
  }
  
  function displayMessage(text, sender) {
    const chatBox = document.getElementById("chat-box");
    const msg = document.createElement("div");
    msg.className = `message ${sender}`;
    msg.textContent = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
  }
  
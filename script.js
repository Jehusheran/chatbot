function sendMessage() {
    let userText = document.getElementById("userInput").value;
    let chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += "<div><b>You:</b> " + userText + "</div>";
  
    fetch("/get", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: userText })
    })
    .then(response => response.json())
    .then(data => {
      chatBox.innerHTML += "<div><b>Bot:</b> " + data.response + "</div>";
      document.getElementById("userInput").value = "";
      chatBox.scrollTop = chatBox.scrollHeight;
    });
  }
  
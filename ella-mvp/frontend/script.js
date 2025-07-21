async function sendMessage() {
  const input = document.getElementById("userInput");
  const chatbox = document.getElementById("chatbox");
  const message = input.value;
  if (!message) return;

  chatbox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
  input.value = "";

  const res = await fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message})
  });

  const data = await res.json();
  chatbox.innerHTML += `<p><strong>Ella:</strong> ${data.response}</p>`;
  chatbox.scrollTop = chatbox.scrollHeight;
}

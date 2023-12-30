// Getting essential elements from the DOM
const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");

// Predefined messages that the bot can send
const BOT_MSGS = [
  "Hi, how are you?",
  "Ohh... I can't understand what you trying to say. Sorry!",
  "I like to play games... But I don't know how to play!",
  "Sorry if my answers are not relevant. :))",
  "I feel sleepy! :(",
];

// URLs for the bot and person images
const BOT_IMG = "https://image.flaticon.com/icons/svg/327/327779.svg";
const PERSON_IMG = "https://image.flaticon.com/icons/svg/145/145867.svg";

// Names for the bot and the user
const BOT_NAME = "AI";
const PERSON_NAME = "User";

// Event listener for the form submission
msgerForm.addEventListener("submit", (event) => {
  event.preventDefault(); // Prevents the default form submission action

  const msgText = msgerInput.value; // Gets the input text
  if (!msgText) return; // If no text is entered, do nothing

  // Append the message to the chat
  appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
  msgerInput.value = ""; // Clear the input field

  botResponse(); // Call the function to simulate the bot's response
});

// Function to append a message to the chat
function appendMessage(name, img, side, text) {
  // HTML structure for the message
  const msgHTML = `
    <div class="msg ${side}-msg">
      <div class="msg-img" style="background-image: url(${img})"></div>

      <div class="msg-bubble">
        <div class="msg-info">
          <div class="msg-info-name">${name}</div>
          <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>

        <div class="msg-text">${text}</div>
      </div>
    </div>
  `;

  // Insert the message HTML into the chat
  msgerChat.insertAdjacentHTML("beforeend", msgHTML);
  // Scroll to the bottom of the chat
  msgerChat.scrollTop += 500;
}

// Function to simulate a bot response
function botResponse() {
  // Choose a random message from the predefined list
  const r = random(0, BOT_MSGS.length - 1);
  const msgText = BOT_MSGS[r];
  // Delay the response based on the message length
  const delay = msgText.split(" ").length * 100;

  setTimeout(() => {
    // Append the bot's message to the chat after the delay
    appendMessage(BOT_NAME, BOT_IMG, "left", msgText);
  }, delay);
}

// Utility function to get an element by selector
function get(selector, root = document) {
  return root.querySelector(selector);
}

// Utility function to format the date as HH:MM
function formatDate(date) {
  const h = "0" + date.getHours();
  const m = "0" + date.getMinutes();

  return `${h.slice(-2)}:${m.slice(-2)}`;
}

// Utility function to generate a random number between min and max
function random(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
}

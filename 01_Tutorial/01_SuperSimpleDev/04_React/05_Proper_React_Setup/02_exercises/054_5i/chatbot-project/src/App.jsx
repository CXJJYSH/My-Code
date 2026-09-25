// Packages
import { useState, useEffect } from "react"; // 没有/是node_modules，有/是public，./是正常路径。
import { Chatbot } from "supersimpledev";
// JS
import { ChatInput } from "./components/ChatInput";
import { ChatMessages } from "./components/ChatMessages";
// Other types
import "./App.css"; // ./ = the current folder

function App() {
  const [chatMessages, setChatMessages] = useState([]);
  // Array Destructuring, the order matters
  // const chatMessages = array[0];
  // const setChatMessages = array[1]; // updater function

  useEffect(() => {
    Chatbot.addResponses({
      goodbye: "Goodbye. Have a great day!",
      "give me a unique id": function () {
        return `Sure! Here's a unique ID: ${crypto.randomUUID()}`;
      },
    });
  });
  // [] tells useEffect to only run once. We only want to run this setup code once because we only want to add these extra responses once.
  // 2026.09.25 23:35

  return (
    <div className="app-container">
      {chatMessages.length === 0 && (
        <p className="welcome-message">
          Welcome to the chatbot project! Send a message using the textbox
          below.
        </p>
      )}
      <ChatMessages chatMessages={chatMessages} />
      <ChatInput
        chatMessages={chatMessages}
        setChatMessages={setChatMessages}
      />
    </div>
  );
}

export default App;

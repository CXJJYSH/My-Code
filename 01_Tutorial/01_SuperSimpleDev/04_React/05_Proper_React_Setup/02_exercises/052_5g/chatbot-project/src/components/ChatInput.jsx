import { useState } from "react";
import { Chatbot } from "supersimpledev";
import LoadingImage from "../assets/loading-spinner.gif";
import "./ChatInput.css";

// In React, the component name must start with a capital letter.
export function ChatInput({ chatMessages, setChatMessages }) {
  const [inputText, setInputText] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  function saveInputText(event) {
    setInputText(event.target.value);
    // event.target = gives us the element that we're typing in
  }

  async function sendMessage() {
    if (isLoading || inputText === "") {
      return;
    }

    // Set isLoading to true at the start, and set it to false after everything is done.
    setIsLoading(true);

    // We can put this at the top of the function or after the first setChatMessages(). Both work.
    setInputText("");

    const newChatMessages = [
      ...chatMessages, // Add a new chat message at the end
      {
        message: inputText,
        sender: "user",
        id: crypto.randomUUID(),
      },
    ];

    setChatMessages([
      ...newChatMessages,
      {
        message: <img src={LoadingImage} className="loading-spinner" />,
        sender: "robot",
        id: crypto.randomUUID(),
      },
      // This creates a temporary Loading... message.
      // Because we don't save this message in newChatMessages,
      // it will be remove later, when we add the response.
    ]);

    const response = await Chatbot.getResponseAsync(inputText);
    setChatMessages([
      ...newChatMessages, // Add a new chat message at the end
      {
        message: response,
        sender: "robot",
        id: crypto.randomUUID(),
      },
    ]); // New value of chatMessages

    // Set isLoading to false after everything is done.
    setIsLoading(false);
  }

  function handleKeyDown(event) {
    if (event.key === "Enter") {
      sendMessage();
    }

    if (event.key === "Escape") {
      // 这里不能写Esc，要写Escape。
      setInputText("");
    }
    // 这里用if或else if都可以。
  }

  return (
    <div className="chat-input-container">
      <input
        placeholder="Send a message to Chatbot"
        size="30"
        onChange={saveInputText}
        // onKeyDown={event.key === "Enter" && sendMessage}
        // 上面这样写不行，下面这样写可以。Simon创建了一个新函数，我也和他一样吧。
        // onKeyDown={(event) => event.key === "Enter" && sendMessage()}
        onKeyDown={handleKeyDown}
        value={inputText}
        className="chat-input"
        // onChange = runs a function when we change the text inside an <input>
      />
      <button onClick={sendMessage} className="send-button">
        Send
      </button>
    </div>
  );
}
// JSX is more strict than normal HTML.
// All elements need a closing tag.
// Shortcut for: <input></input>
// Self-closing element
// size: character

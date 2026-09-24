// Packages
import { useState } from "react"; // 没有/是node_modules，有/是public，./是正常路径。
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

// Packages
import { useState, useEffect } from "react"; // 没有/是node_modules，有/是public，./是正常路径。

// 这句有标红，但是我不知道怎么改成正确的。先改成注释吧。
import { Chatbot } from "supersimpledev";

// JS
import { ChatInput } from "./components/ChatInput";
import { ChatMessages } from "./components/ChatMessages";
// Other types
import RobotProfileImage from "./assets/robot.png";
import "./App.css"; // ./ = the current folder

function App() {
  const [chatMessages, setChatMessages] = useState(
    JSON.parse(localStorage.getItem("messages") || "[]"),
  );
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
    // [] tells useEffect to only run once. We only want to run this setup code once because we only want to add these extra responses once.
    // 2026.09.25 23:35
  }, []);

  useEffect(() => {
    localStorage.setItem("messages", JSON.stringify(chatMessages));
  }, [chatMessages]);

  // Note: in React, <title>{chatMessages.length} Messages</title>
  // counts as putting 2 pieces of text in <title> like this:
  // <title>{chatMessages.length} {'Messages'}</title>
  //
  // The <title> element may not support this. That's why we
  // save it in a variable first and insert it as 1 text.
  const title = `${chatMessages.length} Messages`;

  return (
    <>
      <title>{title}</title>
      <link rel="icon" type="image/svg+xml" href={RobotProfileImage} />

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
    </>
  );
}

export default App;

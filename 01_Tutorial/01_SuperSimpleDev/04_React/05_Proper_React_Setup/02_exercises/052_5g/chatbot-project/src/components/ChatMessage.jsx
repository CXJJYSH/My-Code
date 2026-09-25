import RobotProfileImage from "../assets/robot.png";
import UserProfileImage from "../assets/profile-1.jpg";
import "./ChatMessage.css";

export function ChatMessage({ message, sender }) {
  // console.log(props);
  // props = properties
  // Props make our component reusable.

  // const { message, sender } = props;
  // Destructuring

  return (
    <div
      className={sender === "user" ? "chat-message-user" : "chat-message-robot"}
    >
      {sender === "robot" && (
        <img src={RobotProfileImage} className="chat-message-profile" />
      )}
      <div className="chat-message-text">{message}</div>
      {sender === "user" && (
        <img src={UserProfileImage} className="chat-message-profile" />
      )}
    </div>
  );
}

console.log(UserProfileImage);

import { ChatMessage } from "./ChatMessage";
import { useAutoScroll } from "./UseAutoScroll";
import "./ChatMessages.css";

type ChatMessagesProps = {
  chatMessages: {
    id: string;
    message: string;
    sender: string;
    time: string;
  }[];
};

export function ChatMessages({ chatMessages }: ChatMessagesProps) {
  const chatMessagesRef = useAutoScroll([chatMessages]);

  return (
    <div className="chat-messages-container" ref={chatMessagesRef}>
      {chatMessages.map((chatMessage) => {
        return (
          <ChatMessage
            message={chatMessage.message}
            sender={chatMessage.sender}
            time={chatMessage.time}
            key={chatMessage.id}
          />
        );
      })}
    </div>
  );
}

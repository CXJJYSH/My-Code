import { useRef, useEffect } from "react";

// To use a function as a hook, the function name must start with "use".
export function useAutoScroll(dependencies) {
  // It's highly recommend to rename chatMessagesRef to something more generic like containerRef.
  // This will make the code make more sense if we ever reuse this code in other components.
  const containerRef = useRef(null);

  useEffect(() => {
    const containerElem = containerRef.current;
    if (containerElem) {
      containerElem.scrollTop = containerElem.scrollHeight;
    }
  }, dependencies);

  return containerRef;
}

// 卧槽，这里自己写一个用了useRef又用了useEffect的hook好绕。
// 虽然效果是直白的，但是代码就要层层递进好几次，好不直白。

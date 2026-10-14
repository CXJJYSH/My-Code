import { useState } from "react";
// import "./App.css";

type SquareProps = {
  value: string;
  onSquareClick: () => void;
};

type BoardProps = {
  xIsNext: boolean;
  currentSquares: string[];
  onPlay: (nextSquares: string[]) => void;
};

function Square({ value, onSquareClick }: SquareProps) {
  return (
    <button className="square" onClick={onSquareClick}>
      {value}
    </button>
  );
}

function Board({ xIsNext, currentSquares, onPlay }: BoardProps) {
  function handleClick(i: number) {
    // 这里写得很巧妙啊，要么继续落子，要么没地方落子了该计算胜者了。
    if (currentSquares[i] || calculateWinner(currentSquares)) {
      return;
    }

    const nextSquares = currentSquares.slice();

    if (xIsNext) {
      nextSquares[i] = "X";
    } else {
      nextSquares[i] = "O";
    }

    onPlay(nextSquares);
  }

  const winner = calculateWinner(currentSquares);
  let status;
  if (winner) {
    status = "Winner: " + winner;
  } else {
    status = "Next player: " + (xIsNext ? "X" : "O");
  }

  return (
    <>
      <div className="status">{status}</div>
      <div className="board-row">
        <Square
          value={currentSquares[0]}
          onSquareClick={() => handleClick(0)}
        />
        <Square
          value={currentSquares[1]}
          onSquareClick={() => handleClick(1)}
        />
        <Square
          value={currentSquares[2]}
          onSquareClick={() => handleClick(2)}
        />
      </div>
      <div className="board-row">
        <Square
          value={currentSquares[3]}
          onSquareClick={() => handleClick(3)}
        />
        <Square
          value={currentSquares[4]}
          onSquareClick={() => handleClick(4)}
        />
        <Square
          value={currentSquares[5]}
          onSquareClick={() => handleClick(5)}
        />
      </div>
      <div className="board-row">
        <Square
          value={currentSquares[6]}
          onSquareClick={() => handleClick(6)}
        />
        <Square
          value={currentSquares[7]}
          onSquareClick={() => handleClick(7)}
        />
        <Square
          value={currentSquares[8]}
          onSquareClick={() => handleClick(8)}
        />
      </div>
    </>
  );
}

export default function Game() {
  const [history, setHistory] = useState([Array(9).fill("")]);
  const [currentMove, setCurrentMove] = useState(0);
  const currentSquares = history[currentMove];
  // currentMove在state中会随时修改，所以依赖currentMove的xIsNext也会随时修改。
  const xIsNext = currentMove % 2 === 0;

  function handlePlay(nextSquares: string[]) {
    const nextHistory = [...history.slice(0, currentMove + 1), nextSquares];
    setHistory(nextHistory);
    setCurrentMove(nextHistory.length - 1);
  }

  function jumpTo(currentMove: number) {
    setCurrentMove(currentMove);
  }

  // squares是元素
  // move是元素的索引
  // squares可以用_替代，因为遍历过程中确实没用到，用_表示这个参数存在，但不需要用它。
  const moves = history.map((_, move) => {
    let description;

    if (move > 0) {
      description = "Go to move #" + move;
    } else {
      description = "Go to game Start";
    }

    return (
      <li key={move}>
        <button onClick={() => jumpTo(move)}>{description}</button>
      </li>
    );
  });

  return (
    <div className="game">
      <div className="game-board">
        <Board
          xIsNext={xIsNext}
          currentSquares={currentSquares}
          onPlay={handlePlay}
        />
      </div>

      <div className="game-info">
        <ol>{moves}</ol>
      </div>
    </div>
  );
}

function calculateWinner(squares: string[]) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];

  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }

  return null;
}

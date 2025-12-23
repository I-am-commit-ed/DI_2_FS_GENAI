"use client";

import { useState } from "react";
import Grid from "./components/Grid";
import Keyboard from "./components/Keyboard";

const WORD_LIST = [
  "REACT", "REDUX", "ASYNC", "FETCH", "CACHE",
  "DEBUG", "BUILD", "MERGE", "CLONE", "STACK",
  "QUEUE", "ARRAY", "LOOPS", "CLASS", "SCOPE",
  "HOOKS", "STATE", "PROPS", "ROUTE", "WRITE"
];

export default function Home() {
  const [targetWord] = useState(() =>
    WORD_LIST[Math.floor(Math.random() * WORD_LIST.length)]
  );
  const [guesses, setGuesses] = useState<string[]>([]);
  const [currentGuess, setCurrentGuess] = useState("");
  const [gameStatus, setGameStatus] = useState<"playing" | "won" | "lost">("playing");

  const handleKeyPress = (key: string) => {
    if (gameStatus !== "playing") return;

    if (key === "ENTER") {
      if (currentGuess.length !== 5) return;

      const newGuesses = [...guesses, currentGuess];
      setGuesses(newGuesses);

      if (currentGuess === targetWord) {
        setGameStatus("won");
      } else if (newGuesses.length === 6) {
        setGameStatus("lost");
      }

      setCurrentGuess("");
    } else if (key === "BACKSPACE") {
      setCurrentGuess(currentGuess.slice(0, -1));
    } else if (currentGuess.length < 5 && /^[A-Z]$/.test(key)) {
      setCurrentGuess(currentGuess + key);
    }
  };

  const getLetterStatus = (letter: string, position: number, word: string): "correct" | "present" | "absent" => {
    if (targetWord[position] === letter) return "correct";
    if (targetWord.includes(letter)) return "present";
    return "absent";
  };

  return (
    <div className="min-h-screen bg-zinc-900 text-white flex flex-col items-center justify-center p-4">
      <div className="max-w-lg w-full">
        <h1 className="text-4xl font-bold text-center mb-2">DEV WORDLE</h1>
        <p className="text-center text-zinc-400 mb-8">Guess the programming term</p>

        <Grid
          guesses={guesses}
          currentGuess={currentGuess}
          targetWord={targetWord}
          getLetterStatus={getLetterStatus}
        />

        {gameStatus === "won" && (
          <div className="text-center mt-6 text-2xl font-bold text-green-400">
            You won! 🎉
          </div>
        )}

        {gameStatus === "lost" && (
          <div className="text-center mt-6">
            <div className="text-2xl font-bold text-red-400">Game Over!</div>
            <div className="text-zinc-400">The word was: {targetWord}</div>
          </div>
        )}

        <Keyboard
          onKeyPress={handleKeyPress}
          guesses={guesses}
          targetWord={targetWord}
        />
      </div>
    </div>
  );
}
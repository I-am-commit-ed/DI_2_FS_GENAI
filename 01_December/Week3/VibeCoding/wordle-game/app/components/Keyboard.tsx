import { useEffect } from "react";

type KeyboardProps = {
  onKeyPress: (key: string) => void;
  guesses: string[];
  targetWord: string;
};

const KEYBOARD_ROWS = [
  ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
  ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
  ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "BACKSPACE"],
];

export default function Keyboard({ onKeyPress, guesses, targetWord }: KeyboardProps) {
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      const key = e.key.toUpperCase();

      if (key === "ENTER") {
        onKeyPress("ENTER");
      } else if (key === "BACKSPACE") {
        onKeyPress("BACKSPACE");
      } else if (/^[A-Z]$/.test(key)) {
        onKeyPress(key);
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [onKeyPress]);

  const getKeyStatus = (key: string): "correct" | "present" | "absent" | "unused" => {
    if (key === "ENTER" || key === "BACKSPACE") return "unused";

    let status: "correct" | "present" | "absent" | "unused" = "unused";

    guesses.forEach((guess) => {
      guess.split("").forEach((letter, index) => {
        if (letter === key) {
          if (targetWord[index] === key) {
            status = "correct";
          } else if (targetWord.includes(key) && status !== "correct") {
            status = "present";
          } else if (!targetWord.includes(key) && status === "unused") {
            status = "absent";
          }
        }
      });
    });

    return status;
  };

  const getKeyColor = (status: "correct" | "present" | "absent" | "unused") => {
    switch (status) {
      case "correct":
        return "bg-green-600 hover:bg-green-700";
      case "present":
        return "bg-yellow-600 hover:bg-yellow-700";
      case "absent":
        return "bg-zinc-700 hover:bg-zinc-600";
      default:
        return "bg-zinc-500 hover:bg-zinc-400";
    }
  };

  return (
    <div className="flex flex-col gap-2 mt-8">
      {KEYBOARD_ROWS.map((row, rowIndex) => (
        <div key={rowIndex} className="flex gap-1 justify-center">
          {row.map((key) => {
            const status = getKeyStatus(key);
            const isSpecial = key === "ENTER" || key === "BACKSPACE";

            return (
              <button
                key={key}
                onClick={() => onKeyPress(key)}
                className={`${isSpecial ? "px-3" : "px-4"
                  } py-5 rounded font-bold text-xs ${getKeyColor(status)} transition-colors`}
              >
                {key === "BACKSPACE" ? "←" : key}
              </button>
            );
          })}
        </div>
      ))}
    </div>
  );
}

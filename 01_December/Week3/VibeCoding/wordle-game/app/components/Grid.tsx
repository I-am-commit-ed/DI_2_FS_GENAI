import Tile from "./Tile";

type GridProps = {
  guesses: string[];
  currentGuess: string;
  targetWord: string;
  getLetterStatus: (letter: string, position: number, word: string) => "correct" | "present" | "absent";
};

export default function Grid({ guesses, currentGuess, targetWord, getLetterStatus }: GridProps) {
  const rows = 6;
  const cols = 5;

  const getRow = (rowIndex: number) => {
    if (rowIndex < guesses.length) {
      return guesses[rowIndex];
    } else if (rowIndex === guesses.length) {
      return currentGuess.padEnd(cols, " ");
    } else {
      return " ".repeat(cols);
    }
  };

  return (
    <div className="flex flex-col gap-1 mb-8">
      {Array.from({ length: rows }).map((_, rowIndex) => {
        const word = getRow(rowIndex);
        const isGuessed = rowIndex < guesses.length;

        return (
          <div key={rowIndex} className="flex gap-1 justify-center">
            {Array.from({ length: cols }).map((_, colIndex) => {
              const letter = word[colIndex] || "";
              const status = isGuessed && letter !== " "
                ? getLetterStatus(letter, colIndex, word)
                : "empty";

              return (
                <Tile
                  key={colIndex}
                  letter={letter}
                  status={status}
                />
              );
            })}
          </div>
        );
      })}
    </div>
  );
}

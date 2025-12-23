type TileProps = {
  letter: string;
  status?: "correct" | "present" | "absent" | "empty";
};

export default function Tile({ letter, status = "empty" }: TileProps) {
  const getBackgroundColor = () => {
    switch (status) {
      case "correct":
        return "bg-green-600";
      case "present":
        return "bg-yellow-600";
      case "absent":
        return "bg-zinc-700";
      default:
        return "bg-zinc-800 border-2 border-zinc-600";
    }
  };

  return (
    <div
      className={`w-14 h-14 flex items-center justify-center text-2xl font-bold uppercase ${getBackgroundColor()} transition-all duration-200`}
    >
      {letter}
    </div>
  );
}

const btn = document.getElementById("moveBtn");
const box = document.getElementById("animate");
const container = document.getElementById("container");

let moveIntervalId = null;

function myMove() {
  // prevent multiple intervals if user clicks many times
  if (moveIntervalId !== null) return;

  let pos = 0;

  // max left position = container width - box width
  const maxPos = container.clientWidth - box.clientWidth;

  moveIntervalId = setInterval(() => {
    if (pos >= maxPos) {
      clearInterval(moveIntervalId);
      moveIntervalId = null;
      return;
    }

    pos += 1;
    box.style.left = pos + "px";
  }, 1);
}

btn.addEventListener("click", myMove);

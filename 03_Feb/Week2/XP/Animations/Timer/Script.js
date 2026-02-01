// ===== Part I =====
// After 2 seconds, alert "Hello World"
setTimeout(() => {
  alert("Hello World");
}, 2000);

// ===== Part II =====
// After 2 seconds, add <p>Hello World</p> inside #container
setTimeout(() => {
  const container = document.getElementById("container");
  const p = document.createElement("p");
  p.textContent = "Hello World";
  container.appendChild(p);
}, 2000);

// ===== Part III =====
// Every 2 seconds, add a paragraph.
// Stop when user clicks the button OR when there are 5 paragraphs.
const container = document.getElementById("container");
const clearBtn = document.getElementById("clear");

let intervalId = setInterval(() => {
  const p = document.createElement("p");
  p.textContent = "Hello World";
  container.appendChild(p);

  // stop automatically when there are 5 paragraphs
  const paragraphsCount = container.querySelectorAll("p").length;
  if (paragraphsCount >= 5) {
    clearInterval(intervalId);
    intervalId = null;
  }
}, 2000);

// stop when user clicks the button
clearBtn.addEventListener("click", () => {
  if (intervalId !== null) {
    clearInterval(intervalId);
    intervalId = null;
  }
});

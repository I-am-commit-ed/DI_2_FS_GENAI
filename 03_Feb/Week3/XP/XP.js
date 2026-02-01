/***********************
 * 🌟 Exercise 1: Scope
 ***********************/

// #1
function funcOne() {
  let a = 5;
  if (a > 1) {
    a = 3;
  }
  alert(`inside the funcOne function ${a}`);
}
// Prediction:
// When calling funcOne(), alert shows: "inside the funcOne function 3"
// Why: a starts 5, condition true, then reassigned to 3.
//
// #1.2 If a is const instead of let?
// const a = 5; then inside if: a = 3; -> TypeError (cannot reassign a const).

// #2
let a = 0;
function funcTwo() {
  a = 5; // reassigns the global a
}
function funcThree() {
  alert(`inside the funcThree function ${a}`);
}
// Prediction for sequence:
// funcThree()  -> alerts 0
// funcTwo()    -> sets global a to 5
// funcThree()  -> alerts 5
//
// #2.2 If global a is const instead of let?
// const a = 0; then funcTwo() tries a = 5 -> TypeError (cannot reassign const).

// #3
function funcFour() {
  window.a = "hello"; // creates/overwrites a global property on window (in browser)
}
function funcFive() {
  alert(`inside the funcFive function ${a}`);
}
// Prediction:
// After funcFour(); funcFive(); -> alerts "hello"
// Why: window.a becomes globally accessible as a in the browser.

// #4
let a2 = 1;
function funcSix() {
  let a2 = "test";
  alert(`inside the funcSix function ${a2}`);
}
// Prediction:
// funcSix() alerts "test"
// Why: inner a2 shadows outer a2 (block/function scope).
//
// #4.2 If inner variable is const instead of let?
// const a2 = "test"; works the same (no reassignment), still alerts "test".

// #5
let a3 = 2;
if (true) {
  let a3 = 5;
  alert(`in the if block ${a3}`);
}
alert(`outside of the if block ${a3}`);
// Prediction:
// First alert: "in the if block 5"
// Second alert: "outside of the if block 2"
// Why: let is block-scoped; inner a3 is a different variable.
//
// #5.2 If declared with const instead of let?
// If you use const a3 = 5 inside the block: same output (no reassignment needed).
// If you use const a3 = 2 outside: also fine, as long as you don't reassign it.



/********************************
 * 🌟 Exercise 2: Ternary operator
 ********************************/

// Transform to arrow function:
const winBattle = () => true;

// Ternary assignment:
let experiencePoints = winBattle() ? 10 : 1;

console.log(experiencePoints); // 10



/*******************************
 * 🌟 Exercise 3: Is it a string?
 *******************************/

const isString = (value) => typeof value === "string";

console.log(isString("hello"));      // true
console.log(isString([1, 2, 4, 0]));  // false



/*************************
 * 🌟 Exercise 4: Find the sum
 *************************/

const sum = (x, y) => x + y;

console.log(sum(3, 4)); // 7



/****************************
 * 🌟 Exercise 5: Kg and grams
 ****************************/

// 1) Function declaration
function kgToGramsDecl(kg) {
  return kg * 1000;
}
console.log(kgToGramsDecl(2)); // 2000

// 2) Function expression
const kgToGramsExpr = function (kg) {
  return kg * 1000;
};
console.log(kgToGramsExpr(2)); // 2000

// Difference (one-line):
// Declaration is hoisted (can be called before it’s defined); expression is not (depends on the variable assignment).

// 3) Arrow function one-liner
const kgToGramsArrow = (kg) => kg * 1000;

console.log(kgToGramsArrow(2)); // 2000



/****************************
 * 🌟 Exercise 6: Fortune teller (IIFE)
 ****************************/

(function (numChildren, partnerName, location, jobTitle) {
  const sentence = `You will be a ${jobTitle} in ${location}, and married to ${partnerName} with ${numChildren} kids.`;

  // Display in DOM:
  const p = document.createElement("p");
  p.textContent = sentence;
  document.body.appendChild(p);
})(3, "Alex", "Tel Aviv", "Data Analyst");



/****************************
 * 🌟 Exercise 7: Welcome (Navbar + IIFE)
 ****************************/

/*
HTML idea (put in your HTML file):
<nav id="navbar"></nav>
*/

(function (username) {
  const navbar = document.getElementById("navbar");
  if (!navbar) return; // prevents errors if HTML isn't present

  const userBox = document.createElement("div");
  userBox.style.display = "flex";
  userBox.style.alignItems = "center";
  userBox.style.gap = "10px";

  const nameEl = document.createElement("span");
  nameEl.textContent = username;

  const img = document.createElement("img");
  img.src = "https://via.placeholder.com/40"; // replace with real profile image URL
  img.alt = `${username} profile picture`;
  img.width = 40;
  img.height = 40;
  img.style.borderRadius = "50%";

  userBox.appendChild(img);
  userBox.appendChild(nameEl);
  navbar.appendChild(userBox);
})("John");



/****************************
 * 🌟 Exercise 8: Juice Bar
 ****************************/

/* Part I */
function makeJuice(size) {
  function addIngredients(ing1, ing2, ing3) {
    const sentence = `The client wants a ${size} drink juice, containing ${ing1}, ${ing2}, ${ing3}.`;
    const p = document.createElement("p");
    p.textContent = sentence;
    document.body.appendChild(p);
  }

  // Invoke inner function once
  addIngredients("apple", "mint", "ginger");
}

// Invoke outer function in global scope
makeJuice("large");


/* Part II */
function makeJuice2(size) {
  const ingredients = [];

  function addIngredients(ing1, ing2, ing3) {
    ingredients.push(ing1, ing2, ing3);
  }

  function displayJuice() {
    const sentence = `The client wants a ${size} drink juice, containing ${ingredients.join(", ")}.`;
    const p = document.createElement("p");
    p.textContent = sentence;
    document.body.appendChild(p);
  }

  // Client wants 6 ingredients: call addIngredients twice
  addIngredients("orange", "carrot", "turmeric");
  addIngredients("lemon", "ginger", "mint");

  // Then display once
  displayJuice();
}

// Invoke in global scope
makeJuice2("medium");

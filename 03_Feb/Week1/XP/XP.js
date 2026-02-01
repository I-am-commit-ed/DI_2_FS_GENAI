// 🌟 Exercise 1 : List of people

const people = ["Greg", "Mary", "Devon", "James"];

// Part I - Arrays

// 1) Remove “Greg”
people.shift(); // removes first element ("Greg")
// OR: people.splice(0, 1);

// 2) Replace “James” to “Jason”
people[people.indexOf("James")] = "Jason";

// 3) Add your name to the end
people.push("Manuel");

// 4) Console.log Mary’s index
console.log(people.indexOf("Mary")); // should be 0 after removing Greg

// 5) Copy using slice (NOT include “Mary” or your name)
// At this point: ["Mary","Devon","Jason","Manuel"]
const peopleCopy = people.slice(1, 3); // ["Devon","Jason"]
console.log(peopleCopy);

// 6) Index of “Foo” + why -1
console.log(people.indexOf("Foo")); // -1 because it's not found in the array

// 7) last = last element
const last = people[people.length - 1];
console.log(last);

// Part II - Loops

// 1) Log each person
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
}

// 2) Exit after logging “Devon”
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
  if (people[i] === "Devon") break;
}


// 🌟 Exercise 2 : Your favorite colors

const colors = ["blue", "red", "black", "green", "purple"];

// Basic
for (let i = 0; i < colors.length; i++) {
  console.log(`My #${i + 1} choice is ${colors[i]}`);
}

// Bonus: correct suffixes
const suffixes = ["st", "nd", "rd", "th", "th"]; // good enough for 1–5
for (let i = 0; i < colors.length; i++) {
  console.log(`My ${i + 1}${suffixes[i]} choice is ${colors[i]}`);
}


// 🌟 Exercise 3 : Repeat the question

let num = prompt("Enter a number:");
console.log(typeof num); // prompt returns a string

num = Number(num);

while (num < 10) {
  num = Number(prompt("Number is smaller than 10. Enter a new number:"));
}


// 🌟 Exercise 4 : Building Management

const building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
    firstFloor: 3,
    secondFloor: 4,
    thirdFloor: 9,
    fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent: {
    sarah: [3, 990],
    dan: [4, 1000],
    david: [1, 500],
  },
};

// 1) number of floors
console.log(building.numberOfFloors);

// 2) apartments on floors 1 and 3
console.log(building.numberOfAptByFloor.firstFloor);
console.log(building.numberOfAptByFloor.thirdFloor);

// 3) second tenant + number of rooms
const secondTenant = building.nameOfTenants[1]; // "Dan"
console.log(secondTenant);
console.log(building.numberOfRoomsAndRent[secondTenant.toLowerCase()][0]); // rooms

// 4) If (Sarah + David rent) > Dan rent, set Dan rent to 1200
const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent = building.numberOfRoomsAndRent.dan[1];

if (sarahRent + davidRent > danRent) {
  building.numberOfRoomsAndRent.dan[1] = 1200;
}
console.log(building.numberOfRoomsAndRent.dan[1]);


// 🌟 Exercise 5 : Family

const family = {
  father: "Carlos",
  mother: "Ana",
  sister: "Lina",
};

// keys
for (const key in family) {
  console.log(key);
}

// values
for (const key in family) {
  console.log(family[key]);
}


// 🌟 Exercise 6 : Rudolf

const details = {
  my: "name",
  is: "Rudolf",
  the: "reindeer",
};

let sentence = "";
for (const key in details) {
  sentence += details[key] + " ";
}
console.log(sentence.trim()); // "name Rudolf reindeer"

// If you want EXACT: "my name is Rudolf the reindeer"
console.log("my name is Rudolf the reindeer");


// 🌟 Exercise 7 : Secret Group

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

const secret = names
  .map((name) => name[0])  // first letters
  .sort()                  // alphabetical
  .join("");               // string

console.log(secret); // "ABJKPS"

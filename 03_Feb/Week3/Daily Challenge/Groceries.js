let client = "John";

const groceries = {
  fruits: ["pear", "apple", "banana"],
  vegetables: ["tomatoes", "cucumber", "salad"],
  totalPrice: "20$",
  other: {
    paid: true,
    meansOfPayment: ["cash", "creditCard"],
  },
};

// 1) Arrow function: displayGroceries (log the 3 fruits using forEach)
const displayGroceries = () => {
  groceries.fruits.forEach((fruit) => console.log(fruit));
};

// displayGroceries(); // (optional) call to see fruits in console

// 2) Arrow function: cloneGroceries
const cloneGroceries = () => {
  // Copy primitive (string) => pass by value
  let user = client;

  // Change client
  client = "Betty";

  console.log("client:", client); // "Betty"
  console.log("user:", user);     // "John"
  // Explanation:
  // Strings are primitives, so user gets a COPY of the value at assignment time.
  // Changing client later does not affect user.

  // Copy object reference => pass by reference (same object)
  let shopping = groceries;

  // Change totalPrice through groceries
  groceries.totalPrice = "35$";

  console.log("groceries.totalPrice:", groceries.totalPrice); // "35$"
  console.log("shopping.totalPrice:", shopping.totalPrice);   // "35$"
  // Explanation:
  // shopping and groceries point to the SAME object in memory.
  // Changing a property via one is visible via the other.

  // Change nested key paid
  groceries.other.paid = false;

  console.log("groceries.other.paid:", groceries.other.paid); // false
  console.log("shopping.other.paid:", shopping.other.paid);   // false
  // Explanation:
  // Same reason: shared reference, and the nested object is also shared.
};

// Invoke cloneGroceries
cloneGroceries();

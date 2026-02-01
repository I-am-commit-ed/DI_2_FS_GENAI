// Exercise: not ... bad -> good

let sentence = "This dinner is not that bad ! You cook well";

let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
  // replace from "not" up to the end of "bad"
  let result =
    sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);

  console.log(result);
} else {
  console.log(sentence);
}


const examples = [
  "This dinner is not that bad ! You cook well",
  "This movie is not so bad !",
  "This dinner is bad !",
];

for (const sentence of examples) {
  const wordNot = sentence.indexOf("not");
  const wordBad = sentence.indexOf("bad");

  if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
    const result =
      sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
    console.log(result);
  } else {
    console.log(sentence);
  }
}

const form = document.getElementById("libform");

const nounInput = document.getElementById("noun");
const adjInput = document.getElementById("adjective");
const personInput = document.getElementById("person");
const verbInput = document.getElementById("verb");
const placeInput = document.getElementById("place");

const storySpan = document.getElementById("story");
const shuffleBtn = document.getElementById("shuffle-button");

// We'll store the last valid values so Shuffle keeps them
let lastValues = null;

// At least 3 stories (we'll do 5)
function buildStories({ noun, adjective, person, verb, place }) {
  return [
    `${person} brought a ${adjective} ${noun} to ${place} and decided to ${verb} like nobody was watching.`,
    `In ${place}, a ${adjective} ${noun} convinced ${person} to ${verb} before lunch. Bad idea. Great story.`,
    `${person} tried to ${verb} the ${adjective} ${noun} near ${place}, and the whole town applauded.`,
    `Legend says that in ${place}, if you whisper "${noun}" three times, ${person} will ${verb} in a very ${adjective} way.`,
    `${person} lost a ${adjective} ${noun} in ${place}, then had to ${verb} all day to find it again.`,
  ];
}

function getValues() {
  return {
    noun: nounInput.value.trim(),
    adjective: adjInput.value.trim(),
    person: personInput.value.trim(),
    verb: verbInput.value.trim(),
    place: placeInput.value.trim(),
  };
}

function hasEmpty(values) {
  // returns true if any value is empty
  return Object.values(values).some((v) => v === "");
}

function displayRandomStory(values) {
  const stories = buildStories(values);
  const randomIndex = Math.floor(Math.random() * stories.length);
  storySpan.textContent = stories[randomIndex];
}

// FORM SUBMIT: generate story
form.addEventListener("submit", (event) => {
  event.preventDefault(); // prevent page reload

  const values = getValues();

  if (hasEmpty(values)) {
    storySpan.textContent = "Please fill in all fields 🙂";
    return;
  }

  lastValues = values; // save for shuffle
  displayRandomStory(values);
});

// BONUS: shuffle story but keep same values
shuffleBtn.addEventListener("click", () => {
  if (!lastValues) {
    storySpan.textContent = "First click “Lib it!” to generate a story 🙂";
    return;
  }

  displayRandomStory(lastValues);
});

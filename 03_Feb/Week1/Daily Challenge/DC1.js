// PATTERN (6 lines)
// *
// * *
// * * *
// * * * *
// * * * * *
// * * * * * *

// ✅ Version 1: ONE loop (build a growing string)
let line = "";
for (let i = 0; i < 6; i++) {
  line += "* ";
  console.log(line);
}

// ✅ Version 2: TWO nested loops (outer = rows, inner = stars per row)
for (let row = 1; row <= 6; row++) {
  let stars = "";
  for (let col = 1; col <= row; col++) {
    stars += "* ";
  }
  console.log(stars);
}

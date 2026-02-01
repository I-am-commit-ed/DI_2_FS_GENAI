<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>DOM Exercises 1–4</title>

    <style>
      body {
        font-family: Arial, Helvetica, sans-serif;
        padding: 24px;
        line-height: 1.5;
      }

      article {
        border: 1px solid #ddd;
        padding: 16px;
        border-radius: 8px;
        margin-bottom: 28px;
      }

      button {
        padding: 8px 12px;
        cursor: pointer;
        margin-top: 10px;
      }

      /* BONUS (Exercise 1): fade animation */
      @keyframes fadeOut {
        from { opacity: 1; }
        to { opacity: 0; }
      }

      .fade-out {
        animation: fadeOut 0.7s ease forwards;
      }

      /* Exercise 4 base style */
      #sphereSection {
        border: 1px solid #ddd;
        padding: 16px;
        border-radius: 8px;
        margin-top: 28px;
      }

      #sphereSection label,
      #sphereSection input {
        display: block;
      }

      #sphereSection input {
        margin-bottom: 10px;
        padding: 6px;
        width: 220px;
      }
    </style>
  </head>

  <body>
    <!-- ===================== -->
    <!-- Exercise 1: Article -->
    <!-- ===================== -->
    <section>
      <h2>Exercise 1: Change the article</h2>

      <article id="chocoArticle">
        <h1> Some Facts </h1>
        <h2 id="chocoH2"> The Chocolate </h2>
        <h3 id="chocoH3"> History of the chocolate </h3>

        <p>Chocolate is made from tropical Theobroma cacao tree seeds.
          Its earliest use dates back to the Olmec civilization in Mesoamerica.</p>

        <p id="secondParagraph">After the European discovery of the Americas, chocolate became
          very popular in the wider world, and its demand exploded.</p>

        <p>Chocolate has since become a popular food product that millions enjoy every day,
          thanks to its unique, rich, and sweet taste.</p>

        <p>But what effect does eating chocolate have on our health?</p>
      </article>

      <button id="boldBtn">Make all article paragraphs bold</button>
    </section>

    <!-- ===================== -->
    <!-- Exercise 2: Form -->
    <!-- ===================== -->
    <section>
      <h2>Exercise 2: Work with forms</h2>

      <form id="nameForm">
        <label for="fname">First name:</label><br />
        <input type="text" id="fname" name="firstname" /><br />

        <label for="lname">Last name:</label><br />
        <input type="text" id="lname" name="lastname" /><br /><br />

        <input type="submit" value="Submit" id="submitForm" />
      </form>

      <ul class="usersAnswer"></ul>
    </section>

    <!-- ===================== -->
    <!-- Exercise 3: Bold hover -->
    <!-- ===================== -->
    <section>
      <h2>Exercise 3: Transform the sentence</h2>

      <p id="boldParagraph">
        <strong>Hello</strong> I hope you are enjoying <strong>this</strong> class. At the
        <strong>end</strong> you <strong>will</strong> be great Developers!
        <strong>Enjoy</strong> the <strong>JavaScript </strong> lessons
      </p>
    </section>

    <!-- ===================== -->
    <!-- Exercise 4: Sphere -->
    <!-- ===================== -->
    <section id="sphereSection">
      <h2>Exercise 4: Volume of a sphere</h2>
      <p>Input radius value and get the volume of a sphere.</p>

      <form id="MyForm">
        <label for="radius">Radius</label>
        <input type="text" name="radius" id="radius" required />

        <label for="volume">Volume</label>
        <input type="text" name="volume" id="volume" />

        <input type="submit" value="Calculate" id="submitSphere" />
      </form>
    </section>

    <script>
      // =========================
      // Exercise 1
      // =========================

      // 1) Using a DOM property, retrieve the h1 and console.log it.
      const article = document.getElementById("chocoArticle");
      const h1 = article.firstElementChild; // DOM property (firstElementChild)
      console.log("Exercise 1 - h1:", h1);

      // 2) Using DOM methods, remove the last paragraph in the <article> tag.
      const lastP = article.querySelector("p:last-of-type");
      if (lastP) lastP.remove();

      // 3) Click h2 => background red
      const h2 = document.getElementById("chocoH2");
      h2.addEventListener("click", () => {
        h2.style.backgroundColor = "red";
      });

      // 4) Click h3 => hide (display:none)
      const h3 = document.getElementById("chocoH3");
      h3.addEventListener("click", () => {
        h3.style.display = "none";
      });

      // 5) Button: make all article paragraphs bold
      const boldBtn = document.getElementById("boldBtn");
      boldBtn.addEventListener("click", () => {
        const paragraphs = article.querySelectorAll("p");
        paragraphs.forEach((p) => {
          p.style.fontWeight = "bold";
        });
      });

      // BONUS 1) Hover on h1 => random font size 0..100px
      h1.addEventListener("mouseover", () => {
        const randomSize = Math.floor(Math.random() * 101); // 0..100
        h1.style.fontSize = randomSize + "px";
      });

      // BONUS 2) Hover on 2nd paragraph => fade out (CSS animation)
      const secondParagraph = document.getElementById("secondParagraph");
      secondParagraph.addEventListener("mouseover", () => {
        secondParagraph.classList.add("fade-out");
      });

      // (Optional) if you want it to come back when mouse leaves:
      // secondParagraph.addEventListener("mouseout", () => {
      //   secondParagraph.classList.remove("fade-out");
      //   secondParagraph.style.opacity = 1;
      // });

      // =========================
      // Exercise 2
      // =========================

      // Retrieve the form and console.log it.
      const form = document.getElementById("nameForm");
      console.log("Exercise 2 - form:", form);

      // Retrieve the inputs by their id and console.log them.
      const fnameById = document.getElementById("fname");
      const lnameById = document.getElementById("lname");
      console.log("Exercise 2 - inputs by id:", fnameById, lnameById);

      // Retrieve the inputs by their name attribute and console.log them.
      const fnameByName = document.querySelector('input[name="firstname"]');
      const lnameByName = document.querySelector('input[name="lastname"]');
      console.log("Exercise 2 - inputs by name:", fnameByName, lnameByName);

      // Submit event
      const usersAnswerUl = document.querySelector(".usersAnswer");

      form.addEventListener("submit", (event) => {
        // preventDefault: stops page refresh / default submit navigation
        event.preventDefault();

        const first = fnameById.value.trim();
        const last = lnameById.value.trim();

        // make sure not empty
        if (!first || !last) return;

        // Clear previous answers (optional but nice)
        usersAnswerUl.innerHTML = "";

        // create li per value
        const li1 = document.createElement("li");
        li1.textContent = first;

        const li2 = document.createElement("li");
        li2.textContent = last;

        // append to ul
        usersAnswerUl.appendChild(li1);
        usersAnswerUl.appendChild(li2);

        // (Optional) reset form
        form.reset();
      });

      // =========================
      // Exercise 3
      // =========================

      // Global variable
      let allBoldItems;

      function getBoldItems() {
        const p = document.getElementById("boldParagraph");
        allBoldItems = p.querySelectorAll("strong");
      }

      function highlight() {
        allBoldItems.forEach((el) => {
          el.style.color = "blue";
        });
      }

      function returnItemsToDefault() {
        allBoldItems.forEach((el) => {
          el.style.color = "black";
        });
      }

      getBoldItems();

      const boldParagraph = document.getElementById("boldParagraph");
      boldParagraph.addEventListener("mouseover", highlight);
      boldParagraph.addEventListener("mouseout", returnItemsToDefault);

      // =========================
      // Exercise 4
      // =========================

      const sphereForm = document.getElementById("MyForm");
      const radiusInput = document.getElementById("radius");
      const volumeInput = document.getElementById("volume");

      sphereForm.addEventListener("submit", (event) => {
        event.preventDefault();

        const r = parseFloat(radiusInput.value);

        if (Number.isNaN(r) || r <= 0) {
          volumeInput.value = "";
          return;
        }

        // Volume = (4/3) * π * r^3
        const volume = (4 / 3) * Math.PI * Math.pow(r, 3);

        // Put a rounded value (you can change decimals)
        volumeInput.value = volume.toFixed(2);
      });
    </script>
  </body>
</html>

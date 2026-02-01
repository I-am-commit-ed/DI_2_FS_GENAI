// BONUS I: Use an array of task objects
// Each task: { task_id, text, done }
const tasks = [];

const form = document.getElementById("taskForm");
const input = document.getElementById("taskInput");
const listTasksDiv = document.querySelector(".listTasks");

// Create a unique incremental id (starting from 0)
function nextTaskId() {
  return tasks.length === 0 ? 0 : Math.max(...tasks.map((t) => t.task_id)) + 1;
}

function addTask(text) {
  const trimmed = text.trim();

  // check that the input is not empty
  if (trimmed === "") return;

  const task = {
    task_id: nextTaskId(),
    text: trimmed,
    done: false,
  };

  // add it to the array
  tasks.push(task);

  // add it to the DOM
  renderTask(task);
}

function renderTask(task) {
  const taskRow = document.createElement("div");
  taskRow.className = "task";
  taskRow.dataset.taskId = String(task.task_id); // data-task-id

  // X button (Font Awesome)
  const deleteBtn = document.createElement("button");
  deleteBtn.className = "delete-btn";
  deleteBtn.type = "button";
  deleteBtn.setAttribute("aria-label", "Delete task");
  deleteBtn.innerHTML = `<i class="fa-solid fa-xmark"></i>`;

  // checkbox
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.className = "task-check";
  checkbox.checked = task.done;

  // label
  const label = document.createElement("label");
  label.textContent = task.text;

  // Hook label click to checkbox for nicer UX (optional)
  const checkboxId = `task-checkbox-${task.task_id}`;
  checkbox.id = checkboxId;
  label.setAttribute("for", checkboxId);

  // apply done styling if needed
  if (task.done) taskRow.classList.add("done");

  taskRow.appendChild(deleteBtn);
  taskRow.appendChild(checkbox);
  taskRow.appendChild(label);

  listTasksDiv.appendChild(taskRow);
}

// BONUS I: toggle done property + crossed-out red DOM
function doneTask(taskId, isDone) {
  const task = tasks.find((t) => t.task_id === taskId);
  if (!task) return;

  task.done = isDone;

  const row = listTasksDiv.querySelector(`[data-task-id="${taskId}"]`);
  if (!row) return;

  row.classList.toggle("done", task.done);
}

// BONUS II: delete from array + remove from DOM
function deleteTask(taskId) {
  const index = tasks.findIndex((t) => t.task_id === taskId);
  if (index === -1) return;

  tasks.splice(index, 1);

  const row = listTasksDiv.querySelector(`[data-task-id="${taskId}"]`);
  if (row) row.remove();
}

// Form submit => addTask
form.addEventListener("submit", (e) => {
  e.preventDefault();
  addTask(input.value);
  input.value = "";
  input.focus();
});

// Event delegation for checkbox + delete button
listTasksDiv.addEventListener("click", (e) => {
  const row = e.target.closest(".task");
  if (!row) return;

  const taskId = Number(row.dataset.taskId);

  // delete button click (or icon inside it)
  if (e.target.closest(".delete-btn")) {
    deleteTask(taskId);
  }
});

listTasksDiv.addEventListener("change", (e) => {
  if (!e.target.classList.contains("task-check")) return;

  const row = e.target.closest(".task");
  if (!row) return;

  const taskId = Number(row.dataset.taskId);
  doneTask(taskId, e.target.checked);
});

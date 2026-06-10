const todoList = [
  {
    name: "make dinner",
    dueDate: "2022-12-22",
  },
  {
    name: "wash dishes",
    dueDate: "2022-12-22",
  },
];

renderTodoList();

function renderTodoList() {
  let todoListHTML = "";

  todoList.forEach((todoObject, index) => {
    const { name, dueDate } = todoObject;

    const html = `
      <div>
        ${name}
      </div>

      <div>
        ${dueDate}
      </div>

      <button class="delete-todo-button js-delete-todo-button">
        Delete
      </button>
    `; // 这里每次删完一个都会重新运行一遍显示待办的函数，重新给待办排序，所以保证了删除按钮的可行性和正确性。

    todoListHTML += html;
  });

  // console.log(todoListHTML);

  document.querySelector(".js-todo-list").innerHTML = todoListHTML;

  // Problem 1
  // The code of the delete button are just strings.
  // Problem 2
  // We have nultiple delete buttons.
  // document.querySelector just gives us the first js-delete button.
  // forEach()
  // 1. The value
  // 2. The index
  document
    .querySelectorAll(".js-delete-todo-button")
    .forEach((deleteButton, index) => {
      deleteButton.addEventListener("click", () => {
        // console.log(index);
        todoList.splice(index, 1);
        renderTodoList();
      });
    });
}

document.querySelector(".js-add-todo-button").addEventListener("click", () => {
  addTodo();
});

function addTodo() {
  const inputElement = document.querySelector(".js-name-input");
  const name = inputElement.value;

  const dateInputElement = document.querySelector(".js-due-date-input");
  const dueDate = dateInputElement.value;

  todoList.push({
    // name: name,
    // dueDate: dueDate,
    name,
    dueDate,
  });

  // console.log(todoList);

  inputElement.value = "";

  renderTodoList();
}

// 2026.06.03 14:17

// 2026.06.05 11:41

// 2026.06.05 22:40

// 2026.06.10 23:24

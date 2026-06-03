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

  todoList.forEach(function (todoObject, index) {
    const { name, dueDate } = todoObject;

    const html = `
      <div>
        ${name}
      </div>

      <div>
        ${dueDate}
      </div>

      <button class="delete-todo-button" onclick="
        todoList.splice(${index}, 1);
        renderTodoList();
      ">
        Delete
      </button>
    `; // 这里每次删完一个都会重新运行一遍显示待办的函数，重新给待办排序，所以保证了删除按钮的可行性和正确性。

    todoListHTML += html;
  });

  // console.log(todoListHTML);

  document.querySelector(".js-todo-list").innerHTML = todoListHTML;
}

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

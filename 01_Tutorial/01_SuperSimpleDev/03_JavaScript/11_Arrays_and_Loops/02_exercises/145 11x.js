// 这里要修改。
// When loading the page, load from localStorage.
const todoList = JSON.parse(localStorage.getItem("todoList")) || [
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

  for (let i = 0; i < todoList.length; i++) {
    const todoObject = todoList[i];

    // const name = todoObject.name;
    // const dueDate = todoObject.dueDate;
    const { name, dueDate } = todoObject;

    const html = `
      <div>
        ${name}
      </div>

      <div>
        ${dueDate}
      </div>

      <button class="delete-todo-button" onclick="
        todoList.splice(${i}, 1);
        renderTodoList();

        // Whenever we update the todo list, save in localStorage.
        saveToStorage();
        // 这里是删除的时候要刷新本地存储。 
        console.log(localStorage);
      ">
        Delete
      </button>
    `; // 这里每次删完一个都会重新运行一遍显示待办的函数，重新给待办排序，所以保证了删除按钮的可行性和正确性。

    todoListHTML += html;
  }

  // console.log(todoListHTML);

  document.querySelector(".js-todo-list").innerHTML = todoListHTML;
}

// addTodo()只是把新待办加进列表里，renderTodoList才是创建所有新的HTML。
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

  // Whenever we update the todo list, save in localStorage.
  saveToStorage();
  // 我还以为saveToStorage()是一个什么localStorage的内置方法呢，还纳闷了一会儿，原来是自己创建的一个函数啊。

  // 不清楚localStorage和JSON是如何运作可以用console.log()来输出查看。
  console.log(localStorage);
  // localStorage是一个对象，里面存了todoList，
  // 可以单独调用localStorage.todoList，
  // todoList对应一个字符串，那个字符串是将一个 列表 传化而来的字符串，
  // 原列表里保存的是若干个对象，
  // 对象保存了待办的name和dueDate，
  // name和dueDate这两个属性名也转化成了字符串，
  // name和dueDate对应的值本来就是字符串。
}

function saveToStorage() {
  localStorage.setItem("todoList", JSON.stringify(todoList));
}

// 那两个显示localStorage的console.log()语句是我自己加的，Simon的代码中没有那两句。
// 那两句console.log()加哪里也有要思考的地方，现在那两句console.log()所处的位置其实是不一样的。

// 2026.05.30 12:58

// localStorage大概长这样：
// Storage {calculation: '10062 + 036', todoList: '[{"name":"","dueDate":""},{"name":"","dueDate":""}…"name":"","dueDate":""},{"name":"","dueDate":""}]', cartQuantity: '2', length: 3}
// 最后的length代表Storage一共有三个键，分别是calculation、todoList和cartQuantity。
// 卧槽，calculation和cartQuantity好像分别是计算器项目和购物车项目的本地存储，原来一个Storage把它们一起存了。

// 2026.05.30 13:04

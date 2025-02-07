document.addEventListener("DOMContentLoaded", displayTasks);

function addTask() {
    let taskTitle = document.getElementById("taskTitle").value.trim();
    let taskDescription = document.getElementById("taskDescription").value.trim();
    let taskDateTime = document.getElementById("taskDateTime").value;

    if (taskTitle === "" || taskDateTime === "") {
        alert("Please enter a valid task and date/time.");
        return;
    }

    let task = {
        title: taskTitle,
        description: taskDescription,
        dateTime: taskDateTime
    };

    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.push(task);

    localStorage.setItem("tasks", JSON.stringify(tasks));
    saveTaskToFile(task);
    displayTasks();

    document.getElementById("taskTitle").value = "";
    document.getElementById("taskDescription").value = "";
    document.getElementById("taskDateTime").value = "";
}

function removeTask(index) {
    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.splice(index, 1);
    localStorage.setItem("tasks", JSON.stringify(tasks));
    displayTasks();
}

function displayTasks() {
    let taskList = document.getElementById("taskList");
    taskList.innerHTML = "";

    let tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.forEach((task, index) => {
        let li = document.createElement("li");
        li.innerHTML = `
            <strong>${task.title}</strong>
            <p>${task.description}</p>
            <span class="timestamp">${task.dateTime}</span>
            <button class="remove-btn" onclick="removeTask(${index})">Remove</button>
        `;
        taskList.appendChild(li);
    });
}

function saveTaskToFile(task) {
    fetch("http://127.0.0.1:5000/add_task", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(task)
    });
}

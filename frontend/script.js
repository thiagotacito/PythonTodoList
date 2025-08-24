const apiUrl = "http://127.0.0.1:8000/tasks";

// 🔄 Carregar tarefas
async function loadTasks() {
    const response = await fetch(apiUrl);
    const tasks = await response.json();

    const taskList = document.getElementById("task-list");
    taskList.innerHTML = "";

    tasks.forEach(task => {
        const li = document.createElement("li");
        li.innerHTML = `
            <strong>${task.title}</strong> - ${task.description} 
            [${task.done ? "✅ Concluída" : "❌ Pendente"}]
            <button onclick="toggleTask(${task.id}, ${task.done})">Concluir</button>
            <button onclick="deleteTask(${task.id})">Excluir</button>
        `;
        taskList.appendChild(li);
    });
}

// ➕ Adicionar nova tarefa
async function addTask() {
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;

    if (!title) {
        alert("O título é obrigatório!");
        return;
    }

    const response = await fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, description })
    });

    if (response.ok) {
        document.getElementById("title").value = "";
        document.getElementById("description").value = "";
        loadTasks();
    } else {
        const error = await response.json();
        alert("Erro ao adicionar: " + JSON.stringify(error));
    }
}

// 🔄 Alternar status (done)
async function toggleTask(id, done) {
    const response = await fetch(`${apiUrl}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ done: !done })
    });

    if (response.ok) {
        loadTasks();
    } else {
        const error = await response.json();
        alert("Erro ao atualizar: " + JSON.stringify(error));
    }
}

// ❌ Excluir tarefa
async function deleteTask(id) {
    const response = await fetch(`${apiUrl}/${id}`, {
        method: "DELETE"
    });

    if (response.ok) {
        loadTasks();
    } else {
        const error = await response.json();
        alert("Erro ao excluir: " + JSON.stringify(error));
    }
}

// 🚀 Carregar assim que abrir a página
loadTasks();

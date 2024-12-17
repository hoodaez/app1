async function addTask() {
    const input = document.getElementById('taskInput');
    const task = input.value;

    if (task.trim() === '') return;

    // إرسال المهمة إلى الخادم (Back-End)
    await fetch('http://localhost:3000/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: task })
    });

    input.value = '';
    fetchTasks();
}

async function fetchTasks() {
    const response = await fetch('http://localhost:3000/tasks');
    const tasks = await response.json();

    const taskList = document.getElementById('taskList');
    taskList.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.textContent = task.name;
        taskList.appendChild(li);
    });
}

// تحميل المهام عند فتح الصفحة
fetchTasks();

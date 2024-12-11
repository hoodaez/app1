
// script.js
document.getElementById('addTaskButton').addEventListener('click', function () {
    const taskInput = document.getElementById('taskInput');
    const taskList = document.getElementById('taskList');

    if (taskInput.value.trim() !== '') {
        const listItem = document.createElement('li');
        listItem.textContent = taskInput.value;

        // إضافة زر حذف لكل مهمة
        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.style.marginLeft = '10px';
        deleteButton.style.backgroundColor = 'red';
        deleteButton.style.color = 'white';
        deleteButton.addEventListener('click', function () {
            taskList.removeChild(listItem);
        });

        listItem.appendChild(deleteButton);
        taskList.appendChild(listItem);
        taskInput.value = '';
    }
});


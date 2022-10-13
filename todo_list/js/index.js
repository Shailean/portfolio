const taskManager = new TaskManager();
console.log(taskManager.tasks);

// select the inputs on the html form
const newTaskNameInput = document.querySelector('#newTaskNameInput');
const newTaskDescriptionInput = document.querySelector('#newTaskDescriptionInput');
const newTaskDueDateInput = document.querySelector('#newTaskDueDateInput');
const newTaskAssignedToInput = document.querySelector('#newTaskAssignedToInput');


//Connecting HTML Task Form
let newTaskForm = document.querySelector("#newTaskForm");
newTaskForm.addEventListener('submit', (event) => {
// preventDefault action
  event.preventDefault();

// Get the values of the inputs
const name = newTaskNameInput.value;
const description = newTaskDescriptionInput.value;
const dueDate = newTaskDueDateInput.value;
const assignedTo = newTaskAssignedToInput.value;

// Validate form input (FUNCTION NOT CURRENTLY WORKING)
  function validFormFieldInput() {
    // Validate task name input
    if (name == "") {
      alert("Please enter a task name"); 
      return false;
    } else {
        console.log("Name:  " + name);
    }
    // Validate task description input
    if (description == "") {
      alert("Please enter a task description"); 
      return false;
    } else {
        console.log("Description:  " + description);
    }
    // Validate task due date input
    if (dueDate == "") {
      alert("Please enter a task due date"); 
      return false;
    } else {
        console.log("Due Date:  " + dueDate);
    }
    // Validate task assigned to input
    if (assignedTo == "") {
      alert("Please assign the task"); 
      return false;
    } else {
        console.log("Assigned to:  " + assignedTo);
    }
  };//end bracket for form input validation

// Add the task to the task manager
taskManager.addTask(name, description, dueDate, assignedTo);

// Clear the form
newTaskNameInput.value = '';
});
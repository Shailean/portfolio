// TASK 6 createTaskHTML = (id, name, dueDate)
/* <div class="card" id="tasks-not-started">
    <div class="card-body">
        <h5 class="card-title">Review pull requests</h5>
            <p class="card-text">Group meeting on Jul 17 at 4:00pm EST to approve and merge code</p>
            <p>ASSIGNED TO: All <br> DUE DATE: Jul 17, 2022</p>
            <span class="badge badge-danger">Not Started</span>
</div> */


//TaskManager class created
class TaskManager { 
    constructor(currentId=0) {
        this.tasks = [];
        this.currentId = currentId;
    }

//addTask method created
    addTask(name, description, dueDate, assignedTo){
        const task = {
            id: this.currentId++, //increments currentId
            name,
            description,
            dueDate,
            assignedTo,
            status: 'Not Started'
            };
        this.tasks.push(task); //pushing task
    } 
    render(){
        
        //call the createTaskHtml function
    }
}

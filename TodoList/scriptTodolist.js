function addTodo()
{
    const input=document.getElementById("todo-input");
    const taskText=input.value.trim();
    if (taskText==="")
    {
        alert("Enter the valid text");
        return;
    }
    const li=document.createElement("li");
    const span=document.createElement("span");
    span.textContent=taskText;
    li.appendChild(span);
    const editbtn=document.createElement("button");
    editbtn.textContent="Edit";
    editbtn.onclick=function()
    {
        const newTask=prompt("Edit your task:",span.textContent);
        if (newTask!==null && newTask.trim()!=="")
        {
            span.textContent=newTask;
        }
    }
    li.appendChild(editbtn);
   /* const taskSpan=document.createElement("span");
    taskSpan.textContent=taskText;*/
    const delbtn=document.createElement("button");
    delbtn.textContent="X"
    delbtn.onclick=function(){
        li.remove();
    }
    li.appendChild(delbtn);
    
    const list=document.getElementById("todo-list");
    list.appendChild(li);
    input.value="";
}
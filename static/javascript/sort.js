document.addEventListener('DOMContentLoaded', function() {
    const sortBySelect = document.getElementById('sort-by');
    sortBySelect.addEventListener('change', sortTasks);
  
    function sortTasks() {
      const sortByValue = sortBySelect.value;
      const taskList = document.getElementById('task-list');
      const taskItems = Array.from(taskList.getElementsByClassName('task-item'));
  
      taskItems.sort((a, b) => {
        if (sortByValue === 'priority_asc') {
          return sortPriority_asc(a, b);
        } else if (sortByValue === 'priority_desc') {
            return sortPriority_desc(a, b);
          }  else if (sortByValue === 'due-date') {
          return sortDueDate(a, b);
        }
    
        return 0;
      });
  
      taskList.innerHTML = '';
      taskItems.forEach(item => {
        taskList.appendChild(item);
      });
    }
  
    function sortPriority_desc(a, b) {
        const aPriority = getPriorityValue(a);
        const bPriority = getPriorityValue(b);
      
        if (aPriority === bPriority) {
          return 0;
        } else if (aPriority === 'High') {
          return -1;
        } else if (bPriority === 'High') {
          return 1;
        } else if (aPriority === 'Medium') {
          return -1;
        } else if (bPriority === 'Medium') {
          return 1;
        } else if (aPriority === 'Low') {
          return -1;
        } else {
          return 1;
        }
      }
      

      function sortPriority_asc(a, b) {
        const aPriority = getPriorityValue(a);
        const bPriority = getPriorityValue(b);
      
        if (aPriority === bPriority) {
          return 0;
        } else if (aPriority === 'High') {
          return 1;
        } else if (bPriority === 'High') {
          return -1;
        } else if (aPriority === 'Medium') {
          return 1;
        } else if (bPriority === 'Medium') {
          return -1;
        } else if (aPriority === 'Low') {
          return 1;
        } else {
          return -1;
        }
      }
      
  
    function sortDueDate(a, b) {
      const aDueDate = getDueDate(a);
      const bDueDate = getDueDate(b);
  
      return aDueDate - bDueDate;
    }
  
    function getPriorityValue(taskItem) {
      const priorityElement = taskItem.querySelector('.priority span');
      const priority = priorityElement.textContent.trim();
  
      if (priority === 'High') {
        return 'High';
      } else if (priority === 'Medium') {
        return 'Medium';
      } else if (priority === 'Low') {
        return 'Low';
      }
  
      return '';
    }
  
    function getDueDate(taskItem) {
      const dueDateElement = taskItem.querySelector('.due-date span');
      return new Date(dueDateElement.textContent.trim());
    }
  });
  
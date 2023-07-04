document.addEventListener('DOMContentLoaded', function() {
    // Get the filter option elements
    const filterStatus = document.getElementById('filter-status');
    const filterPriority = document.getElementById('filter-priority');
    const filterCategory = document.getElementById('filter-category');
  
    // Get the task list element
    const taskList = document.getElementById('task-list');
  
    // Add event listeners to the filter options
    filterStatus.addEventListener('change', filterTasks);
    filterPriority.addEventListener('change', filterTasks);
    filterCategory.addEventListener('change', filterTasks);
  
    // Function to filter tasks based on selected filter options
    function filterTasks() {
      const selectedStatus = filterStatus.value;
      const selectedPriority = filterPriority.value;
      const selectedCategory = filterCategory.value;
  
      // Get all task items
      const taskItems = taskList.getElementsByClassName('task-item');
  
      // Loop through task items and show/hide based on filter options
      for (let i = 0; i < taskItems.length; i++) {
        const taskItem = taskItems[i];
  
        // Get the data attributes of the task item

        const statusElement = document.querySelector('.task-item .status .status-in');
        const status = statusElement.textContent;

        const priorityElement = document.querySelector('.task-item .priority span');
        const priority = priorityElement.textContent;


        const categoryElement = document.querySelector('.task-item .category span');
        const category = categoryElement.textContent;
          
        // Check if task item matches the selected filter options
        const statusMatch = selectedStatus === 'all' || selectedStatus === status;
        const priorityMatch = selectedPriority === 'all' || selectedPriority === priority;
        const categoryMatch = selectedCategory === 'all' || selectedCategory === category;
  
        // Show/hide task item based on filter options
        if (statusMatch && priorityMatch && categoryMatch) {
          taskItem.style.display = 'block';
        } else {
          taskItem.style.display = 'none';
        }
      }
    }
  
    // Initial task filtering
    filterTasks();
  });
  
let schools = [];

function createSchool(name, location, logo, dateString) {
    console.log('Creating new school:', name, location, logo, dateString);
  
    // Parse the date string into a Date object
    const dateObj = new Date(dateString);
  
    // Create the school object with the parsed date
    const newSchool = { id: schools.length + 1, name, location, logo, date: dateObj };
    schools.push(newSchool);
    displaySchools();
  }
  //event listener
  document.getElementById('create-school-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const schoolName = document.getElementById('school-name').value;
    const schoolLocation = document.getElementById('Location').value;
    const schoolLogo = document.getElementById('logo').value;
    const schoolDateString = document.getElementById('Date').value;
  
    console.log('Form submitted:', schoolName, schoolLocation, schoolLogo, schoolDateString);
  
    if (schoolName && schoolLocation && schoolLogo && schoolDateString) {
      createSchool(schoolName, schoolLocation, schoolLogo, schoolDateString);
      document.getElementById('school-name').value = '';
      document.getElementById('Location').value = '';
      document.getElementById('logo').value = '';
      document.getElementById('Date').value = '';
    } else {
      console.error('One or more form fields are empty.');
    }
  });
function updateSchool(id, newName) {
  const school = schools.find(s => s.id === id);
  if (school) {
    school.name = newName;
    displaySchools();
  }
}

function deleteSchool(id) {
  const index = schools.findIndex(s => s.id === id);
  if (index !== -1) {
    schools.splice(index, 1);
    displaySchools();
  }
}

function displaySchools() {
    const schoolsTable = document.getElementById('schools-table');
    schoolsTable.innerHTML = '';
  
    schools.forEach(school => {
      const row = document.createElement('tr');
      // Use the date object in the school object
    const dateString = school.date.toISOString().slice(0, 10);
  
      const idCell = document.createElement('td');
      idCell.textContent = school.id;
      idCell.classList.add('px-4', 'py-2');
      row.appendChild(idCell);
  
      const nameCell = document.createElement('td');
      nameCell.textContent = school.name;
      nameCell.classList.add('px-4', 'py-2');
      row.appendChild(nameCell);
  
      const locationCell = document.createElement('td');
      locationCell.textContent = school.location;
      locationCell.classList.add('px-4', 'py-2');
      row.appendChild(locationCell);
  
      const logoCell = document.createElement('td');
      logoCell.textContent = school.logo;
      logoCell.classList.add('px-4', 'py-2');
      row.appendChild(logoCell);
  
      const dateCell = document.createElement('td');
      dateCell.textContent = school.date;
      dateCell.classList.add('px-4', 'py-2');
      row.appendChild(dateCell);
  
      const statusCell = document.createElement('td');
      statusCell.textContent = 'Active';
      statusCell.classList.add('px-4', 'py-2', 'active');
      row.appendChild(statusCell);
  
      const actionsCell = document.createElement('td');
      actionsCell.classList.add('px-4', 'py-2');
  
      const editButton = document.createElement('button');
      editButton.textContent = 'Edit';
      editButton.classList.add('bg-yellow-500', 'hover:bg-yellow-600', 'text-white', 'font-bold', 'py-1', 'px-2', 'rounded-md', 'mr-2');
      editButton.addEventListener('click', () => {
        const newName = prompt('Enter new school name');
        updateSchool(school.id, newName);
      });
      actionsCell.appendChild(editButton);
  
      const deleteButton = document.createElement('button');
      deleteButton.textContent = 'Delete';
      deleteButton.classList.add('bg-red-500', 'hover:bg-red-600', 'text-white', 'font-bold', 'py-1', 'px-2', 'rounded-md');
      deleteButton.addEventListener('click', () => deleteSchool(school.id));
      actionsCell.appendChild(deleteButton);
  
      row.appendChild(actionsCell);
      schoolsTable.appendChild(row);
    });
  }
displaySchools();

document.querySelectorAll('.btn-toggle-status').forEach(button => {
    button.addEventListener('click', function() {
      const row = this.closest('tr');
      const statusElement = row.querySelector('.status');
      const isActive = statusElement.classList.contains('active');
  
      if (isActive) {
        statusElement.textContent = 'Inactive';
        statusElement.classList.remove('active');
        statusElement.classList.add('inactive');
        this.textContent = 'Activate';
      } else {
        statusElement.textContent = 'Active';
        statusElement.classList.remove('inactive');
        statusElement.classList.add('active');
        this.textContent = 'Deactivate';
      }
    });
  });
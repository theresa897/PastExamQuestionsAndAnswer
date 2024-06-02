let currentlyEditedQuestion = null;

// Get the necessary DOM elements
const form = document.getElementById('question-form');
const table = document.getElementById('question-table');
const tbody = table.getElementsByTagName('tbody')[0];

// Array to store the questions
let questions = [];

// Function to create a new row in the table
function createRow(question) {
  const row = document.createElement('tr');

  // Create cells for each data point
  const idCell = document.createElement('td');
  idCell.textContent = question.id;

  const subjectCell = document.createElement('td');
  subjectCell.textContent = question.subject;

  const titleCell = document.createElement('td');
  titleCell.textContent = question.title;

  const contentCell = document.createElement('td');
  contentCell.textContent = question.content;

  const fileCell = document.createElement('td');
  fileCell.textContent = question.file ? 'Attached' : 'None';

  const schoolCell = document.createElement('td');
  schoolCell.textContent = question.school;

  const createdCell = document.createElement('td');
  createdCell.textContent = new Date(question.createdAt).toLocaleString();

  const updatedCell = document.createElement('td');
  updatedCell.textContent = new Date(question.updatedAt).toLocaleString();

  const voteCell = document.createElement('td');
  voteCell.textContent = question.votes;

  const actionsCell = document.createElement('td');
  const editButton = document.createElement('button');
  editButton.textContent = 'Edit';
  editButton.addEventListener('click', () => editQuestion(question.id));

  const deleteButton = document.createElement('button');
  deleteButton.textContent = 'Delete';
  deleteButton.addEventListener('click', () => deleteQuestion(question.id));

  actionsCell.appendChild(editButton);
  actionsCell.appendChild(deleteButton);

  // Add the cells to the row
  row.appendChild(idCell);
  row.appendChild(subjectCell);
  row.appendChild(titleCell);
  row.appendChild(contentCell);
  row.appendChild(fileCell);
  row.appendChild(schoolCell);
  row.appendChild(createdCell);
  row.appendChild(updatedCell);
  row.appendChild(voteCell);
  row.appendChild(actionsCell);

  // Add the row to the table
  tbody.appendChild(row);
}

// Function to handle form submission
// Function to handle form submission
form.addEventListener('submit', (event) => {
  event.preventDefault();

  const subject = document.getElementById('subject').value;
  const title = document.getElementById('title').value;
  const content = document.getElementById('question-text').value;
  const school = document.getElementById('school').value;
  const file = document.getElementById('file-input').files[0];

  if (currentlyEditedQuestion) {
    // Update an existing question
    currentlyEditedQuestion.subject = subject;
    currentlyEditedQuestion.title = title;
    currentlyEditedQuestion.content = content;
    currentlyEditedQuestion.file = file ? file.name : null;
    currentlyEditedQuestion.school = school;
    currentlyEditedQuestion.updatedAt = new Date().toISOString();

    // Update the corresponding row in the table
    const rowIndex = questions.findIndex(q => q.id === currentlyEditedQuestion.id);
    const row = tbody.children[rowIndex];
    row.children[1].textContent = currentlyEditedQuestion.subject;
    row.children[2].textContent = currentlyEditedQuestion.title;
    row.children[3].textContent = currentlyEditedQuestion.content;
    row.children[4].textContent = currentlyEditedQuestion.file ? 'Attached' : 'None';
    row.children[5].textContent = currentlyEditedQuestion.school;
    row.children[7].textContent = new Date(currentlyEditedQuestion.updatedAt).toLocaleString();

    currentlyEditedQuestion = null; // Reset the currently edited question
  } else {
    // Create a new question
    const newQuestion = {
      id: questions.length + 1,
      subject,
      title,
      content,
      file: file ? file.name : null,
      school,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      votes: 0
    };

    questions.push(newQuestion);
    createRow(newQuestion);
  }

  // Clear the form
  form.reset();
});

// Show the download button if a file was uploaded
// Show the download button if a file was uploaded
if (currentlyEditedQuestion && currentlyEditedQuestion.file) {
  downloadBtn.style.display = 'inline-block';
  downloadBtn.addEventListener('click', () => downloadFile(currentlyEditedQuestion.file));
} else {
  downloadBtn.style.display = 'none';
}



// Function to edit a question
function editQuestion(id) {
  const question = questions.find(q => q.id === id);
  if (question) {
    currentlyEditedQuestion = question;
    document.getElementById('subject').value = question.subject;
    document.getElementById('title').value = question.title;
    document.getElementById('question-text').value = question.content;
    document.getElementById('school').value = question.school;
    document.getElementById('file-input').value = ''; // Clear the file input
  }
}

// Function to delete a question
function deleteQuestion(id) {
  const index = questions.findIndex(q => q.id === id);
  if (index !== -1) {
    questions.splice(index, 1);
    tbody.removeChild(tbody.children[index]);
  }
}

// Function to download the file
function downloadFile(fileName) {
  const questions = questions.find(q => q.file === fileName);
  if (questions) {
    // Create a temporary download link
    const downloadLink = document.createElement('a');
    downloadLink.href = URL.createObjectURL(new Blob([questions.file], { type: 'application/octet-stream' }));
    downloadLink.download = fileName;

    // Append the link to the DOM, click it, and remove it
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
  }
};
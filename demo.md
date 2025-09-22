---
layout: default
title: ENS Grades Demo
slug: /demo.html
---

<style>
.demo-content {
  text-align: justify;
  max-width: 900px;
  margin: 0 auto;
}

.demo-content h1 {
  font-weight: 300;
  color: #111;
  margin-bottom: 20px;
  text-align: center;
}

.demo-content h2 {
  font-weight: 300;
  color: #111;
  margin-bottom: 15px;
}

.demo-content h3 {
  font-weight: 300;
  color: #3953a5;
  margin-top: 0;
  margin-bottom: 15px;
}

.demo-content h4 {
  font-weight: 300;
  color: #111;
  margin-bottom: 10px;
}

.demo-content h5 {
  font-weight: 600;
  color: #111;
  margin-bottom: 8px;
}

.demo-content p {
  font-weight: 300;
  color: #111;
  margin-bottom: 15px;
  text-align: justify;
}

.demo-section {
  background: #f8f9fa;
  border-left: 4px solid #3953a5;
  padding: 20px;
  margin: 20px 0;
  border-radius: 0 5px 5px 0;
}

.input-group {
  margin-bottom: 20px;
}

.input-group label {
  display: block;
  font-weight: 300;
  margin-bottom: 5px;
  color: #111;
}

.file-input-wrapper {
  position: relative;
  display: inline-block;
  cursor: pointer;
  width: 100%;
}

.file-input {
  position: absolute;
  left: -9999px;
}

.file-input-button {
  display: inline-block;
  padding: 12px 24px;
  background: #fff;
  border: 2px dashed #3953a5;
  border-radius: 3px;
  color: #3953a5;
  text-align: center;
  transition: all 0.3s;
  width: 100%;
  cursor: pointer;
  font-weight: 300;
  font-size: 14px;
  box-sizing: border-box;
}

.file-input-button:hover {
  background: #3953a5;
  color: white;
  text-decoration: none;
}

.file-selected {
  border: 2px solid #28a745;
  background: #d4edda;
  color: #155724;
}

.example-button {
  background: #3953a5;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 3px;
  cursor: pointer;
  margin-left: 10px;
  transition: background 0.3s;
  font-weight: 300;
  font-size: 14px;
  text-decoration: none;
  display: inline-block;
}

.example-button:hover {
  background: #2c4282;
  text-decoration: none;
  color: white;
}

.form-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 3px;
  font-size: 14px;
  font-weight: 300;
  color: #111;
  box-sizing: border-box;
}

.form-input:focus {
  outline: none;
  border-color: #3953a5;
  box-shadow: 0 0 5px rgba(57, 83, 165, 0.3);
}

.generate-button {
  background: #3953a5;
  color: white;
  padding: 15px 30px;
  border: none;
  border-radius: 3px;
  font-size: 16px;
  font-weight: 300;
  cursor: pointer;
  width: 100%;
  margin-top: 20px;
  transition: background 0.3s;
}

.generate-button:hover {
  background: #2c4282;
}

.generate-button:disabled {
  background: #6c757d;
  cursor: not-allowed;
}

.tab-container {
  margin-bottom: 20px;
}

.tab-buttons {
  display: flex;
  border-bottom: 1px solid #ddd;
  margin-bottom: 15px;
}

.tab-button {
  background: none;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  border-bottom: 2px solid transparent;
  transition: all 0.3s;
  font-weight: 300;
  color: #111;
}

.tab-button.active {
  border-bottom-color: #3953a5;
  color: #3953a5;
  font-weight: 300;
}

.tab-button:hover {
  color: #3953a5;
}

.tab-content {
  display: none;
}

.tab-content.active {
  display: block;
}

.info-box {
  background: #f8f9fa;
  border: 1px solid #3953a5;
  border-radius: 3px;
  padding: 20px;
  margin: 20px 0;
}

.info-box h4 {
  margin-top: 0;
  color: #3953a5;
  font-weight: 300;
}

.info-box h5 {
  color: #111;
  font-weight: 300;
  margin-bottom: 8px;
}

.info-box p {
  margin-bottom: 10px;
}

.info-box ul {
  margin-bottom: 10px;
}

.info-box li {
  font-weight: 300;
  color: #111;
}

.grades-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
  font-size: 14px;
}

.grades-table th,
.grades-table td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: left;
}

.grades-table th {
  background: #f8f9fa;
  font-weight: 300;
  color: #111;
}

.add-grade-button {
  background: #3953a5;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 3px;
  cursor: pointer;
  margin-top: 10px;
  font-weight: 300;
  font-size: 14px;
  transition: background 0.3s;
}

.add-grade-button:hover {
  background: #2c4282;
}

.remove-grade-button {
  background: #dc3545;
  color: white;
  border: none;
  padding: 4px 8px;
  border-radius: 3px;
  cursor: pointer;
  font-size: 12px;
  font-weight: 300;
}

.remove-grade-button:hover {
  background: #c82333;
}

.status-message {
  padding: 10px 15px;
  border-radius: 3px;
  margin: 10px 0;
  display: none;
  font-weight: 300;
}

.status-success {
  background: #d4edda;
  border: 1px solid #c3e6cb;
  color: #155724;
}

.status-error {
  background: #f8d7da;
  border: 1px solid #f5c6cb;
  color: #721c24;
}

.status-info {
  background: #cce5ff;
  border: 1px solid #99ccff;
  color: #004085;
}

.upload-mode-section {
  transition: opacity 0.3s ease;
}

.upload-mode-section.hidden {
  display: none;
}

/* Radio button styling */
input[type="radio"] {
  accent-color: #3953a5;
}

/* Mobile responsive */
@media screen and (max-width: 600px) {
  .demo-content {
    padding: 0 15px;
  }
  
  .demo-section {
    padding: 15px;
  }
  
  .tab-buttons {
    flex-wrap: wrap;
  }
  
  .tab-button {
    flex: 1;
    min-width: 100px;
  }
  
  .example-button {
    margin-left: 0;
    margin-top: 10px;
    display: block;
    text-align: center;
  }
  
  .grades-table {
    font-size: 12px;
  }
  
  .grades-table th,
  .grades-table td {
    padding: 8px 5px;
  }
}
</style>

<div class="demo-content">
  <h1>ENS Grades Generator Demo</h1>
  <p style="text-align: center; margin-bottom: 30px;">Generate professional academic transcripts with GPA conversion for international applications</p>

  <div class="info-box">
    <h4>How it works</h4>
    <p>This tool generates academic transcripts from ENS Rennes grades with automatic conversion to international GPA standards. You can:</p>
    <ul>
      <li><strong>Upload Files:</strong> Use your own files (single student or batch mode with Excel)</li>
      <li><strong>Manual Input:</strong> Fill forms directly in the browser</li>
    </ul>
    <p><strong>Note:</strong> This connects to a Vercel-deployed API for PDF generation.</p>
    
    <div style="text-align: center; margin: 20px 0;">
      <button type="button" class="example-button" onclick="testAPIConnection()" style="margin-right: 10px; background: #28a745;">
        🔗 Test API Connection
      </button>
      <a href="/downloads/example_files.zip" download class="example-button" style="margin-left: 0; font-size: 16px; padding: 15px 30px;">
        📁 Download All Example Files (ZIP)
      </a>
    </div>
  </div>

  <div class="tab-container">
    <div class="tab-buttons">
      <button class="tab-button active" onclick="switchTab('upload', this)">Upload Files</button>
      <button class="tab-button" onclick="switchTab('manual', this)">Manual Input</button>
    </div>

    <!-- Upload Files Tab -->
    <div id="upload" class="tab-content active">
      <div class="demo-section">
        <h3>Upload Your Files</h3>
        
        <div class="input-group">
          <label>Select Processing Mode</label>
          <div style="display: flex; gap: 20px; margin-bottom: 20px;">
            <label style="display: flex; align-items: center; cursor: pointer;">
              <input type="radio" name="upload-mode" value="single" checked onchange="toggleUploadMode()" style="margin-right: 8px;">
              Single Student
            </label>
            <label style="display: flex; align-items: center; cursor: pointer;">
              <input type="radio" name="upload-mode" value="batch" onchange="toggleUploadMode()" style="margin-right: 8px;">
              Batch Processing (Excel)
            </label>
          </div>
        </div>

        <!-- Single Mode Upload -->
        <div id="single-upload" class="upload-mode-section">
          <div class="input-group">
            <label for="student-file">Student Information (YAML file)</label>
            <div class="file-input-wrapper">
              <input type="file" id="student-file" class="file-input" accept=".yaml,.yml" onchange="handleFileUpload(this, 'student')">
              <label for="student-file" class="file-input-button" id="student-file-label">
                Click to upload student info file (YAML)
              </label>
            </div>
          </div>

          <div class="input-group">
            <label for="author-file">Author Information (YAML file)</label>
            <div class="file-input-wrapper">
              <input type="file" id="author-file" class="file-input" accept=".yaml,.yml" onchange="handleFileUpload(this, 'author')">
              <label for="author-file" class="file-input-button" id="author-file-label">
                Click to upload author info file (YAML)
              </label>
            </div>
          </div>

          <div class="input-group">
            <label for="grades-file">Grades Data (JSON file)</label>
            <div class="file-input-wrapper">
              <input type="file" id="grades-file" class="file-input" accept=".json" onchange="handleFileUpload(this, 'grades')">
              <label for="grades-file" class="file-input-button" id="grades-file-label">
                Click to upload grades file (JSON)
              </label>
            </div>
          </div>
        </div>

        <!-- Batch Mode Upload -->
        <div id="batch-upload" class="upload-mode-section" style="display: none;">
          <div class="input-group">
            <label for="excel-file">Students Excel File (.xlsx)</label>
            <div class="file-input-wrapper">
              <input type="file" id="excel-file" class="file-input" accept=".xlsx,.xls" onchange="handleFileUpload(this, 'excel')">
              <label for="excel-file" class="file-input-button" id="excel-file-label">
                Click to upload Excel file with student data
              </label>
            </div>
          </div>

          <div class="input-group">
            <label for="author-file-batch">Author Information (YAML file)</label>
            <div class="file-input-wrapper">
              <input type="file" id="author-file-batch" class="file-input" accept=".yaml,.yml" onchange="handleFileUpload(this, 'author-batch')">
              <label for="author-file-batch" class="file-input-button" id="author-file-batch-label">
                Click to upload author info file (YAML)
              </label>
            </div>
          </div>

          <div class="info-box">
            <h4>Excel File Format Requirements</h4>
            <p>Your Excel file should contain the following columns:</p>
            <ul>
              <li><strong>Student Info:</strong> Etud_Nom (Last Name), Etud_Prénom (First Name), Etud_Naissance (Birth Date), Etud_Ville (Birth City)</li>
              <li><strong>Courses:</strong> Columns with patterns like "Obj1_Libellé", "Obj1_Note_Ado/20", "Obj1_Crédits"</li>
              <li><strong>Notes:</strong> Only courses with Type="ELP" will be included in the transcript</li>
            </ul>
            <p><em>Example: "Obj1_Libellé" = "Programming 1", "Obj1_Note_Ado/20" = "16.5", "Obj1_Crédits" = "6"</em></p>
          </div>
        </div>
      </div>
    </div>

    <!-- Manual Input Tab -->
    <div id="manual" class="tab-content">
      <div style="text-align: center; margin-bottom: 20px;">
        <button type="button" class="example-button" onclick="loadExampleData()" style="margin-left: 0; background: #3953a5; padding: 12px 24px;">
          📝 Fill with Example Data
        </button>
      </div>

      <div class="demo-section">
        <h3>Student Information</h3>
        <div class="input-group">
          <label for="student-gender">Gender</label>
          <select id="student-gender" class="form-input">
            <option value="Mr">Mr</option>
            <option value="Ms">Ms</option>
          </select>
        </div>
        <div class="input-group">
          <label for="student-firstname">First Name</label>
          <input type="text" id="student-firstname" class="form-input" placeholder="Jean">
        </div>
        <div class="input-group">
          <label for="student-name">Last Name</label>
          <input type="text" id="student-name" class="form-input" placeholder="DUPONT">
        </div>
        <div class="input-group">
          <label for="student-pronoun">Pronoun</label>
          <select id="student-pronoun" class="form-input">
            <option value="he">he</option>
            <option value="she">she</option>
            <option value="they">they</option>
          </select>
        </div>
        <div class="input-group">
          <label for="student-dob">Date of Birth</label>
          <input type="text" id="student-dob" class="form-input" placeholder="26th of August 2000">
        </div>
        <div class="input-group">
          <label for="student-pob">Place of Birth</label>
          <input type="text" id="student-pob" class="form-input" placeholder="Rennes (FRANCE)">
        </div>
      </div>

      <div class="demo-section">
        <h3>Author Information</h3>
        <div class="input-group">
          <label for="author-gender">Gender</label>
          <select id="author-gender" class="form-input">
            <option value="Mr">Mr</option>
            <option value="Ms">Ms</option>
          </select>
        </div>
        <div class="input-group">
          <label for="author-firstname">First Name</label>
          <input type="text" id="author-firstname" class="form-input" placeholder="Martin">
        </div>
        <div class="input-group">
          <label for="author-name">Last Name</label>
          <input type="text" id="author-name" class="form-input" placeholder="QUINSON">
        </div>
        <div class="input-group">
          <label for="author-field">Field</label>
          <input type="text" id="author-field" class="form-input" placeholder="Computer Science">
        </div>
        <div class="input-group">
          <label for="author-title">Title</label>
          <input type="text" id="author-title" class="form-input" placeholder="Director of the Computer Sciences teaching department">
        </div>
        <div class="input-group">
          <label for="author-schoolyear">School Year</label>
          <input type="text" id="author-schoolyear" class="form-input" placeholder="2023-2024">
        </div>
        <div class="input-group">
          <label for="author-yearname">Year Name</label>
          <input type="text" id="author-yearname" class="form-input" placeholder="First year of Master's degree in Computer Science">
        </div>
      </div>

      <div class="demo-section">
        <h3>Grades</h3>
        <table class="grades-table" id="grades-table">
          <thead>
            <tr>
              <th>Course Name</th>
              <th>Grade (/20)</th>
              <th>ECTS Credits</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody id="grades-tbody">
            <tr>
              <td><input type="text" class="form-input" placeholder="Programming 1" value="Programming 1"></td>
              <td><input type="number" class="form-input" step="0.1" min="0" max="20" placeholder="16.5" value="16.5"></td>
              <td><input type="number" class="form-input" step="1" min="0" placeholder="6" value="6"></td>
              <td><button type="button" class="remove-grade-button" onclick="removeGradeRow(this)">Remove</button></td>
            </tr>
          </tbody>
        </table>
        <button type="button" class="add-grade-button" onclick="addGradeRow()">Add Grade</button>
      </div>
    </div>

  <div class="status-message" id="status-message"></div>

  <button type="button" class="generate-button" onclick="generateTranscript()" id="generate-btn">
    Generate Transcript (Demo)
  </button>

  <div id="result-section" style="display: none; margin-top: 30px;">
    <div class="demo-section">
      <h3>Generated Transcript Preview</h3>
      <div class="info-box">
        <h4>Transcript Generated Successfully!</h4>
        <p>In the full version with Vercel integration, this would generate and download a PDF file.</p>
        <div id="transcript-summary"></div>
      </div>
    </div>
  </div>
</div>

<script>
// API Configuration - Points to ENSGrading API deployed on Railway
const API_BASE_URL = 'https://ensgrading-production.up.railway.app';

// Global variables
let uploadedFiles = {
  student: null,
  author: null,
  grades: null,
  excel: null,
  'author-batch': null
};

// =============================================================================
// UI INTERACTION FUNCTIONS
// =============================================================================

function switchTab(tabName, clickedButton) {
  // Hide all tab contents
  const contents = document.querySelectorAll('.tab-content');
  contents.forEach(content => content.classList.remove('active'));
  
  // Remove active class from all buttons
  const buttons = document.querySelectorAll('.tab-button');
  buttons.forEach(button => button.classList.remove('active'));
  
  // Show selected tab and activate button
  document.getElementById(tabName).classList.add('active');
  
  // If no button reference passed, find it by the onclick attribute
  if (!clickedButton) {
    clickedButton = document.querySelector(`.tab-button[onclick*="'${tabName}'"]`);
  }
  
  if (clickedButton) {
    clickedButton.classList.add('active');
  }
}

function toggleUploadMode() {
  const uploadMode = document.querySelector('input[name="upload-mode"]:checked').value;
  const singleUpload = document.getElementById('single-upload');
  const batchUpload = document.getElementById('batch-upload');
  
  if (uploadMode === 'single') {
    singleUpload.style.display = 'block';
    batchUpload.style.display = 'none';
  } else {
    singleUpload.style.display = 'none';
    batchUpload.style.display = 'block';
  }
}

function handleFileUpload(input, type) {
  const file = input.files[0];
  if (!file) {
    return;
  }

  // Handle inconsistent label naming
  let labelId;
  if (type === 'author-batch') {
    labelId = 'author-file-batch-label';
  } else {
    labelId = `${type}-file-label`;
  }
  
  const label = document.getElementById(labelId);
  
  if (label) {
    label.textContent = `✓ ${file.name}`;
    label.classList.add('file-selected');
  } else {
    console.error('Label not found for ID:', labelId);
    showStatus(`Error: Could not find label for ${type} file upload`, 'error');
    return;
  }
  
  uploadedFiles[type] = file;
}

// =============================================================================
// API INTERACTION FUNCTIONS
// =============================================================================

async function testAPIConnection() {
  showStatus('Testing API connection...', 'info');
  
  try {
    // Test the main endpoint first
    const testUrl = `${API_BASE_URL}/`;
    const getResponse = await fetch(testUrl, { method: 'GET' });
    
    if (getResponse.ok) {
      // Test CORS with OPTIONS request
      const apiUrl = `${API_BASE_URL}/api/single`;
      const optionsResponse = await fetch(apiUrl, { method: 'OPTIONS' });
      
      if (optionsResponse.ok) {
        showStatus('✅ API connection successful! CORS is working properly.', 'success');
      } else {
        showStatus(`⚠️ OPTIONS request failed with status ${optionsResponse.status}. Check console for details.`, 'error');
      }
    } else {
      showStatus(`⚠️ Main endpoint failed with status ${getResponse.status}. Check console for details.`, 'error');
    }
    
  } catch (error) {
    console.error('API connection test failed:', error);
    
    if (error.name === 'TypeError' && error.message.includes('fetch')) {
      showStatus('❌ API connection failed: Cannot reach the server. The API may not be deployed yet.', 'error');
    } else {
      showStatus('❌ API connection failed: ' + error.message, 'error');
    }
  }
}

// =============================================================================
// FORM AND DATA HANDLING FUNCTIONS
// =============================================================================

function addGradeRow() {
  const tbody = document.getElementById('grades-tbody');
  const row = document.createElement('tr');
  row.innerHTML = `
    <td><input type="text" class="form-input" placeholder="Course name"></td>
    <td><input type="number" class="form-input" step="0.1" min="0" max="20" placeholder="Grade"></td>
    <td><input type="number" class="form-input" step="1" min="0" placeholder="ECTS"></td>
    <td><button type="button" class="remove-grade-button" onclick="removeGradeRow(this)">Remove</button></td>
  `;
  tbody.appendChild(row);
}

function removeGradeRow(button) {
  const row = button.closest('tr');
  row.remove();
}

function loadExampleData() {
  // Fill manual input fields with example data
  document.getElementById('student-gender').value = 'Mr';
  document.getElementById('student-firstname').value = 'Jean';
  document.getElementById('student-name').value = 'DUPONT';
  document.getElementById('student-pronoun').value = 'he';
  document.getElementById('student-dob').value = '26th of August 2000';
  document.getElementById('student-pob').value = 'Rennes (FRANCE)';
  
  document.getElementById('author-gender').value = 'Mr';
  document.getElementById('author-firstname').value = 'Martin';
  document.getElementById('author-name').value = 'QUINSON';
  document.getElementById('author-field').value = 'Computer Science';
  document.getElementById('author-title').value = 'Director of the Computer Sciences teaching department';
  document.getElementById('author-schoolyear').value = '2023-2024';
  document.getElementById('author-yearname').value = 'First year of Master\'s degree in Computer Science';
  
  // Clear existing grades and add example grades
  const tbody = document.getElementById('grades-tbody');
  tbody.innerHTML = `
    <tr>
      <td><input type="text" class="form-input" value="Programming 1"></td>
      <td><input type="number" class="form-input" step="0.1" min="0" max="20" value="16.5"></td>
      <td><input type="number" class="form-input" step="1" min="0" value="6"></td>
      <td><button type="button" class="remove-grade-button" onclick="removeGradeRow(this)">Remove</button></td>
    </tr>
    <tr>
      <td><input type="text" class="form-input" value="Algorithms"></td>
      <td><input type="number" class="form-input" step="0.1" min="0" max="20" value="14.2"></td>
      <td><input type="number" class="form-input" step="1" min="0" value="6"></td>
      <td><button type="button" class="remove-grade-button" onclick="removeGradeRow(this)">Remove</button></td>
    </tr>
    <tr>
      <td><input type="text" class="form-input" value="Mathematics"></td>
      <td><input type="number" class="form-input" step="0.1" min="0" max="20" value="12.8"></td>
      <td><input type="number" class="form-input" step="1" min="0" value="3"></td>
      <td><button type="button" class="remove-grade-button" onclick="removeGradeRow(this)">Remove</button></td>
    </tr>
  `;
  
  // Switch to manual tab if not already there
  const manualTab = document.getElementById('manual');
  if (!manualTab.classList.contains('active')) {
    switchTab('manual');
  }
  
  showStatus('Example data loaded successfully!', 'success');
}

// =============================================================================
// UTILITY FUNCTIONS
// =============================================================================

function showStatus(message, type) {
  const statusDiv = document.getElementById('status-message');
  statusDiv.textContent = message;
  statusDiv.className = `status-message status-${type}`;
  statusDiv.style.display = 'block';
  
  setTimeout(() => {
    statusDiv.style.display = 'none';
  }, 5000);
}

function calculateGPA(grade) {
  if (grade >= 16) return { gpa: '4.0', letter: 'A+' };
  if (grade >= 14) return { gpa: '4.0', letter: 'A' };
  if (grade >= 13) return { gpa: '3.7', letter: 'A-' };
  if (grade >= 12) return { gpa: '3.33', letter: 'B+' };
  if (grade >= 11) return { gpa: '3.0', letter: 'B' };
  if (grade >= 10) return { gpa: '2.7', letter: 'B-' };
  if (grade >= 9) return { gpa: '2.33', letter: 'C+' };
  if (grade >= 8) return { gpa: '2.0', letter: 'C' };
  if (grade >= 7) return { gpa: '1.7', letter: 'C-' };
  return { gpa: '0.0', letter: 'F' };
}

// =============================================================================
// TRANSCRIPT GENERATION FUNCTIONS
// =============================================================================

function generateTranscript() {
  try {
    // Get data from current active tab
    const activeTab = document.querySelector('.tab-content.active').id;

    if (activeTab === 'upload') {
      // Check upload mode
      const uploadMode = document.querySelector('input[name="upload-mode"]:checked').value;
      
      if (uploadMode === 'single') {
        handleSingleUploadGeneration();
      } else {
        handleBatchUploadGeneration();
      }
      return;
    } else {
      handleManualInputGeneration();
    }

  } catch (error) {
    showStatus('Error generating transcript: ' + error.message, 'error');
  }
}

async function handleSingleUploadGeneration() {
  // Check if files are uploaded for single mode
  if (!uploadedFiles.student || !uploadedFiles.author || !uploadedFiles.grades) {
    showStatus('Please upload all required files (student info, author info, and grades).', 'error');
    return;
  }

  showStatus('Generating transcript...', 'info');
  
  try {
    // Create FormData object
    const formData = new FormData();
    formData.append('student_info', uploadedFiles.student);
    formData.append('author_info', uploadedFiles.author);
    formData.append('grades', uploadedFiles.grades);

    // Call API
    const response = await fetch(`${API_BASE_URL}/api/single`, {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`HTTP ${response.status}: ${errorText}`);
    }

    const result = await response.json();

    // Handle successful response
    downloadPDFFromBase64(result.pdf_data, result.filename);
    showTranscriptResult('single', result);
    showStatus(`Transcript generated successfully for ${result.student_name}!`, 'success');

  } catch (error) {
    console.error('Full error:', error);
    if (error.name === 'TypeError' && error.message.includes('fetch')) {
      showStatus('Network error: Unable to connect to the API. Please check if the API is deployed and accessible.', 'error');
    } else {
      showStatus('Error generating transcript: ' + error.message, 'error');
    }
  }
}

async function handleBatchUploadGeneration() {
  // Check if Excel and author files are uploaded
  if (!uploadedFiles.excel || !uploadedFiles['author-batch']) {
    showStatus('Please upload both Excel file and author info file for batch processing.', 'error');
    return;
  }

  showStatus('Processing batch generation...', 'info');
  
  try {
    // Create FormData object
    const formData = new FormData();
    formData.append('students_excel', uploadedFiles.excel);
    formData.append('author_info', uploadedFiles['author-batch']);

    // Call Vercel API
    const response = await fetch(`${API_BASE_URL}/api/batch`, {
      method: 'POST',
      body: formData
    });

    const result = await response.json();

    if (!response.ok) {
      throw new Error(result.error || 'Failed to generate batch transcripts');
    }

    // Handle successful response
    downloadZipFromBase64(result.zip_data, result.filename);
    showTranscriptResult('batch', result);
    showStatus(`Batch processing completed! Generated ${result.generated_count} transcripts.`, 'success');

  } catch (error) {
    showStatus('Error generating batch transcripts: ' + error.message, 'error');
  }
}

async function handleManualInputGeneration() {
  showStatus('Generating transcript from manual input...', 'info');
  
  try {
    // Get data from manual input
    const studentData = {
      gender: document.getElementById('student-gender').value,
      firstname: document.getElementById('student-firstname').value,
      name: document.getElementById('student-name').value,
      pronoun: document.getElementById('student-pronoun').value,
      dob: document.getElementById('student-dob').value,
      pob: document.getElementById('student-pob').value
    };

    const authorData = {
      gender: document.getElementById('author-gender').value,
      firstname: document.getElementById('author-firstname').value,
      name: document.getElementById('author-name').value,
      field: document.getElementById('author-field').value,
      title: document.getElementById('author-title').value,
      schoolyear: document.getElementById('author-schoolyear').value,
      yearname: document.getElementById('author-yearname').value
    };

    // Get grades from table
    const gradesData = {};
    const rows = document.querySelectorAll('#grades-tbody tr');

    for (let row of rows) {
      const inputs = row.querySelectorAll('input');
      const courseName = inputs[0].value.trim();
      const grade = parseFloat(inputs[1].value);
      const ects = parseInt(inputs[2].value);

      if (courseName && !isNaN(grade) && !isNaN(ects)) {
        gradesData[courseName] = [grade, ects];
      }
    }

    // Validate required fields
    if (!studentData.firstname || !studentData.name || Object.keys(gradesData).length === 0) {
      showStatus('Please fill in all required fields.', 'error');
      return;
    }

    // Create YAML and JSON content
    const studentYaml = `student:
  gender: ${studentData.gender}
  name: ${studentData.name}
  firstname: ${studentData.firstname}
  pronoun: ${studentData.pronoun}
  dob: ${studentData.dob}
  pob: ${studentData.pob}`;

    const authorYaml = `author:
  gender: ${authorData.gender}
  name: ${authorData.name}
  firstname: ${authorData.firstname}
  field: ${authorData.field}
  title: ${authorData.title}
  schoolyear: "${authorData.schoolyear}"
  yearname: ${authorData.yearname}`;

    const gradesJson = JSON.stringify(gradesData, null, 2);

    // Create FormData object
    const formData = new FormData();
    formData.append('student_info', new Blob([studentYaml], { type: 'text/plain' }));
    formData.append('author_info', new Blob([authorYaml], { type: 'text/plain' }));
    formData.append('grades', new Blob([gradesJson], { type: 'application/json' }));

    // Call Vercel API
    const response = await fetch(`${API_BASE_URL}/api/single`, {
      method: 'POST',
      body: formData
    });

    const result = await response.json();

    if (!response.ok) {
      throw new Error(result.error || 'Failed to generate transcript');
    }

    // Handle successful response
    downloadPDFFromBase64(result.pdf_data, result.filename);
    showTranscriptResult('single', result);
    showStatus(`Transcript generated successfully for ${result.student_name}!`, 'success');

  } catch (error) {
    showStatus('Error generating transcript: ' + error.message, 'error');
  }
}

// =============================================================================
// FILE DOWNLOAD FUNCTIONS
// =============================================================================

function downloadPDFFromBase64(base64Data, filename) {
  try {
    // Convert base64 to blob
    const binaryString = atob(base64Data);
    const bytes = new Uint8Array(binaryString.length);
    for (let i = 0; i < binaryString.length; i++) {
      bytes[i] = binaryString.charCodeAt(i);
    }
    const blob = new Blob([bytes], { type: 'application/pdf' });

    // Create download link
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    link.style.display = 'none';
    
    // Trigger download
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    // Clean up
    URL.revokeObjectURL(url);
  } catch (error) {
    showStatus('Error downloading PDF: ' + error.message, 'error');
  }
}

function downloadZipFromBase64(base64Data, filename) {
  try {
    // Convert base64 to blob
    const binaryString = atob(base64Data);
    const bytes = new Uint8Array(binaryString.length);
    for (let i = 0; i < binaryString.length; i++) {
      bytes[i] = binaryString.charCodeAt(i);
    }
    const blob = new Blob([bytes], { type: 'application/zip' });

    // Create download link
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    link.style.display = 'none';
    
    // Trigger download
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    // Clean up
    URL.revokeObjectURL(url);
  } catch (error) {
    showStatus('Error downloading ZIP: ' + error.message, 'error');
  }
}

function showTranscriptResult(mode, result) {
  const resultSection = document.getElementById('result-section');
  const summaryDiv = document.getElementById('transcript-summary');
  
  if (mode === 'single') {
    summaryDiv.innerHTML = `
      <h5>✅ Transcript Generated Successfully!</h5>
      <p><strong>Student:</strong> ${result.student_name}</p>
      <p><strong>File:</strong> ${result.filename}</p>
      <p><em>The PDF transcript has been automatically downloaded to your device.</em></p>
    `;
  } else if (mode === 'batch') {
    const studentList = result.student_names.map(name => `<li>${name}</li>`).join('');
    summaryDiv.innerHTML = `
      <h5>✅ Batch Processing Completed!</h5>
      <p><strong>Generated Transcripts:</strong> ${result.generated_count}</p>
      <p><strong>ZIP File:</strong> ${result.filename}</p>
      <p><strong>Students Processed:</strong></p>
      <ul>${studentList}</ul>
      <p><em>The ZIP file containing all transcripts has been automatically downloaded to your device.</em></p>
    `;
  }
  
  resultSection.style.display = 'block';
  resultSection.scrollIntoView({ behavior: 'smooth' });
}
</script>
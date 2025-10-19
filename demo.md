---
layout: default
title: Démo Bulletin ENS
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
  <h1>Démo du Générateur de Relevés ENS</h1>
  <p style="text-align: center; margin-bottom: 30px;">Génération des relevés de notes académiques avec conversion GPA pour les candidatures à l'international</p>

  <div class="info-box">
    <h4>Comment ça marche</h4>
    <p>Cet outil génère des relevés académiques à partir des notes de l'ENS Rennes avec conversion automatique aux standards internationaux de GPA. Vous pouvez :</p>
    <ul>
      <li><strong>Mode étudiant unique :</strong> Génère un bulletin pour un seul étudiant</li>
      <li><strong>Mode traitement par lot :</strong> Traitement multiple d'étudiants à partir d'un fichier Excel</li>
    </ul>
    
    <div style="text-align: center; margin: 20px 0;">
      <a href="/downloads/example_files.zip" download class="example-button" style="margin-left: 0; font-size: 16px; padding: 15px 30px;">
        📁 Télécharger des fichiers d'exemple (ZIP)
      </a>
    </div>
  </div>

  <div class="tab-container">
    <div id="upload" class="tab-content active">
      <div class="demo-section">
        <h3>Ajoutez vos fichiers</h3>
        
        <div class="input-group">
          <label>Sélectionnez le mode de traitement</label>
          <div style="display: flex; gap: 20px; margin-bottom: 20px;">
            <label style="display: flex; align-items: center; cursor: pointer;">
              <input type="radio" name="upload-mode" value="single" checked onchange="toggleUploadMode()" style="margin-right: 8px;">
              Étudiant unique
            </label>
            <label style="display: flex; align-items: center; cursor: pointer;">
              <input type="radio" name="upload-mode" value="batch" onchange="toggleUploadMode()" style="margin-right: 8px;">
              Traitement par lot (Excel)
            </label>
          </div>
        </div>

        <!-- Single Mode Upload -->
        <div id="single-upload" class="upload-mode-section">
          <div class="input-group">
            <label for="student-file">Informations sur l'étudiant (fichier YAML)</label>
            <div class="file-input-wrapper">
              <input type="file" id="student-file" class="file-input" accept=".yaml,.yml" onchange="handleFileUpload(this, 'student')">
              <label for="student-file" class="file-input-button" id="student-file-label">
                Informations de l'étudiant (YAML)
              </label>
            </div>
          </div>

          <div class="input-group">
            <label for="author-file">Informations sur l'auteur (fichier YAML)</label>
            <div class="file-input-wrapper">
              <input type="file" id="author-file" class="file-input" accept=".yaml,.yml" onchange="handleFileUpload(this, 'author')">
              <label for="author-file" class="file-input-button" id="author-file-label">
                Informations de l'auteur (YAML)
              </label>
            </div>
          </div>

          <div class="input-group">
            <label for="year-file">Informations sur l'année (fichier YAML)</label>
            <div class="file-input-wrapper">
              <input type="file" id="year-file" class="file-input" accept=".yaml,.yml" onchange="handleFileUpload(this, 'year')">
              <label for="year-file" class="file-input-button" id="year-file-label">
                Informations de l'année (YAML)
              </label>
            </div>
          </div>
          
          <div class="input-group">
            <label for="grades-file">Données des notes (fichier JSON)</label>
            <div class="file-input-wrapper">
              <input type="file" id="grades-file" class="file-input" accept=".json" onchange="handleFileUpload(this, 'grades')">
              <label for="grades-file" class="file-input-button" id="grades-file-label">
                Notes (JSON)
              </label>
            </div>
          </div>
        </div>

        <!-- Batch Mode Upload -->
        <div id="batch-upload" class="upload-mode-section" style="display: none;">
          <div class="input-group">
            <label for="excel-file">Fichier Excel des étudiants (.xlsx)</label>
            <div class="file-input-wrapper">
              <input type="file" id="excel-file" class="file-input" accept=".xlsx,.xls" onchange="handleFileUpload(this, 'excel')">
              <label for="excel-file" class="file-input-button" id="excel-file-label">
                Excel avec les données des étudiants
              </label>
            </div>
          </div>

          <div class="input-group">
            <label for="author-file-batch">Informations sur l'auteur (fichier YAML)</label>
            <div class="file-input-wrapper">
              <input type="file" id="author-file-batch" class="file-input" accept=".yaml,.yml" onchange="handleFileUpload(this, 'author-batch')">
              <label for="author-file-batch" class="file-input-button" id="author-file-batch-label">
                Informations de l'auteur (YAML)
              </label>
            </div>
          </div>
          
          <div class="input-group">
            <label>Afficher les classements (ranking)</label>
            <div style="display: flex; gap: 20px; margin-bottom: 20px;">
              <label style="display: flex; align-items: center; cursor: pointer;">
                <input type="radio" name="display-rank" value="false" checked style="margin-right: 8px;">
                Non
              </label>
              <label style="display: flex; align-items: center; cursor: pointer;">
                <input type="radio" name="display-rank" value="true" style="margin-right: 8px;">
                Oui
              </label>
            </div>
          </div>

          <div class="info-box">
            <h4>Exigences de format pour le fichier Excel</h4>
            <p>Votre fichier Excel doit contenir les colonnes suivantes :</p>
            <ul>
              <li><strong>Informations sur l'étudiant :</strong> Etud_Nom, Etud_Prénom, Etud_Naissance (Date de naissance), Etud_Ville (Ville de naissance)</li>
              <li><strong>Cours :</strong> Colonnes avec des motifs comme "Obj1_Libellé", "Obj1_Note_Ado/20", "Obj1_Crédits"</li>
              <li><strong>Remarques :</strong> Seuls les cours avec Type="ELP" seront inclus dans le relevé</li>
            </ul>
            <p><em>Exemple : "Obj1_Libellé" = "Programmation 1", "Obj1_Note_Ado/20" = "16.5", "Obj1_Crédits" = "6"</em></p>
          </div>
        </div>
      </div>
    </div>

  <div class="status-message" id="status-message"></div>

  <button type="button" class="generate-button" onclick="generateTranscript()" id="generate-btn">
    Générer le relevé de notes
  </button>
</div>

<script>
// API Configuration - Points to ENSGrading API deployed on Railway
const API_BASE_URL = 'https://ensgrading-production.up.railway.app';

// Global variables
let uploadedFiles = {
  student: null,
  author: null,
  year: null,
  grades: null,
  excel: null,
  'author-batch': null
};

// =============================================================================
// UI INTERACTION FUNCTIONS
// =============================================================================

// This function is no longer needed as we removed tabs, but keeping it in case other code references it
function switchTab(tabName, clickedButton) {
  // No need for implementation since we only have one tab now
  return;
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
    showStatus(`Error: Could not find label for ${type} file upload`, 'error');
    return;
  }
  
  uploadedFiles[type] = file;
}


// =============================================================================
// FORM AND DATA HANDLING FUNCTIONS
// =============================================================================

// These functions have been removed as we no longer have manual grade input

// Function removed as we no longer have the manual input option

// =============================================================================
// UTILITY FUNCTIONS
// =============================================================================

function showStatus(message, type) {
  const statusDiv = document.getElementById('status-message');
  statusDiv.textContent = message;
  statusDiv.className = `status-message status-${type}`;
  statusDiv.style.display = 'block';
}


// =============================================================================
// TRANSCRIPT GENERATION FUNCTIONS
// =============================================================================

function generateTranscript() {
  try {
    // Check upload mode
    const uploadMode = document.querySelector('input[name="upload-mode"]:checked').value;
    
    if (uploadMode === 'single') {
      handleSingleUploadGeneration();
    } else {
      handleBatchUploadGeneration();
    }
    return;
  } catch (error) {
    showStatus('Error generating transcript: ' + error.message, 'error');
  }
}

async function handleSingleUploadGeneration() {
  // Check if files are uploaded for single mode
  if (!uploadedFiles.student || !uploadedFiles.author || !uploadedFiles.grades) {
    showStatus('Veuillez ajouter tous les fichiers requis (informations étudiant, informations auteur et notes).', 'error');
    return;
  }

  showStatus('Génération du relevé en cours...', 'info');
  
  try {
    // Create FormData object
    const formData = new FormData();
    formData.append('student_info', uploadedFiles.student);
    formData.append('author_info', uploadedFiles.author);
    formData.append('grades', uploadedFiles.grades);
    formData.append('year_info', uploadedFiles.year);

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
    showStatus(`Transcript generated successfully for ${result.student_name}!`, 'success');

  } catch (error) {
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
    
    // Check if rank display is enabled
    const displayRank = document.querySelector('input[name="display-rank"]:checked').value === 'true';
    if (displayRank) {
      formData.append('display_rank', 'true');
    }

    // Call API
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
    showStatus(`Batch processing completed! Generated ${result.generated_count} transcripts.`, 'success');

  } catch (error) {
    showStatus('Error generating batch transcripts: ' + error.message, 'error');
  }
}

// This function has been removed as we no longer have manual input mode

// =============================================================================
// FILE DOWNLOAD FUNCTIONS
// =============================================================================

function downloadPDFFromBase64(base64Data, filename) {
  try {
    if (!base64Data) {
      throw new Error('No PDF data provided');
    }
    
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
    
    showStatus(`PDF download initiated: ${filename} (${Math.round(blob.size/1024)}KB)`, 'success');
    
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
</script>
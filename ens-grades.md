---
layout: default
title: ENS Grades
slug: /ens-grades.html
---

<style>
.ens-grades-content {
  text-align: justify;
}

.ens-grades-content table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
  font-size: 14px;
}

.ens-grades-content table, .ens-grades-content th, .ens-grades-content td {
  border: 1px solid #ddd;
}

.ens-grades-content th, .ens-grades-content td {
  padding: 0.6rem;
  text-align: center;
}

.ens-grades-content th {
  background-color: #f6f8fa;
  font-weight: 300;
}

.download-section {
  text-align: center;
  margin: 30px 0;
}

.download-button {
  background: #3953a5;
  color: white;
  padding: 12px 24px;
  border-radius: 3px;
  text-decoration: none;
  font-weight: 300;
  font-size: 14px;
  transition: background 0.3s;
  display: inline-block;
}

.download-button:hover {
  background: #2c3f82;
  text-decoration: none;
}

.pdf-section {
  margin-top: 30px;
  text-align: center;
}

.pdf-section h2 {
  margin-bottom: 15px;
  font-weight: 300;
  color: #111;
}

.pdf-container {
  margin: 0 auto;
  max-width: 100%;
}

.pdf-container iframe {
  width: 100%;
  height: 80vh;
  border: 1px solid #ddd;
  border-radius: 3px;
}

@media screen and (max-width: 500px) {
  .pdf-container iframe {
    height: 60vh;
  }
  
  .download-button {
    padding: 10px 20px;
    font-size: 13px;
  }
}
</style>

<div class="ens-grades-content">
  <h1>Convertisseur de notes ENS Rennes vers le système de notation international</h1>
  
  <h2>Motivation</h2>
  <p>Afin de répondre aux critères de notation à l'international (e.g., des universités américaines, suisses, allemandes...), il est fortement bénéfique d'avoir un système de notation connu des universités étrangères à la France.</p>

  <p>Exemple d'université étrangère imposant des critères spécifiques sur les notes :</p>
  <p><u>À l'Univeristé British Columbia :</u> <a href="https://www.grad.ubc.ca/prospective-students/graduate-degree-programs/phd-computer-science" target="_blank">PhD in Computer Science</a></p>
  <p>La motivation est principalement de proposer des relevés de notes équivalents qui permettraient de ne <strong>pas pénaliser</strong> les étudiants et élèves du département informatique de l'ENS Rennes dans leur candidature à l'international : le système de notation de l'ENS Rennes – et en particulier des grandes écoles françaises – est connu, en France, comme plus sévère mais ce n'est pas forcément le cas des universités étrangères.</p>
  <p>De plus, le système de notation français (notes sur 20, passage à 10 et difficulté d'obtenir de hautes notes) n'est en général pas connu des universités étrangères : pour maximiser l'égalité et les chances des étudiants et élèves de l'ENS Rennes dans leur candidature, faciliter la lecture et compréhension avec un système de notation commun et adapté est bénéfique.</p>
  <p>Enfin, d'autres écoles comme l'INSA Lyon ou d'autres ENS comme l'ENS Ulm proposent déjà des relevés de notes adaptés à l'international en soulignant la difficulté du cursus avec un barème adapté. Il est alors d'autant plus bénéfique de proposer un système similaire pour mettre sur un pied d'égalité les étudiants et élèves de l'ENS Rennes avec les autres écoles.</p>
  <p>Des exemples concrets où un tel système est sincèrement bénéfique aux étudiants et élèves sont les thèses de doctorat. Cela peut aussi concerner les admissions dans d'autres universités ou pour des stages.</p>


  <h2>Conversion des notes</h2>
  <p>Chaque école qui propose un tel système a un barème adapté à la difficulté du cursus de son école ou celui d'un département – notamment, pour les ENS. Cela peut être rendu public dans une grille d'équivalences de notes ou être effectué en interne (où la notation est donnée implicitement).</p>
  <p><u>À l'INSA Lyon, grille publique :</u> <a href="https://www.insa-lyon.fr/sites/www.insa-lyon.fr/files/tableau_de_conversion_des_notes_0.pdf" target="_blank">Tableau de conversion de notes</a></p>
  <p><u>À l'Université de Caen, grille publique :</u> <a href="https://www.unicaen.fr/wp-content/uploads/2020/10/Grille_Proposition-d-equivalence-notes-Hors-Europe.pdf" target="_blank">Tableau de conversion de notes</a></p>
  <p><u>À l'Université de Paris-Saclay, méthode de conversion en fonction de la note et/ou du rang :</u> <a href="https://www.universite-paris-saclay.fr/sites/default/files/2022-03/grades_transcript_m1_ies_ead_0.pdf" target="_blank">Notice de conversion de notes</a></p>
  <p><u>À l'Université de Panthéon Sorbonne, grille publique :</u> <a href="https://international.pantheonsorbonne.fr/sites/default/files/inline-files/Tableau_conversion_notes.pdf" target="_blank">Tableau de conversion de notes</a></p>
  <p><u>À l'ENS Ulm, exemple d'un élève au DIT :</u> <a href="https://www.normalesup.org/~rouvroy/ressources/L3_Grades.pdf" target="_blank">Relevé de notes</a></p>


  <table>
    <tr><th>Note française (sur 20)</th><th>GPA</th><th>Lettre</th></tr>
    <tr><td>≥ 14</td><td>4.0</td><td>A</td></tr>
    <tr><td>13 – 13.9</td><td>3.7</td><td>B+</td></tr>
    <tr><td>12 – 12.9</td><td>3.33</td><td>B</td></tr>
    <tr><td>11 – 11.9</td><td>3.0</td><td>B-</td></tr>
    <tr><td>10.5 – 10.9</td><td>2.7</td><td>C+</td></tr>
    <tr><td>10.1 – 10.4</td><td>2.33</td><td>C</td></tr>
    <tr><td>9 – 10.0</td><td>2.0</td><td>C-</td></tr>
    <tr><td>7 – 8.9</td><td>1.7</td><td>D</td></tr>
    <tr><td>&lt; 7</td><td>0.0</td><td>F</td></tr>
    <tr><td>N/A</td><td>N/A</td><td>N/A</td></tr>
  </table>

  <p>La moyenne est le <strong>GPA cumulatif</strong> : il s'obtient en conversion en calculant la moyenne des GPA de chaque UE (avec en coefficient le nombre d'ECTS associés).</p>

  <h2>Outil</h2>
  <p>L'outil est encore en développement.</p>
  <ol>
    <li>Lecture d'un relevé de notes en PDF-texte (et non image) qui peut être certifié ou non (par la scolarité) : ceci est géré dans le fichier grades.py avec un paramètre dans la fonction <i>read_grades()</i>. Le programme génère dans le dossier config un fichier grades.json qui contient UEs, ECTS et notes.
      <br><i>Si une UE n'a pas été validée, au dépend du fichier certifié ou non, il peut ne pas contenir les ECTS. Il est donc laissé à l'utilisateur le soin de vérifier le fichier config/grades.json avec les bons ECTS.</i></li>
    <br>
    <li>Création d'un relevé de notes équivalent en PDF dans le répertoire local : ceci est géré dans le fichier main.py à exécuter.</li>
  </ol>

  <p>Installer les librairies : <code>pip install -r requirements.txt</code> (testé avec Python 3.13.5)</p>
  <p>Remplir au préalable les informations de l'étudiant dans <code>config/info.yaml</code> et exécuter <code>script.sh</code></p>

  <h2>Accord</h2>
  <p>Afin de compléter l'outil, nous avons besoin de l'accord et de la collaboration du directeur du département informatique. Sur les points suivants :</p>
  <ul>
    <li><b>Validation de la grille de notes proposée.</b></li>
    <li><b>Validation de l'outil</b> : utilisation ou intégration dans un système déjà existant.</li>
    <li><b>Approbation du PDF généré</b> : contenu, ajout de signature, tampon, etc.</li>
    <li><b>Envoi aux universités étrangères</b> : au besoin, dans le cas de certaines universités en Amérique ou en Europe, il est demandé d'envoyer les mêmes bulletins dans une lettre officielle à l'université étrangère.</li>
  </ul>
</div>

<div class="download-section">
  <a href="/convertisseur/source_code.zip" class="download-button" download>📥 Télécharger le code source</a>
</div>

<div class="pdf-section">
  <h2>Exemple de relevé international généré</h2>
  <div class="pdf-container">
    <iframe src="/convertisseur/exemple.pdf"></iframe>
  </div>
</div>

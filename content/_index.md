---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

sections:
  - block: about.biography
    id: about
    content:
      title: Biography
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
  - block: skills
    content:
      title: Skills
      text: ''
      # Choose a user to display skills from (a folder name within `content/authors/`)
      username: admin
    design:
      columns: '1'
  - block: experience
    id: experience
    content:
      title: Experience
      # Date format for experience
      #   Refer to https://docs.hugoblox.com/customization/#date-format
      date_format: Jan 2006
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      items:
        - title: M1 Research Project
          company: Inria (EMPENN team)
          company_url: 'https://team.inria.fr/empenn/'
          company_logo: inria-logo
          location: Rennes, France
          date_start: '2023-10-10'
          date_end: '2024-05-05'
          description: Year-long research project under [Camille Maumet](http://camillemaumet.com/) & [Fanny Dégeilh's](https://team.inria.fr/empenn/team-members/fanny-degeilh/) supervision as part of my M1 at ENS Rennes (dedicating ~8h a week to research). Working on reproducibility in pediatric brain imaging and the impact of inter scanner harmonization on cortical thickness statistics.  
        - title: Research Internship
          company: Inria (EMPENN team)
          company_url: 'https://team.inria.fr/empenn/'
          company_logo: inria-logo
          location: Rennes, France
          date_start: '2023-05-05'
          date_end: '2023-07-07'
          description: Summer internship under [Fanny Dégeilh's](https://team.inria.fr/empenn/team-members/fanny-degeilh/) supervision. I listed different brain atlases for infants (0-5 yo) and tested several brain segmentation tools on HCP Baby data.
        - title: Professor of Semiconductor Physics
          company: University X
          company_url: 'https://team.inria.fr/genscale/'
          company_logo: inria-logo
          location: Rennes, France
          date_start: '2022-05-05'
          date_end: '2022-07-07'
          description: Summer internship under [Claire Lemaitre's](http://people.rennes.inria.fr/Claire.Lemaitre/index.php) supervision. I worked on developping a tool for genotyping structural variants using linked-reads in Python.
    design:
      columns: '2'
  - block: markdown
    id: contact
    content:
      title: Contact
      subtitle:
      text: **Mail** : emma [dot] redor [at] ens-rennes [dot] fr
---

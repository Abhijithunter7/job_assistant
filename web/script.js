document.addEventListener('DOMContentLoaded', () => {
  const searchBtn = document.getElementById('search-btn');
  const jobListings = document.getElementById('job-listings');
  const matchScores = document.getElementById('match-scores');

  // Mock CV data (replace with actual CV processing in a real app)
  const cvData = {
    skills: ['python', 'java', 'javascript', 'sql', 'react', 'node', 'aws'],
    experiences: ['years', 'project', 'lead', 'developed'],
    keywords: ['tensorflow', 'machine', 'learning', 'data', 'science']
  };

  searchBtn.addEventListener('click', () => {
      const jobTitle = document.getElementById('job-title').value.toLowerCase();
      const location = document.getElementById('location').value.toLowerCase();
      const company = document.getElementById('company').value.toLowerCase();
      const skills = document.getElementById('skills').value.toLowerCase().split(',').map(s => s.trim());
      const keywords = document.getElementById('keywords').value.toLowerCase().split(',').map(k => k.trim());
      const isRemote = document.getElementById('remote').checked;

      let apiUrl = 'http://127.0.0.1:8000/jobs?';
      if (jobTitle) apiUrl += `job_title=${encodeURIComponent(jobTitle)}&`;
      if (location) apiUrl += `location=${encodeURIComponent(location)}&`;
      if (company) apiUrl += `company=${encodeURIComponent(company)}&`;
      if (skills.length > 0 && skills[0] !== '') apiUrl += `skills=${encodeURIComponent(skills.join(','))}&`;
      if (keywords.length > 0 && keywords[0] !== '') apiUrl += `keywords=${encodeURIComponent(keywords.join(','))}&`;
      apiUrl += `remote=${isRemote}`;

      fetch(apiUrl)
          .then(response => {
              if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
              return response.json();
          })
          .then(jobs => {
              jobListings.innerHTML = '';
              matchScores.innerHTML = '';

              jobs.forEach((job, index) => {
                  // Simulate similarity scoring (adjust as needed)
                  let score = 0;
                  if (jobTitle && job.title.toLowerCase().includes(jobTitle)) score += 20;
                  if (location && job.location.toLowerCase().includes(location)) score += 15;
                  if (company && job.company.toLowerCase().includes(company)) score += 15;
                  if (skills.length > 0 && skills.every(skill => (job.description.toLowerCase() + job.title.toLowerCase()).includes(skill))) score += 25;
                  if (keywords.length > 0 && keywords.every(keyword => (job.description.toLowerCase() + job.title.toLowerCase()).includes(keyword))) score += 25;

                  const adjustedScore = Math.min(score * 1.5, 100);

                  const jobDiv = document.createElement('div');
                  jobDiv.className = 'p-4 border rounded-lg mb-4';
                  jobDiv.innerHTML = `
                      <h3 class="font-semibold">${job.company}</h3>
                      <p class="text-sm text-gray-600">${job.title}</p>
                      <p class="text-sm text-gray-500">${job.description}</p>
                      <button class="mt-2 bg-gray-200 text-black px-4 py-2 rounded">Apply</button>
                  `;
                  jobListings.appendChild(jobDiv);

                  const scoreDiv = document.createElement('div');
                  scoreDiv.innerHTML = `
                      <p class="text-sm">${job.title}</p>
                      <div class="progress-bar">
                          <div class="progress" style="width: ${adjustedScore}%"></div>
                      </div>
                      <p class="text-right text-sm">${Math.round(adjustedScore)}%</p>
                  `;
                  matchScores.appendChild(scoreDiv);
              });
          })
          .catch(error => {
              console.error('Error fetching jobs:', error);
              jobListings.innerHTML = '<p class="text-red-500">Failed to load jobs. Check the API.</p>';
          });
  });

  searchBtn.click();
});
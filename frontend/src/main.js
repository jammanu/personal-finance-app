const API_BASE = 'http://localhost:8000';

function renderApp() {
  document.getElementById('app').innerHTML = `
<h1>Personal Finance Dashboard</h1>
<div>
    <h2>Create Account</h2>
    <input id="accountName" placeholder="Account Name" />
    <input id="accountBalance" type="number" placeholder="Initial Balance" />
    <button id="createAccount">Create Account</button>
</div>
<div>
    <h2>Summary</h2>
    <button id="loadSummary">Load Summary</button>
    <pre id="summary"></pre>
</div>
<div>
    <h2>Suggestions</h2>
    <button id="loadSuggestions">Load Suggestions</button>
    <pre id="suggestions"></pre>
</div>
  `;
  // attach event handlers
  document.getElementById('loadSummary').onclick = fetchSummary;
  document.getElementById('loadSuggestions').onclick = fetchSuggestions;
  document.getElementById('createAccount').onclick = createAccount;
}

async function fetchSummary() {
  const res = await fetch(`${API_BASE}/summary`);
  const data = await res.json();
  document.getElementById('summary').innerText = JSON.stringify(data, null, 2);
}

async function fetchSuggestions() {
  const res = await fetch(`${API_BASE}/suggestions`);
  const data = await res.json();
  document.getElementById('suggestions').innerText = data.suggestions.join('\n');
}

async function createAccount() {
  const name = document.getElementById('accountName').value;
  const balance = parseFloat(document.getElementById('accountBalance').value) || 0;
  await fetch(`${API_BASE}/accounts`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, balance })
  });
  await fetchSummary();
}

// initialize app after DOM load
window.addEventListener('DOMContentLoaded', () => {
  renderApp();
});

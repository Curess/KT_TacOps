const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

// Connect to SQLite database
const db = new sqlite3.Database(':memory:', (err) => {
  if (err) {
    return console.error(err.message);
  }
  console.log('Connected to the in-memory SQLite database.');
});

// Middleware to parse request bodies
app.use(bodyParser.json());
app.use(express.static('public')); // Serve static files

// Initialize database structure
db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS factions (
    faction_id INTEGER PRIMARY KEY,
    faction_name TEXT NOT NULL UNIQUE
  )`);

  db.run(`CREATE TABLE IF NOT EXISTS subfactions (
    subfaction_id INTEGER PRIMARY KEY,
    faction_id INTEGER NOT NULL,
    subfaction_name TEXT NOT NULL,
    FOREIGN KEY (faction_id) REFERENCES factions (faction_id)
  )`);

  db.run(`CREATE TABLE IF NOT EXISTS kill_teams (
    killteam_id INTEGER PRIMARY KEY,
    subfaction_id INTEGER NOT NULL,
    killteam_name TEXT NOT NULL,
    FOREIGN KEY (subfaction_id) REFERENCES subfactions (subfaction_id)
  )`);

  db.run(`CREATE TABLE IF NOT EXISTS tacops (
    tacop_id INTEGER PRIMARY KEY,
    archetype TEXT,
    unique_team BOOLEAN,
    team_id INTEGER,
    description TEXT,
    FOREIGN KEY (team_id) REFERENCES kill_teams (killteam_id)
  )`);

  // Insert placeholder data for factions
  const factions = ['Imperium', 'Chaos', 'Aeldari', 'Xenos'];
  const placeholders = factions.map(() => '(?)').join(',');
  const sql = `INSERT INTO factions (faction_name) VALUES ${placeholders}`;
  db.run(sql, factions);
});

// Define API routes here

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

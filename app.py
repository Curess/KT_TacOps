from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Import models from DB_Creator.py (adjust path if needed)
from DB_Creator import db, KillTeam, Archetype, TacOp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kt_database.db'  # Replace with your database path
db.init_app(app)

# Optional: Create database tables if not already existing
with app.app_context():
    db.create_all()

# Route for viewing all Kill Teams (replace with your own functionality)
@app.route('/')
def list_kill_teams():
    # Fetch all Kill Teams from database
    kill_teams = KillTeam.query.all()

    # Render a template with data (create list_kill_teams.html with your design)
    return render_template('list_kill_teams.html', kill_teams=kill_teams)

# Example route for adding a new Kill Team (replace with your own logic)
@app.route('/add_kill_team', methods=['GET', 'POST']):
    if request.method == 'GET':
        # Show a form for adding a new Kill Team
        return render_template('add_kill_team.html')
    elif request.method == 'POST':
        # Extract data from the form and create a new Kill Team object
        name = request.form['name']
        # (Add logic to handle other form fields, e.g., selecting Archetypes)

        # Create a new Kill Team object and save to database
        new_kill_team = KillTeam(name=name)
        db.session.add(new_kill_team)
        db.session.commit()

        # Redirect to the list of Kill Teams after adding
        return redirect('/')

# (Add more routes for your desired functionalities)

if __name__ == '__main__':
    app.run(debug=True)

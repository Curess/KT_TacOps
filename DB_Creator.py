from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class KillTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    archetypes = db.relationship('Archetype', secondary='kt_archetype', backref='kill_teams')

class Archetype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    tac_ops = db.relationship('TacOp', backref='archetype')

class TacOp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.Text)
    is_unique = db.Column(db.Boolean, default=False)
    archetype_id = db.Column(db.Integer, db.ForeignKey('archetype.id'), nullable=True)

kt_archetype = db.Table('kt_archetype',
    db.Column('kill_team_id', db.Integer, db.ForeignKey('kill_team.id')),
    db.Column('archetype_id', db.Integer, db.ForeignKey('archetype.id'))
)

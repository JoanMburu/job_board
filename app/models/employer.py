from app import db
import bcrypt
from datetime import datetime

class Employer(db.Model):
    __tablename__ = 'employers'
    
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    about = db.Column(db.Text, nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    
    # Timestamp fields
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Set on creation
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Updated when record is modified
    
    # Relationship with jobs
    jobs = db.relationship('Job', backref='employer', lazy=True)
    

    def __init__(self, company_name, email, phone_number, about, password):
        self.company_name = company_name
        self.email = email
        self.phone_number = phone_number
        self.about = about
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
 
        
 
    def to_dict(self):
        return {
            "id": self.id,
            "company_name": self.company_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "about": self.about,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            # Not returning password_hash for security reasons
            "jobs": [job.to_dict() for job in self.jobs] if self.jobs else []
        }
         
         
    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))   
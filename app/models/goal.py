from app import db


class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    tasks = db.relationship("Task", back_populates="goal", lazy=True)
    
    def get_dict(self):
        return {
            "goal_id": self.goal_id,
            "title": self.title
        }
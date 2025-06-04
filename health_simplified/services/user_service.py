from health_simplified.db.session import get_db
from health_simplified.models.user import User
from sqlalchemy.orm import Session

class UserService:
    def create_user(self, name: str):
        db: Session = next(get_db())
        user = User(name=name)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def list_users(self):
        db: Session = next(get_db())
        return db.query(User).all()

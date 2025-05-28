# food_tracking.py
import typer 
from datetime import datetime
from models import Session, User, FoodEntry
from typing import Optional


app = typer.Typer()

@app.command()
def add(user: str, food:str, calories:int, date:Optional[str] = None):
    """Add a food entry"""
    session = Session()
    try:
        user_obj = session.query(User).filter_by(name=user).first()
        if not user_obj:
            typer.echo(f"User '{user}' not found!", err=True)
            return
        
        entry_date = datetime.strptime(date, "%y-%m-%d").date() 
        if date else datetime.utcnow().date()
        entry = FoodEntry(
            user_id=user_obj.id,
            food=food,
            calories=calories,
            date=entry_date
            
        )         
        session.add(entry)
        session.commit()
        typer.echo(f"Added {food} ({calories} cal) to {user}'s log on {entry_date}")
    except Exception as e:
           session.rollback()
           typer.echo(f"Error adding entry: {str()}", err=True)
       
    finally:
          session.close()
          
    @app.command()
    def list(user: Optional[str] = None, date: Optional[str] = None):
        """List food entries with optional filter"""
    session = Session()
    try:
        query = session.query(FoodEntry)
        
        if user:
            user_obj = session.query(User).filter_by(name=user).first()
            if user_obj:
                query = query.filter_by(user_id=user_obj.id)
            else:
                typer.echo(f"User '{user}' not found!", err=True)
                return
            if date:
                filter_date = datetime.strptime(date, "%Y-%m-%d").date()
                query = query.filter_by(date=filter_date)
            
            entries = query.all()
            
            if not entries:
                typer.echo("No entries found matching criteria")
                return
            for entry in entries:
                user_name = session.query(User).get(entry.user_id).name
                typer.echo(f"{entry_id}: {user_name} ate {entry.food} ({entry.calories} cal) on (entry.date)")
    finally:
                session.close()      
        
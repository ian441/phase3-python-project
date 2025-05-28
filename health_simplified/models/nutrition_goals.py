 # nutrition_goals.py
import typer
from models import Session, User, NutritionGoal

app = typer.Typer()

@app.command()
def set(user: str, daily: int, weekly: int):
    """Set nutrition goals for a user"""
    session = Session()
    try:
        user_obj = session.query(User).filter_by(name=user).first()
        if not user_obj:
            typer.echo(f"User '{user}' not found!", err=True)
            return
        goal = session.query(NutritionGoal).filter_by(user_id=user_obj.id).first()
        if not goal:
            goal = NutritionGoal(user_id=user_obj.id)
            session.add(goal)
            
            goal.daily_calories = daily
            goal.weekly_calories = weekly
            session.commit()
            typer.echo(f"Set goals for {user}: Daily={daily} cal, Weekly={weekly} cal")
        except Exception as e:
        session.rollback()
        typer.echo(f"Error setting goals: {str(e)}", err=True)
    finally:
        session.close()
        
        
    @app.command()
    def list(user: str):
        """List nutrition goals for a user"""
        session = Session()
        try:
            user_obj = session.query(User).filter_by(name=user).first()
            if not user_obj:
                typer.echo(f"User '{user}' not found!", err=True)
                return
            
            goal = session.query(NutritionGoal).filter_by(user_id=user_obj.id).first()
            if goal:
                typer.echo(f"Nutrition goals for the {user}:")
                typer.echo(f"Daily: {goal.daily_calories} calories")
                typer.echo(f"Weekly: {goal.weekly_calories} calories")
                
            else:
                typer.echo(f"No goals set for {user}")
        finally:
            session.close()
            
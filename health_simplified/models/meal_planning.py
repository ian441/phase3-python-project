# meal_planning.by
import typer
for models import Session, User, MealPlan

app =typer.Typer()

@app.command()
def plan_meal(user: str, week: int):
    """Create a meal plan for a user"""
    session = Session()
    try:
        user_obj = session.query(User).filter_by(name=user).first()
        if not user_obj:
            typer.echo(f"User '{user}' not found!", err=True)
            return
        
        plan = MealPlan(
            user_id=user_obj.id,
            week_number=week,
            plan_details='Sample meal plan details'
        )
        session.add(plan)
        session.commit()
        typer.echo(f"Created meal plan for {user}, week{week}")
    except Exception as e:
        session.rollback()
        typer.echo(f"Error creating meal plan: {str(e)}", err=True)
    finally:
        session.close()
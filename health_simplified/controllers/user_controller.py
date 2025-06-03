import typer
from health_simplified.services.user_service import UserService
from health_simplified.services.goal_service import GoalService
from health_simplified.services.meal_plan_service import MealPlanService
from health_simplified.services.food_service import FoodService

user_cli = typer.Typer()
user_service = UserService()
goal_service = GoalService()
meal_plan_service = MealPlanService()
food_service = FoodService()

@user_cli.command("create")
def create_user(name: str):
    """Create a new user."""
    user_service.create_user(name)
    typer.echo(f"User '{name}' created.")

@user_cli.command("list")
def list_users():
    """List all users."""
    users = user_service.list_users()
    for user in users:
        typer.echo(f"{user.id}: {user.name}")

@user_cli.command("summary")
def user_summary(name: str):
    """Show user info, goals, meal plans, and food entries."""
    typer.echo(f"Summary for {name}:")

    
    try:
        goals = goal_service.list_goals(name)
        typer.echo("\nGoals:")
        for goal in goals:
            typer.echo(f"  Daily: {goal.daily}, Weekly: {goal.weekly}")
    except Exception as e:
        typer.echo("  No goals found.")

    
    try:
        meal_plans = meal_plan_service.list_meal_plans(name)
        typer.echo("\nMeal Plans:")
        for plan in meal_plans:
            typer.echo(f"  Week {plan.week}: {plan.details}")
    except Exception as e:
        typer.echo("  No meal plans found.")

    
    try:
        food_entries = food_service.list_food_entries(name)
        typer.echo("\nFood Entries:")
        for entry in food_entries:
            typer.echo(f"  {entry.food} ({entry.calories} cal) on {entry.date}")
    except Exception as e:
        typer.echo("  No food entries found.")
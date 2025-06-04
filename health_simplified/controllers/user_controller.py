import typer
from health_simplified.services.user_service import UserService
from health_simplified.services.goal_service import GoalService
from health_simplified.services.meal_plan_service import MealPlanService
from health_simplified.services.food_service import FoodService
from tabulate import tabulate

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
    if users:
        table = [[user.id, user.name] for user in users]
        typer.echo(tabulate(table, headers=["ID", "Name"], tablefmt="grid"))
    else:
        typer.echo("No users found.")

@user_cli.command("summary")
def user_summary(name: str):
    """Show user info, goals, meal plans, and food entries."""
    typer.echo(f"\nSummary for {name}:")
    typer.echo("=" * (len(name) + 12) + "\n")

    
    try:
        goals = goal_service.list_goals(name)
        if goals:
            goals_table = [[goal.daily, goal.weekly] for goal in goals]
            typer.echo("Goals:")
            typer.echo(tabulate(goals_table, headers=["Daily Goals", "Weekly Goals"], tablefmt="grid"))
        else:
            typer.echo("No goals found.")
    except Exception as e:
        typer.echo("Error retrieving goals.")

    
    try:
        meal_plans = meal_plan_service.list_meal_plans(name)
        if meal_plans:
            meal_plans_table = [[plan.week, plan.details] for plan in meal_plans]
            typer.echo("\nMeal Plans:")
            typer.echo(tabulate(meal_plans_table, headers=["Week", "Details"], tablefmt="grid"))
        else:
            typer.echo("\nNo meal plans found.")
    except Exception as e:
        typer.echo("\nError retrieving meal plans.")

    
    try:
        food_entries = food_service.list_food_entries(name)
        if food_entries:
            food_table = [[entry.food, entry.calories, entry.date] for entry in food_entries]
            typer.echo("\nFood Entries:")
            typer.echo(tabulate(food_table, headers=["Food", "Calories", "Date"], tablefmt="grid"))
        else:
            typer.echo("\nNo food entries found.")
    except Exception as e:
        typer.echo("\nError retrieving food entries.")
import typer
from health_simplified.services.meal_plan_service import MealPlanService

meal_plan_cli = typer.Typer()
meal_plan_service = MealPlanService()

@meal_plan_cli.command("create")
def create_meal_plan(user: str, week: int):
    """Create a meal plan for a user for a specific week."""
    meal_plan_service.create_meal_plan(user, week)
    typer.echo(f"Meal plan for {user} for week {week} created.")

@meal_plan_cli.command("list")
def list_meal_plans(user: str):
    """List meal plans for a user."""
    meal_plans = meal_plan_service.list_meal_plans(user)
    for plan in meal_plans:
        typer.echo(f"Meal Plan ID {plan.id} for {user}: {plan.details}")
@meal_plan_cli.command("delete")
def delete_meal_plan(id: int):
    """Delete a meal plan by ID."""
    meal_plan_service.delete_meal_plan(id)
    typer.echo(f"Deleted meal plan ID {id}.")

@meal_plan_cli.command("update")
def update_meal_plan(id: int, details: str = None, week: int = None):
    """Update a meal plan's details or week."""
    meal_plan_service.update_meal_plan(id, details, week)
    typer.echo(f"Updated meal plan ID {id}.")
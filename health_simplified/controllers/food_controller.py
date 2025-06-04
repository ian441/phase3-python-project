import typer
from health_simplified.services.food_service import  FoodService

food_cli = typer.Typer()
food_service = FoodService()

@food_cli.command("add")
def add_food_entry(user: str, food: str, calories: int, date: str):
    """Add a food entry for a user."""
    food_service.add_food_entry(user, food, calories, date)
    typer.echo(f"Added entry: {food} ({calories} calories) for {user} on {date}.")

@food_cli.command("list")
def list_food_entries(user: str = None, date: str = None):
    """List food entries for a user on a specific date."""
    entries = food_service.list_food_entries(user, date)
    for entry in entries:
        typer.echo(f"{entry.id}: {entry.food} ({entry.calories} calories) on {entry.date}")

@food_cli.command("update")
def update_food_entry(id: int, food: str = None, calories: int = None):
    """Update a food entry."""
    food_service.update_food_entry(id, food, calories)
    typer.echo(f"Updated entry ID {id}.")

@food_cli.command("delete")
def delete_food_entry(id: int):
    """Delete a food entry."""
    food_service.delete_food_entry(id)
    typer.echo(f"Deleted entry ID {id}.")

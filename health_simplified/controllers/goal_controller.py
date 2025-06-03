import typer
from health_simplified.services.goal_service import GoalService

goal_cli = typer.Typer()
goal_service = GoalService()

@goal_cli.command("set")
def set_goal(user: str, daily: int, weekly: int):
    """Set daily and weekly calorie goals for a user."""
    goal_service.set_goal(user, daily, weekly)
    typer.echo(f"Set goals for {user}: Daily {daily}, Weekly {weekly}.")

@goal_cli.command("list")
def list_goals(user: str):
    """List goals for a user."""
    goals = goal_service.list_goals(user)
    for goal in goals:
        typer.echo(f"Goal ID {goal.id}: Daily {goal.daily}, Weekly {goal.weekly}")

import typer
from .user_controller import user_cli
from .food_controller import food_cli
from .goal_controller import goal_cli
from .meal_plan_controller import meal_plan_cli

app = typer.Typer()

app.add_typer(user_cli, name="user")
app.add_typer(food_cli, name="food")
app.add_typer(goal_cli, name="goal")
app.add_typer(meal_plan_cli, name="meal-plan")

def cli():
    app()

# user.py
import typer
from models import Session, user
from typing import Optional

app = typer.Typer()

@app.command()
def create(name:str):
    """New user"""
    session = Session()
    try:
        user = user(name=name)
        session.add(user)
        session.commit()
        typer.echo(f"User '{name}' created successfully!")
    except Exception as e:
        session.rollback()
        typer.echo(f"Error creating user: {str(e)}", error=True )
    finally:
        session.close()
        
    @app.command
    def list():
        """List all users"""
        session = Session()
    try:
        users = session.query(user).all()
        if not users:
            typer.echo("No users found")
            return
        
        for user in users:
            typer.echo(f"{user.id}: {user.name}")
    finally:   
    session.close()
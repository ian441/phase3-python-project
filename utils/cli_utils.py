# import typer
# from typing import List, Dict, Any, Optional
# from datetime import datetime, date
# from rich.console import Console
# from rich.table import Table
# from rich import box
# from functools import wraps
# from sqlalchemy.exc import SQLAlchemyError

# console = Console()

# def display_table(
#     title: str,
#     columns: List[str],
#     rows: List[Dict[str, Any]],
#     sort_by: Optional[str] = None,
#     highlight_condition: Optional[callable] = None
# ) -> None:
#     """
#     Display tabular data in a formatted table with optional sorting and highlighting.
    
#         """
#     table = Table(title=title, box=box.ROUNDED, highlight=True)
    
#     for col in columns:
#         table.add_column(col, style="cyan")
    
#     if sort_by and sort_by in columns:
#         reverse = sort_by.startswith('-')
#         sort_key = sort_by.lstrip('-')
#         rows = sorted(rows, key=lambda x: x.get(sort_key, ""), reverse=reverse)
    
#     for row in rows:
#         row_data = [str(row.get(col, "")) for col in columns]
#         style = "bold yellow" if highlight_condition and highlight_condition(row) else None
#         table.add_row(*row_data, style=style)
    
#     console.print(table)

# def format_date(input_date: str, future_allowed: bool = False) -> date:
#     """
#     Parse and validate date from various string formats.
    
#     """
#     formats = [
#         "%Y-%m-%d"  
        
#     ]
    
#     for fmt in formats:
#         try:
#             parsed_date = datetime.strptime(input_date, fmt).date()
#             if not future_allowed and parsed_date > date.today():
#                 raise typer.BadParameter("Date cannot be in the future")
#             return parsed_date
#         except ValueError:
#             continue
    
#     raise typer.BadParameter(
#         f"Invalid date format: {input_date}. Try YYYY-MM-DD, MM/DD/YYYY, or DD-MM-YYYY"
#     )

# def prompt_confirm(
#     message: str,
#     default: bool = False,
#     abort: bool = False,
#     warning: bool = False
# ) -> bool:
#     """
#     Prompt user for confirmation with customizable options.
    
#     """
#     style = "yellow" if warning else None
#     return typer.confirm(
#         typer.style(message, fg=style),
#         default=default,
#         abort=abort
#     )

# def handle_db_errors(func):
#     """
#     Decorator to handle database operations with proper error reporting.
#     """
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except SQLAlchemyError as e:
#             typer.echo(f" Database error: {str(e)}", err=True)
#             raise typer.Exit(1)
#         except Exception as e:
#             typer.echo(f" Unexpected error: {str(e)}", err=True)
#             raise typer.Exit(1)
#     return wrapper

# def progress_spinner(description: str = "Processing..."):
#     """
#     Context manager for displaying a progress spinner.
#     """
#     return console.status(f"[bold green]{description}")

# def print_success(message: str):
#     """Print success message with green styling."""
#     console.print(f"[bold green]✓ {message}")

# def print_warning(message: str):
#     """Print warning message with yellow styling."""
#     console.print(f"[bold yellow]⚠ {message}")

# def print_error(message: str):
#     """Print error message with red styling."""
#     console.print(f"[bold red]✗ {message}")
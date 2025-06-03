# from datetime import date
# from typing import Optional, Tuple
# import re

# class ValidationError(ValueError):
#     """Custom validation error with formatted messages."""
#     def __init__(self, field: str, message: str):
#         super().__init__(f"Invalid {field}: {message}")
#         self.field = field
#         self.message = message

# def validate_text(
#     value: str,
#     field_name: str,
#     min_len: int = 1,
#     max_len: int = 100,
#     regex: Optional[str] = None
# ) -> str:
#     """
#     Validate text input with length and optional regex constraints.
    
#     """
#     value = value.strip()
#     if not value:
#         raise ValidationError(field_name, "cannot be empty")
#     if len(value) < min_len:
#         raise ValidationError(field_name, f"must be at least {min_len} characters")
#     if len(value) > max_len:
#         raise ValidationError(field_name, f"cannot exceed {max_len} characters")
#     if regex and not re.match(regex, value):
#         raise ValidationError(field_name, "contains invalid characters")
#     return value

# def validate_user_name(name: str) -> str:
#     """Validate username with specific rules."""
#     return validate_text(
#         name,
#         "name",
#         min_len=2,
#         max_len=50,
#         regex=r"^[a-zA-Z][a-zA-Z0-9 .'-]*$"
#     )

# def validate_calories(calories: int, max_value: int = 10000) -> int:
#     """
#     Validate calorie values.
    
#     """
#     if not isinstance(calories, int):
#         raise ValidationError("calories", "must be a whole number")
#     if calories <= 0:
#         raise ValidationError("calories", "must be positive")
#     if calories > max_value:
#         raise ValidationError("calories", f"cannot exceed {max_value}")
#     return calories

# def validate_date_range(
#     start_date: date,
#     end_date: date,
#     allow_future: bool = False
# ) -> Tuple[date, date]:
#     """
#     Validate date range constraints.
    
#     """
#     if not allow_future:
#         today = date.today()
#         if start_date > today or end_date > today:
#             raise ValidationError("date", "cannot be in the future")
#     if start_date > end_date:
#         raise ValidationError("date range", "start date must be before end date")
#     return start_date, end_date

# def validate_week_number(week: int) -> int:
#     """
#     Validate week number (1-52).
    
#     """
#     if not 1 <= week <= 52:
#         raise ValidationError("week number", "must be between 1 and 52")
#     return week

# def validate_meal_plan_details(details: str) -> str:
#     """
#     Validate meal plan description text.
    
#     """
#     return validate_text(
#         details,
#         "meal plan details",
#         min_len=10,
#         max_len=2000
#     )

# def validate_goals(
#     daily: int,
#     weekly: int,
#     min_daily: int = 1000,
#     max_daily: int = 5000
# ) -> Tuple[int, int]:
#     """
#     Validate nutrition goal constraints.
    
#     """
#     daily = validate_calories(daily, max_daily)
#     weekly = validate_calories(weekly)
    
#     if daily < min_daily:
#         raise ValidationError("daily goal", f"must be at least {min_daily}")
#     if weekly < daily * 7:
#         raise ValidationError("weekly goal", "must be at least 7x daily goal")
#     if weekly > daily * 8:
#         raise ValidationError("weekly goal", "cannot exceed 8x daily goal")
    
#     return daily, weekly
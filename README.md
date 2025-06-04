# Health Simplified CLI

**Health Simplified** is a Python-based command-line application for managing users, nutrition goals, meal plans, and food entries. It is designed to help users track their dietary habits and goals in a simple, structured way.

---

## Features

- **User Management:** Create and list users.
- **Nutrition Goals:** Set and list daily/weekly calorie goals for each user.
- **Meal Plans:** Create, list, update, and delete meal plans per user.
- **Food Entries:** Add, list, update, and delete food entries for users.
- **Summary View:** Display a user's goals, meal plans, and food entries in a table format.

---

## Installation

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd phase3-python-project
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Initialize the database:**
   ```sh
   python init_db.py
   ```

---

## Usage

All commands use the CLI entry point:

```sh
python -m health_simplified.main <resource> <command> [OPTIONS]
```

### User Commands

- **Create a user:**
  ```sh
  python -m health_simplified.main user create --name "John Doe"
  ```

- **List users:**
  ```sh
  python -m health_simplified.main user list
  ```

- **Show user summary:**
  ```sh
  python -m health_simplified.main user summary --name "John Doe"
  ```

### Goal Commands

- **Set goals:**
  ```sh
  python -m health_simplified.main goal set --user "John Doe" --daily 2000 --weekly 14000
  ```

- **List goals:**
  ```sh
  python -m health_simplified.main goal list --user "John Doe"
  ```

### Meal Plan Commands

- **Create a meal plan:**
  ```sh
  python -m health_simplified.main meal-plan create --user "John Doe" --week 1
  ```

- **List meal plans:**
  ```sh
  python -m health_simplified.main meal-plan list --user "John Doe"
  ```

- **Update a meal plan:**
  ```sh
  python -m health_simplified.main meal-plan update <id> --details "New details" --week 2
  ```

- **Delete a meal plan:**
  ```sh
  python -m health_simplified.main meal-plan delete <id>
  ```

### Food Entry Commands

- **Add a food entry:**
  ```sh
  python -m health_simplified.main food add --user "John Doe" --food "Chicken Salad" --calories 350 --date "2023-10-01"
  ```

- **List food entries:**
  ```sh
  python -m health_simplified.main food list --user "John Doe"
  ```

- **Update a food entry:**
  ```sh
  python -m health_simplified.main food update <id> --food "New Food" --calories 400
  ```

- **Delete a food entry:**
  ```sh
  python -m health_simplified.main food delete <id>
  ```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

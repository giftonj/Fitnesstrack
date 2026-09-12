# Fitnesstrack - Fitness & Nutrition Tracker

![Python](https://img.shields.io/badge/python-3.12-blue)
![Django](https://img.shields.io/badge/django-4.2+-green)
![Vercel](https://img.shields.io/badge/deployed%20on-vercel-purple)

A comprehensive fitness tracking application that allows users to log their daily workouts, track nutrition intake, and manage their fitness journey with a secure login system.

## 🚀 Features

- **Workout Tracking**: Log exercises, track duration, sets, reps, and intensity
- **Nutrition Logging**: Record meals, track calories, macronutrients, and dietary habits
- **Progress Visualization**: View historical data and track improvements over time
- **Secure Authentication**: User registration, login, and profile management
- **Responsive Design**: Works on all devices with a clean, intuitive interface

## 📂 Project Structure

```
fitnesstrack/
├── .github/
│   └── workflows/          # GitHub Actions workflows
├── fitnesstrack/           # Main Django project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Configuration settings
│   ├── urls.py             # Main URL routing
│   └── wsgi.py             # WSGI configuration
├── nutrition/              # Nutrition tracking app
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/         # Database migrations
│   ├── models.py           # Data models
│   ├── templates/
│   │   └── nutrition/      # Template files
│   ├── tests.py
│   ├── urls.py             # App-specific URLs
│   └── views.py            # View functions
├── workouts/               # Workout tracking app
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   └── workouts/       # Template files
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── login/                  # Authentication app
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── templates/
│   │   └── login/          # Template files
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
├── vercel.json             # Vercel deployment configuration
└── README.md               # Project documentation
```

## 🔧 Technical Requirements

### Prerequisites

- Python 3.12+
- Django 4.2+
- PostgreSQL or SQLite (configured in settings.py)
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:giftonj/Fitnesstrack.git
   cd Fitnesstrack
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with your configuration:

   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=postgres://user:password@localhost:5432/fitnesstrack
   ```

5. Run migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

## 🌐 Deployment

This project is configured for deployment on Vercel. To deploy:

1. Push your code to a GitHub repository
2. Import the repository to Vercel
3. Vercel will automatically detect the configuration in `vercel.json`

## 📝 Missing Files & Improvements

### Current Structure Analysis:

1. **Good Practices:**
   - Proper Django app structure with separate apps for different functionalities
   - Clear separation of templates, migrations, and models
   - Includes all essential Django files (wsgi.py, asgi.py, manage.py)
   - Good use of GitHub Actions folder structure

2. **Missing Files/Improvements:**
   - **Configuration:**
     - No `.env.example` file for environment variables
     - No `ALLOWED_HOSTS` configuration in settings.py (security risk)
     - No static files configuration (though this might be handled by Vercel)

   - **Security:**
     - No password hashing configuration in settings.py
     - No CSRF protection configuration (though Django handles this by default)

   - **Testing:**
     - No test coverage documentation
     - No example test cases in README

   - **Deployment:**
     - No documentation for database setup in production
     - No configuration for static files in production

3. **Suggested Improvements:**
   - Add `ALLOWED_HOSTS` in production settings
   - Implement proper static files handling (consider using WhiteNoise)
   - Add database backup strategy
   - Implement proper logging configuration
   - Add API documentation (consider Swagger/OpenAPI)
   - Implement proper error handling and logging
   - Add more comprehensive test coverage

## 🛠️ Development Setup

### Running Tests

```bash
python manage.py test
```

### Running Linters

```bash
pip install flake8
flake8 .
```

### Running Formatters

```bash
pip install black
black .
```

## 📊 Database Schema

### Core Models

1. **User Profile** (extends Django's built-in User model)
   - First name, last name, date of birth, profile picture
   - Fitness goals, current weight, height, target weight

2. **Workout Models**
   - Exercise (name, type, muscle group)
   - Workout (date, duration, description)
   - WorkoutEntry (exercise, sets, reps, weight, duration)

3. **Nutrition Models**
   - FoodItem (name, calories, protein, carbs, fats)
   - Meal (date, type, description)
   - NutritionEntry (food item, quantity, calories consumed)

## 📈 Architecture Diagram

```
┌───────────────────────────────────────────────────────────────────────────────┐
│                                Fitnesstrack Application                        │
├─────────────────┬─────────────────┬─────────────────┬─────────────────────────┤
│   Frontend      │   Backend       │   Database      │   Services             │
│  (Templates)    │  (Django)       │  (PostgreSQL)   │                         │
├─────────────────┼─────────────────┼─────────────────┼─────────────────────────┤
│ - HTML/CSS      │ - Models        │ - User          │ - Authentication       │
│ - JavaScript    │ - Views         │ - Workouts      │ - Workout Tracking     │
│ - Bootstrap     │ - Forms         │ - Nutrition     │ - Nutrition Logging    │
│ - AJAX          │ - URLs          │ - Profiles      │ - Progress Analysis    │
└─────────────────┴─────────────────┴─────────────────┴─────────────────────────┘
```

## 🔄 API Endpoints

### Authentication

- `POST /api/login/` - User login
- `POST /api/register/` - User registration
- `POST /api/logout/` - User logout

### Workouts

- `GET /api/workouts/` - List all workouts
- `POST /api/workouts/` - Create new workout
- `GET /api/workouts/<id>/` - Get specific workout
- `PUT /api/workouts/<id>/` - Update workout
- `DELETE /api/workouts/<id>/` - Delete workout

### Nutrition

- `GET /api/nutrition/` - List all nutrition entries
- `POST /api/nutrition/` - Add new nutrition entry
- `GET /api/nutrition/<id>/` - Get specific entry
- `PUT /api/nutrition/<id>/` - Update entry
- `DELETE /api/nutrition/<id>/` - Delete entry

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📢 Contact

Project Link: [https://github.com/giftonj/Fitnesstrack](https://github.com/giftonj/Fitnesstrack)

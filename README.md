# ContentUp

A FastAPI-based dashboard for validating Amazon product listings against expected content values. This tool helps ensure your Amazon product listings maintain high content accuracy across different marketplaces.

## Project Structure

```
contentup/
│
├── app/                    # Application package
│   ├── __init__.py        # Package initializer with version
│   ├── main.py            # FastAPI application creation and configuration
│   ├── core/              # Core application code
│   │   ├── __init__.py
│   │   ├── config.py      # Configuration management
│   │   ├── security.py    # Security utilities
│   │   └── logging.py     # Logging configuration
│   │
│   ├── api/               # API endpoints
│   │   ├── __init__.py
│   │   ├── v1/           # API version 1
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   └── routes.py
│   │   └── deps.py       # Dependency injection
│   │
│   ├── db/               # Database related code
│   │   ├── __init__.py
│   │   ├── session.py    # Database session management
│   │   └── base.py       # Base class for DB models
│   │
│   ├── models/           # SQLAlchemy models
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── schemas/          # Pydantic models
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── services/         # Business logic
│   │   ├── __init__.py
│   │   └── validation.py
│   │
│   ├── utils/            # Utility functions
│   │   ├── __init__.py
│   │   └── helpers.py
│   │
│   └── templates/        # Jinja2 templates
│       └── index.html
│
├── tests/                # Test files
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_api/
│   └── test_services/
│
├── alembic/              # Database migrations
│   ├── versions/
│   └── env.py
│
├── static/              # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── img/
│
├── docs/                # Documentation
│   ├── api/
│   └── guides/
│
├── scripts/             # Utility scripts
│   └── seed_data.py
│
├── .env                 # Environment variables
├── .gitignore
├── alembic.ini         # Alembic configuration
├── pyproject.toml      # Project metadata and dependencies
├── requirements.txt    # Project dependencies
└── README.md
```

## Features

- **Content Validation**: Validate product listings against expected values
- **Scoring System**: Comprehensive scoring for title, bullets, description, images, A+ content, video, and variations
- **Visualization**: Interactive charts showing marketplace performance and criteria scores
- **Detailed Reports**: Downloadable CSV reports with detailed validation results
- **Enhanced Filtering System**: Client-side filtering by marketplace and score ranges with visual feedback and loading indicators
- **JSON to CSV Converter**: Built-in tool for converting JSON data to CSV format with template support
- **Template Management**: Save and reuse field templates for JSON to CSV conversion
- **Responsive UI**: User-friendly interface with real-time feedback during operations

## Requirements

- Python 3.11 or higher
- `uv` package manager (recommended) or pip

## Installation

### Using UV (Recommended)

1. Install UV if you don't have it already:

```bash
# On macOS/Linux
curl -sSf https://install.ultraviolet.dev | sh

# On Windows (using PowerShell)
iwr -useb https://install.ultraviolet.dev/windows | iex
```

2. Clone the repository:

```bash
git clone https://github.com/utilitygods/contentivo.git
cd contentup
```

3. Create a virtual environment and install dependencies:

```bash
# Create and activate a virtual environment
uv venv --python=python3.11 

# On Windows
.\.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate

# Install dependencies
uv pip install -e .
```

### Using Pip (Alternative)

```bash
# Create and activate a virtual environment
python -m venv .venv

# On Windows
.\.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. Place your data files in the `docs` folder:
   - Rainforest API JSON file (e.g., `Collection_Results.json`)
   - Comparison CSV file (e.g., `comparison_value.csv`)
   - Master variation CSV file (e.g., `master_Validation.csv`)

2. Run the application:

```bash
uvicorn app.main:app --reload
```

3. Open your browser and navigate to http://localhost:8000

4. Use the search form to enter:
   - Keyword (e.g., "Pop Socket")
   - ASIN (e.g., "B0CDF5M6TW")
   - Country (e.g., "US")

5. Click "Search & Prepare Data" to filter the data based on your search criteria

6. The validation will run automatically, and you'll see the results displayed in the dashboard

7. Use the filtering controls to narrow down results:
   - Filter by marketplace (US, UK, DE, etc.)
   - Filter by score range (Excellent: 90-100%, Very Good: 80-90%, etc.)
   - The UI will show a loading indicator and update in real-time as filters are applied

8. Use the JSON to CSV Converter:
   - Navigate to the "JSON Converter" page
   - Upload your JSON file
   - Select or create a template for field mapping
   - Choose the fields you want to include in the CSV
   - Click "Export CSV" to download the converted file

## Recent Updates

### Version 1.1.0
- Added JSON to CSV converter with template support
- Improved filtering system with marketplace and score range filters
- Enhanced UI with loading indicators and real-time updates
- Added template management for JSON to CSV conversion
- Improved error handling and user feedback
- Added support for nested JSON data extraction
- Enhanced marketplace detection from various data sources

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Development Guidelines

### Module Responsibilities

- **api/**: Contains all API endpoints organized by version
- **core/**: Core application configuration and setup
- **db/**: Database connection and session management
- **models/**: SQLAlchemy ORM models
- **schemas/**: Pydantic models for request/response validation
- **services/**: Business logic and data processing
- **utils/**: Helper functions and utilities
- **templates/**: Frontend templates (if using server-side rendering)

### Best Practices

1. **Dependency Injection**: Use FastAPI's dependency injection system in `api/deps.py`
2. **Configuration**: Keep configuration in `core/config.py` using pydantic settings
3. **Database**: Use async SQLAlchemy for database operations
4. **Type Hints**: Use type hints throughout the codebase
5. **Documentation**: Document API endpoints using FastAPI's built-in swagger support
6. **Testing**: Write tests for API endpoints and services

## Development

### Setup Environment
```bash
# Create and activate virtual environment
uv venv --python=python3.11
source .venv/bin/activate  # On Unix/macOS
# or
.\.venv\Scripts\activate  # On Windows

# Install dependencies
uv pip install -e .
```

### Run Development Server
```bash
# Method 1: Using Python
python app/main.py

# Method 2: Using uvicorn directly
uvicorn app.main:app --reload

# Method 3: Using development script
./scripts/dev.sh
```

### Access the API
- API Documentation: http://localhost:8000/docs
- Alternative Documentation: http://localhost:8000/redoc
- Health Check: http://localhost:8000/api/v1/health

## Environment Variables
Copy `.env.example` to `.env` and update the values:
```bash
cp .env.example .env
```

## Database
See [DATABASE.md](DATABASE.md) for database setup and management.

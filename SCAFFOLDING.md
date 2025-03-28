# ContentUp Scaffolding Guide

This document explains the capabilities and structure of the ContentUp FastAPI scaffolding.

## Core Features

### 1. API Structure
- **Versioned APIs**: `/api/v1/` structure for API versioning
- **OpenAPI Documentation**: Auto-generated Swagger/ReDoc docs
- **CORS Support**: Configurable CORS middleware
- **Health Checks**: Built-in health check endpoint

### 2. Database Integration
- **SQLAlchemy ORM**: Async SQLAlchemy for database operations
- **Migration System**: Alembic for database migrations
- **Connection Pooling**: Optimized database connection management
- **Base Models**: Timestamp mixin for created_at/updated_at fields

### 3. Environment Management
- **Settings Management**: Pydantic-based settings
- **Environment Variables**: `.env` file support
- **Multiple Environments**: Development/Production configurations
- **UV Package Manager**: Modern Python package management

### 4. Development Tools
- **Hot Reload**: Automatic server restart on code changes
- **Development Scripts**: Convenient development commands
- **Docker Support**: Production-ready Docker setup
- **Nginx Integration**: Reverse proxy with SSL support

## Project Structure

```
contentup/
├── app/
│   ├── api/              # API endpoints
│   │   ├── v1/          # Version 1 API
│   │   └── deps.py      # Dependencies
│   ├── core/            # Core configuration
│   │   └── config.py    # Settings management
│   ├── db/              # Database
│   │   ├── session.py   # DB session
│   │   └── schema/      # SQL schemas
│   ├── models/          # SQLAlchemy models
│   └── services/        # Business logic
├── scripts/             # Utility scripts
└── alembic/             # DB migrations
```

## Available Commands

### Development
```bash
# Start development server
python app/main.py
# or
uvicorn app.main:app --reload
# or
./scripts/dev.sh

# Create database migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head
```

### Production
```bash
# Build Docker image
docker build -t contentup .

# Start production stack
docker-compose up -d
```

## API Endpoints

### Built-in Endpoints
- `GET /api/v1/health`: Health check
- `GET /docs`: Swagger documentation
- `GET /redoc`: ReDoc documentation

### Database Endpoints
- `GET /api/v1/users`: List users
- `GET /api/v1/users/{id}`: Get user
- `POST /api/v1/users`: Create user
- `GET /api/v1/products`: List products

## Configuration Options

### Environment Variables
```env
PROJECT_NAME=ContentUp
VERSION=0.1.0
API_V1_STR=/api/v1
POSTGRES_SERVER=localhost
POSTGRES_USER=contentup
POSTGRES_PASSWORD=contentup123
POSTGRES_DB=contentup
```

### CORS Configuration
- Configurable origins
- All methods enabled
- All headers allowed
- Credentials support

## Database Features

### Models
- Base model with timestamps
- User model with email/name
- Product model with price support
- SQLAlchemy async session management

### Migrations
- Automatic migration generation
- Forward/backward migration support
- Migration history tracking
- Safe schema updates

## Development Features

### Hot Reload
- Automatic code reloading
- Fast development cycle
- Debug mode support
- Error tracking

### Docker Support
- Multi-stage builds
- Production optimization
- Volume mounting
- Health checks

### Nginx Integration
- Reverse proxy
- SSL/TLS support
- Static file serving
- Load balancing ready

## Best Practices Implemented

### Code Organization
- Clear module separation
- Dependency injection
- Environment isolation
- Type hints throughout

### Database
- Connection pooling
- Async operations
- Migration management
- Transaction support

### Security
- CORS protection
- Environment separation
- SSL support
- Password hashing ready

### Development
- Modern tooling (UV)
- Docker support
- Clear documentation
- Development utilities

## Extending the Scaffold

### Adding New Features
1. Create new models in `app/models/`
2. Add routes in `app/api/v1/`
3. Generate migrations with Alembic
4. Update documentation

### Adding New Dependencies
1. Add to `pyproject.toml`
2. Update Docker configuration if needed
3. Update development scripts
4. Document new requirements

## Common Tasks

### Adding a New Model
1. Create model in `app/models/`
2. Generate migration
3. Add API endpoints
4. Update documentation

### Adding New Endpoints
1. Create route in `app/api/v1/`
2. Add dependencies if needed
3. Update OpenAPI documentation
4. Add tests

### Database Changes
1. Modify models
2. Generate migration
3. Test migration
4. Apply to development 
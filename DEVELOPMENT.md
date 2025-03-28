# Development Guide

This guide explains how to set up and run the ContentUp development environment.

## Prerequisites

- Python 3.11 or higher
- PostgreSQL installed locally
- Docker and Docker Compose (for production deployment)
- UV package manager (recommended) or pip

## Local Development Setup

1. **Install PostgreSQL locally**
```bash
# macOS (using Homebrew)
brew install postgresql@15
brew services start postgresql@15

# Ubuntu/Debian
sudo apt install postgresql-15
sudo systemctl start postgresql
```

2. **Create local database**
```bash
# Connect to PostgreSQL
psql postgres

# Create database and user
CREATE DATABASE contentup;
CREATE USER contentup WITH PASSWORD 'contentup123';
GRANT ALL PRIVILEGES ON DATABASE contentup TO contentup;
```

3. **Set up Python environment**
```bash
# Create and activate virtual environment
uv venv --python=python3.11
source .venv/bin/activate  # On Unix/macOS
# or
.\.venv\Scripts\activate  # On Windows

# Install dependencies
uv pip install -e .
```

4. **Configure environment**
```bash
# Copy example environment file
cp .env.example .env

# Update .env with local PostgreSQL settings
POSTGRES_USER=contentup
POSTGRES_PASSWORD=contentup123
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_DB=contentup
```

5. **Run the application**
```bash
uvicorn app.main:app --reload
```

## Production Deployment

1. **Prepare Production Environment**
```bash
# Copy environment file and update with production values
cp .env.example .env

# Edit .env with secure credentials
nano .env
```

2. **Deploy to Production**
```bash
# Start the stack
docker-compose up -d

# View logs
docker-compose logs -f

# Scale web service if needed
docker-compose up -d --scale web=3
```

3. **Production Commands**
```bash
# Stop services
docker-compose down

# Rebuild and restart web service
docker-compose up -d --no-deps --build web

# View specific service logs
docker-compose logs -f web
docker-compose logs -f nginx
```

## Environment Features

### Local Development
- Local PostgreSQL installation
- Hot reload enabled
- Debug mode
- Direct database access
- Faster development cycle

### Production Environment
- Multiple web instances
- Nginx reverse proxy
- SSL/TLS with Let's Encrypt
- PostgreSQL in Docker
- Health checks
- Automatic restarts

## Troubleshooting

### Local Development Issues

1. **Database Connection**
```bash
# Check PostgreSQL status
# macOS
brew services list

# Ubuntu/Debian
sudo systemctl status postgresql

# Test connection
psql -U contentup -d contentup -h localhost
```

2. **Reset Local Database**
```bash
dropdb contentup
createdb contentup
```

### Production Issues

1. **Container Issues**
```bash
# Check container status
docker-compose ps

# View container logs
docker-compose logs

# Restart specific service
docker-compose restart web
```

2. **Database Backup/Restore**
```bash
# Backup
docker exec contentup-db-prod pg_dump -U ${POSTGRES_USER} ${POSTGRES_DB} > backup.sql

# Restore
docker exec -i contentup-db-prod psql -U ${POSTGRES_USER} ${POSTGRES_DB} < backup.sql
```

## Directory Structure
```
contentup/
├── app/                    # Main application package
│   ├── api/               # API endpoints
│   ├── core/              # Core configuration
│   ├── db/                # Database layer
│   │   ├── queries/      # SQLC generated code
│   │   └── schema/       # SQL schema files
│   └── services/         # Business logic
├── docker-compose.yml     # Production Docker configuration
└── .env                   # Environment variables
```

## Best Practices

1. **Environment Variables**
   - Never commit sensitive data to git
   - Use .env for local development
   - Use secure secrets management in production

2. **Database**
   - Use async SQLAlchemy operations
   - Implement database migrations
   - Regular backups in production

3. **Code Quality**
   - Use type hints
   - Document functions and classes
   - Follow PEP 8 guidelines 
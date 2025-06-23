# IoT Device Management Backend

A backend system for managing IoT devices across multiple locations with FastAPI and PostgreSQL.

## Features

- User registration and login with JWT-based authentication
- CRUD operations for devices
- Telemetry data ingestion and retrieval
- Real-time device status monitoring
- Role-based access control

## Prerequisites

- Python 3.10+
- PostgreSQL
- AWS account with permissions to create Elastic Beanstalk environments
- AWS CLI and EB CLI installed

## Local Development

1. Clone the repository
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables or create a `.env` file
5. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

## AWS Elastic Beanstalk Deployment

### Installing EB CLI

```bash
pip install awsebcli
```

### Deploying to AWS Elastic Beanstalk

1. Install AWS CLI and configure your credentials:
   ```bash
   aws configure
   ```

2. Install EB CLI:
   ```bash
   pip install awsebcli
   ```

3. Initialize the EB CLI repository:
   ```bash
   eb init -p python-3.10 iot-device-backend --region us-east-1
   ```

4. Create a new environment with a PostgreSQL database:
   ```bash
   eb create iot-backend-env \
     --instance-type t2.micro \
     --elb-type application \
     --database \
     --database.engine postgres \
     --database.instance db.t3.micro \
     --database.username postgres \
     --database.password yourpassword
   ```

5. Set environment variables:
   ```bash
   eb setenv \
     SECRET_KEY="your-secret-key" \
     ALGORITHM="HS256" \
     ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

6. Deploy the application:
   ```bash
   eb deploy
   ```

7. Open the application:
   ```bash
   eb open
   ```

### Automated Deployment

You can also use the provided deployment script:

```bash
chmod +x deploy_to_eb.sh
./deploy_to_eb.sh
```

Note: You'll need to update the script with your actual VPC IDs, subnet IDs, and other configuration options.

## API Documentation

Once deployed, visit `/docs` for the Swagger UI API documentation.

## Database Migrations

Migrations are managed with Alembic:

```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head
```

## Environment Variables

- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: JWT secret key
- `ALGORITHM`: JWT algorithm (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: JWT token expiration time in minutes 
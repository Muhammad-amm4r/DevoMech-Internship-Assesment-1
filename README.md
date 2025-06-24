# IoT Device Management Backend

A comprehensive backend system for managing IoT devices across multiple locations, built with FastAPI and PostgreSQL.

## Features

- **User Management**: Registration and JWT-based authentication
- **Device Management**: CRUD operations for IoT devices
- **Telemetry**: Ingest and retrieve telemetry data from devices
- **Status Monitoring**: Get the latest known status of devices
- **Security**: Role-based access control

## Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT
- **Database Migrations**: Alembic
- **Container**: Docker

## Project Structure

```
iot-backend/
├── alembic/            # Database migrations
├── app/
│   ├── api/            # API endpoints
│   ├── core/           # Core functionality (auth, config)
│   ├── crud/           # Database operations
│   ├── db/             # Database connection
│   ├── models/         # SQLAlchemy models
│   └── schemas/        # Pydantic models
├── requirements.txt    # Python dependencies
├── alembic.ini         # Alembic configuration
└── README.md           # Project documentation
```

## Getting Started

### Local Development with Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/Muhammad-amm4r/DevoMech-Internship-Assesment-1.git
   cd DevoMech-Internship-Assesment-1
   ```

2. Start the application with Docker Compose:
   ```bash
   docker-compose up -d
   ```

3. Access the API documentation at http://localhost:8000/docs

### Local Development without Docker

1. Clone the repository:
   ```bash
   git clone https://github.com/Muhammad-amm4r/DevoMech-Internship-Assesment-1.git
   cd DevoMech-Internship-Assesment-1
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (create a `.env` file)

5. Start the application:
   ```bash
   uvicorn app.main:app --reload
   ```

6. Access the API documentation at http://localhost:8000/docs

## API Endpoints

- **Authentication**:
  - `POST /auth/token`: Get access token
  - `POST /auth/register`: Register new user

- **Users**:
  - `GET /users/`: List users
  - `POST /users/`: Create user

- **Devices**:
  - `GET /devices/`: List devices
  - `POST /devices/`: Create device
  - `GET /devices/{device_id}`: Get device
  - `PUT /devices/{device_id}`: Update device
  - `DELETE /devices/{device_id}`: Delete device

- **Telemetry**:
  - `POST /telemetry/`: Send telemetry data
  - `GET /telemetry/device/{device_id}`: Get device telemetry
  - `GET /telemetry/device/{device_id}/latest`: Get latest telemetry
  - `GET /telemetry/device/{device_id}/status`: Get device status

## License

MIT

## Contributors

- amm4r

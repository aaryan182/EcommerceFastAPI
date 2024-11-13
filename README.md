# EcommerceFastAPI

> An e-commerce API built with FastAPI designed to handle essential online store operations including user management, product listings, orders and more.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## About

EcommerceFastAPI is an API for managing e-commerce operations. Built with FastAPI, it’s structured for high performance, scalability and ease of use. The project aims to support a complete e-commerce backend including user authentication, product management and order processing.

## Features

- **User Management**: Sign up, login and profile management.
- **Product Listings**: CRUD operations for product categories, items and inventory.
- **Order Management**: Place and manage orders.
- **Authentication**: Secure authentication and authorization using JWT.
- **Admin Dashboard**: Interface to manage products, users and orders .

## Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL 
- **ORM**: SQLAlchemy 
- **Authentication**: JWT-based auth
- **Containerization**: Docker 

## Installation

### Prerequisites

- Python 3.8+
- PostgreSQL database
- Docker 

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aaryan182/EcommerceFastAPI.git
   cd EcommerceFastAPI
2. **Install depedencies**:
   ```bash
   pip install -r requirements.txt
3. **Set up environment variables: Create a .env file and add the following variables**:
   ```bash
   DATABASE_URL=postgresql://user:password@localhost:5432/ecommerce_db
   SECRET_KEY=your_jwt_secret_key
4. **Run migrations (if using an ORM)**:
   ```bash
   alembic upgrade head
5. **Start the server**:
   ```bash
   uvicorn main:app --reload
## Usage

Once the server is running the API will be available at http://localhost:8000.

## API Documentation

FastAPI provides interactive API documentation:

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

## API Endpoints

Here’s a summary of the primary endpoints :

## Authentication

POST /auth/signup - Register a new user.

POST /auth/login - Authenticate a user and return a JWT token.

## Products

GET /products - Retrieve a list of all products.

POST /products - Add a new product (admin only).

GET /products/{id} - Get details of a specific product.

## Orders

POST /orders - Place a new order.

GET /orders/{id} - Retrieve details of an order.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request. Follow these steps:

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

## License

Distributed under the MIT License. See LICENSE for more information.





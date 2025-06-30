# General description

_WebhookHandler - is an asynchronous REST API application for managing user accounts and payments, developed using modern Python technologies. The system provides functionality for users and administrators with different access levels, as well as integration with payment systems via webhooks._

## Core Features
### For Users:
1. 🔐 Email/password authentication

2. 👤 View personal data (ID, email, full name)

3. 💳 Account management (view balances)

4. 💰 View payment history

### For Administrators:
1. 🔐 Email/password authentication

2. 👥 Full user management (CRUD operations)

3. 📊 View all users and their accounts

4. 👤 View administrative profile data

### Payment Integration:
1. 🤖 Payment system webhook processing emulation

2. 🔒 Secure transaction signature verification

3. ⚡ Automatic account creation when needed

4. ✅ Guaranteed single transaction processing

## Implementation Highlights
## 1. Security:

* Webhook signature validation via SHA256

* JWT authentication

* Protection against duplicate transaction processing

## 2. Performance:

* Asynchronous architecture

* Optimized database queries

## 3. Scalability:

* Containerized architecture

* Clear separation of application layers

## 4. Testability:

* Preconfigured test data

* Isolated development environment

## Setup Instructions
### Option 1: Using Docker Compose


`
git clone <repository>`\
`cd <project folder>`\
`docker-compose up -d`
### Option 2: Local Setup

`git clone <repository>`\
`cd <project folder>`\
`python -m venv venv`\
`source venv/bin/activate`  # Linux/MacOS\
`venv\Scripts\activate`  # Windows\
`pip install -r requirements.txt`\
`alembic upgrade head`\
`python main.py`

## Test Credentials
### User:

* Email: user_user@example.com

* Password: 123456

### Admin:

* Email: admin_admin@example.com

* Password: 123456

## API Documentation
##### After launching the server, documentation is available at:

`/docs - Swagger UI`

`/redoc - ReDoc`




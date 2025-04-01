# PhiMart E-commerce API

## Project Overview
PhiMart is a fully functional E-commerce API built using Django and Django REST Framework (DRF). This API enables users to browse products, manage carts, and place orders efficiently. It includes authentication and authorization features, role-based access control, and API documentation for ease of use. The system is designed to be scalable, secure, and easy to integrate with front-end applications.

## Key Features:
- **Authentication & Authorization:** Secure login and registration using Djoser and JWT authentication.
- **Product Management:** Users can browse products, filter by categories, and view product details. Admins can add, update, and delete products.
- **Cart & Orders:** Users can add products to their cart, update item quantities, and place orders.
- **Role-Based Access Control (RBAC):** Separate permissions for users and admins to restrict access where necessary.
- **API Documentation:** Integrated with Swagger and Redoc for better usability.
- **Scalability & Security:** Designed with best practices for handling high traffic and secure data transactions.

## Live Demo
[PhiMart Live Demo](https://your-live-demo-link.com) *(Replace with actual link if available)*

## Technologies Used
- **Backend:** Django, Django REST Framework (DRF)
- **Authentication:** Djoser, JWT Authentication
- **Database:** SQLite (Can be switched to PostgreSQL or MySQL)
- **API Documentation:** Swagger, Redoc

## Prerequisites
Before installing the project, ensure you have the following installed:
- **Python 3.9+**
- **Django 4+**
- **PostgreSQL** *(or any other database you prefer)*
- **Docker (optional for deployment)**

## Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/kashem-khondaker/Phimart_shop
   cd phimart
   ```
2. **Create Virtual Environment & Install Dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate    # For Windows
   pip install -r requirements.txt
   ```
3. **Apply Migrations & Run Server**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Environment Variables (.env setup)
Create a `.env` file in the root directory and add the following:
```
SECRET_KEY=your_secret_key_here
DEBUG=True
DATABASE_URL=your_database_url
ALLOWED_HOSTS=*
```

## Project Folder Structure
```
phimart/
│── api/
│── fixtures/
│── order/
│── phi_mart/
│── product/
│── manage.py
│── .env
│── requirements.txt
```

## Deployment Steps
1. **Setup a Cloud Server** *(AWS, DigitalOcean, or Heroku)*
2. **Install Dependencies & Environment Variables**
3. **Use Gunicorn & Nginx for Production**
4. **Run Database Migrations**
5. **Deploy using Docker (Optional)**

## API Endpoints
### Authentication
| Method | Endpoint | Description |
|--------|-----------------|-----------------------------|
| POST | /auth/users/ | Register a new user |
| POST | /auth/jwt/create/ | Login and receive JWT token |
| POST | /auth/jwt/refresh/ | Refresh JWT token |

### Products
| Method | Endpoint | Description |
|--------|----------------------|--------------------------------|
| GET | /api/v1/products/ | Retrieve all products |
| POST | /api/v1/products/ | Add a new product (Admin only) |
| GET | /api/v1/products/{id}/ | Retrieve detailed product info |
| PATCH | /api/v1/products/{id}/ | Update product details (Admin only) |
| DELETE | /api/v1/products/{id}/ | Remove a product (Admin only) |

### Categories
| Method | Endpoint | Description |
|--------|----------------------|-----------------------------|
| GET | /api/v1/categories/ | View all available categories |
| POST | /api/v1/categories/ | Create a new category (Admin only) |
| GET | /api/v1/categories/{id}/ | View category details |
| PATCH | /api/v1/categories/{id}/ | Edit category details (Admin only) |
| DELETE | /api/v1/categories/{id}/ | Delete category (Admin only) |

## API Documentation
- **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **Redoc UI:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Admin Panel
The default Django admin panel can be accessed at:
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## How to Contribute
1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes and push them.
4. Create a pull request for review.

## License
This project is licensed under the **BSD License**.

## Authors & Credits
- **Your Name** *(Lead Developer)*
- **Contributor 1** *(Feature Development)*
- **Contributor 2** *(Bug Fixing & Testing)*

## Contact Information
For any queries or support, contact:
- **Email:** kashem.khondaker.official001@gmail.com
- **GitHub:** [https://github.com/kashem-khondaker](https://github.com/kashem-khondaker)
- **LinkedIn:** [https://www.linkedin.com/in/kashem-khondakar-280a19236/](https://www.linkedin.com/in/kashem-khondakar-280a19236/)

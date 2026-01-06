# CodeAlpha E-Commerce

A simple e-commerce web application built with Django, featuring user authentication, product catalog, shopping cart, and order management.

## Features

- User registration and login
- Product listing and details
- Shopping cart functionality
- Order placement and history
- Admin panel for product management
- Responsive design with Bootstrap

## Technologies Used

- **Backend**: Django 4.2.5
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Image Handling**: Django's ImageField for product images

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/codealpha_e-commerce.git
   cd codealpha_e-commerce/ecommerce
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/`

## Usage

- **Home Page**: Browse products
- **Register/Login**: Create an account or log in
- **Products**: View product details
- **Cart**: Add items to cart, view cart
- **Checkout**: Place orders
- **My Orders**: View order history
- **Admin**: Access at `/admin/` to manage products

## Project Structure

```
ecommerce/
├── ecommerce/          # Main Django project
├── users/              # User authentication app
├── products/           # Product catalog app
├── orders/             # Order and cart management app
├── static/             # Static files (CSS, JS, images)
├── templates/          # HTML templates
├── media/              # Uploaded product images
└── db.sqlite3          # SQLite database
```

## Models

### Product
- name: CharField
- price: IntegerField
- description: TextField
- image: ImageField

### Order
- user: ForeignKey to User
- product: ForeignKey to Product
- quantity: IntegerField
- total_price: IntegerField
- is_placed: BooleanField

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
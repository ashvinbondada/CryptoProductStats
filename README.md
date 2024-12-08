# Full-Stack Web Application: Interest Form with Coinbase Asset Data

## Overview
This is a small full-stack web application that collects user information through an interest form. Users can input their **name**, **email address**, and a **Coinbase asset** (e.g., BTC-USD). The application processes this data, retrieves important asset information such as **volume**, **price**, and other key metrics, and serves it back to the user. Additionally, the app includes **email functionality** to enhance user interaction.

## Features
1. **Interest Form**:
   - Collects user inputs: name, email, and Coinbase asset.
   - Validates and stores the form data.

2. **Coinbase Asset Data Processing**:
   - Fetches important metrics like volume, price, high, and low values for the specified asset using the Coinbase API.
   - Processes and stores the data for easy access.

3. **Email Functionality**:
   - Sends email notifications to users (e.g., confirmation or summary of their submission).

4. **Data Serving**:
   - Serves the processed asset data back to the user through an API endpoint.

## Technologies Used
- **Frontend**: React with Tailwind CSS for responsive and centered design.
- **Backend**: Django REST Framework (DRF) to handle API requests and manage data processing.
- **Database**: SQLite for development (can be upgraded for production).
- **API Integration**: Coinbase API to fetch real-time asset metrics.
- **Email Service**: Django's built-in email functionality for user notifications.

## How It Works
1. The user submits the interest form via the frontend.
2. The backend processes the form data and sends a request to the Coinbase API to retrieve asset metrics.
3. The retrieved data is stored in the database and served back to the user through an API endpoint.
4. An email is sent to the user as part of the workflow.

## Getting Started
### Prerequisites
- Python 3.x
- Node.js (for the React frontend)
- Coinbase API credentials (if required for extended functionality)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/ashvinbondada/CryptoProductStats.git
   cd CryptoProductStats
   ```

2. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. Migrate the database:
   ```bash
   python manage.py migrate
   ```

5. Start the backend server:
   ```bash
   python manage.py runserver
   ```

6. Navigate to the frontend directory from root and install dependencies:
   ```bash
   cd frontend
   npm install
   ```

7. Start the frontend development server:
   ```bash
   npm run dev
   ```

### Usage
1. Open the app in your browser (usually at `http://localhost:5173/`).
2. Fill out the interest form with your name, email, and a Coinbase asset.
3. Submit the form and view the processed data returned by the app.

## Future Improvements
- Add authentication for enhanced security.
- Implement persistent email notifications with user-specific dashboards.
- Extend support for more data sources beyond Coinbase.

## License
This project is open-source and available under the MIT License.

---
Feel free to reach out with any questions or suggestions!


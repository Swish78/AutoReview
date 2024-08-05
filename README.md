# AutoReview - AI-Powered Product Review Aggregator

AutoReview is a web application that aggregates and analyzes product reviews from multiple sources to provide summarized insights and ratings. Leveraging machine learning, it offers a comprehensive view of product sentiment and quality.

## Features

- Aggregates product reviews from various sources (e.g., Amazon, Yelp).
- Analyzes sentiment of reviews (positive, negative, neutral).
- Provides summarized insights and ratings for each product.
- Real-time and periodic updates using cron jobs.
- Interactive charts and graphs for visualizing review data.

## Tech Stack

- **Frontend:** React, Tailwind CSS
- **Backend:** Django, Django REST Framework (DRF)
- **Machine Learning:** Python-based ML models for sentiment analysis and text summarization
- **Database:** PostgreSQL
- **Cron Jobs:** Celery
- **Web Scraping / APIs:** BeautifulSoup, Scrapy, or platform APIs
- **Deployment:** AWS, Heroku, Vercel, Netlify

## Installation

### Prerequisites

- Python 3.x
- Node.js and npm
- PostgreSQL

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/autoreview.git
   cd autoreview
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL and create a database. Update the database settings in `autoreview/settings.py`.

5. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

6. Set up Celery for periodic tasks:
   ```bash
   celery -A autoreview worker -l info
   ```

7. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install frontend dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

## Configuration

- **Machine Learning Models:** Update paths and configurations for ML models in the `autoreview/ml` directory.
- **Cron Jobs:** Configure Celery tasks for data collection and updates in `autoreview/tasks.py`.

## Usage

1. **Search for Products:** Use the search functionality to find products and view aggregated reviews.
2. **View Insights:** Explore summarized insights and sentiment analysis for each product.
3. **Interactive Charts:** Visualize ratings and sentiment distributions using interactive charts.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Machine Learning Libraries:** Thanks to the open-source libraries used for sentiment analysis and summarization.
- **Frontend Libraries:** React and Tailwind CSS for a responsive and modern UI.

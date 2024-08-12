## Features Checklist

- [x] **Aggregates Product Reviews**
  - [x] Collects reviews from various sources (e.g., Amazon, Yelp)
  - [x] Integrates with platform APIs for review retrieval

- [ ] **Sentiment Analysis**
  - [ ] Analyzes sentiment of reviews (positive, negative, neutral)
  - [] Utilizes Python-based ML models for sentiment analysis 

- [ ] **Summarized Insights**
  - [x] Provides summarized insights for each product -> used "https://huggingface.co/paulmbw/autotrain-productkit-customer-insights-2851583532"
  - [ ] Generates ratings based on aggregated review data

- [ ] **Real-time and Periodic Updates**
  - [ ] Implements cron jobs for periodic updates
  - [ ] Supports real-time data updates

- [ ] **Data Visualization**
  - [ ] Interactive charts and graphs for visualizing review data
  - [ ] Provides various visual representation options (e.g., bar charts, pie charts)

## Tech Stack Checklist

### Frontend
- [x] React
- [x] Tailwind CSS

### Backend
- [x] Django
- [x] Django REST Framework (DRF)

### Machine Learning
- [ ] Python-based ML models for sentiment analysis
- [ ] Text summarization models

### Database
- [ ] PostgreSQL
- [x] SQLite (alternative option)

### Cron Jobs
- [ ] Celery for scheduling tasks

### Web Scraping / APIs
- [ ] BeautifulSoup
- [ ] Scrapy
- [ ] Platform APIs for data retrieval

### Deployment
- [ ] AWS
- [ ] Netlify

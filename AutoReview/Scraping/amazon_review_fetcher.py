import requests
import json


class AmazonReviewFetcher:
    def __init__(self):
        self.base_url = "https://real-time-amazon-data.p.rapidapi.com/product-reviews"
        self.headers = {
            "x-rapidapi-key": "faf3a44d00mshcb8d61c3a12ed38p14383fjsn63d1b83e5928",
            "x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
        }

    def set_querystring(self, asin: str, country: str = 'IN', sort_by: str = "TOP_REVIEWS", star_rating: str = "ALL",
                        verified_purchases_only: bool = False, images_or_videos_only: bool = False,
                        current_format_only: bool = False, page: int = 1) -> dict:
        """
        Create a querystring for the API request with default parameters.

        Parameters:
        - asin (str): Amazon Standard Identification Number (ASIN) of the product.
        - country (str): Country code. Default is 'IN'.
        - sort_by (str): A sorting option. Default is 'TOP_REVIEWS'.
        - star_rating (str): Filter by star rating. Default is 'ALL'.
        - verified_purchases_only (bool): Whether to include only verified purchases. Default is False.
        - images_or_videos_only (bool): Whether to include only reviews with images or videos. Default is False.
        - current_format_only (bool): Whether to include only the current format. Default is False.
        - page (int): Page number. Default is 1.

        Returns:
        - dict: The querystring dictionary.
        """
        return {
            "asin": asin,
            "country": country,
            "sort_by": sort_by,
            "star_rating": star_rating,
            "verified_purchases_only": str(verified_purchases_only).lower(),
            "images_or_videos_only": str(images_or_videos_only).lower(),
            "current_format_only": str(current_format_only).lower(),
            "page": str(page)
        }

    def fetch_reviews(self, querystring: dict):
        """
        Fetch reviews from the API using the provided querystring and headers.

        Parameters:
        - querystring (dict): The querystring dictionary.

        Returns:
        - list: A list of reviews with specific fields extracted.
        """
        response = requests.get(self.base_url, headers=self.headers, params=querystring)
        data = response.json()

        reviews = data.get('data', {}).get('reviews', [])

        extracted_reviews = []
        for review in reviews:
            extracted_review = {
                'review_id': review.get('review_id'),
                'review_title': review.get('review_title'),
                'review_comment': review.get('review_comment'),
                'review_star_rating': review.get('review_star_rating'),
                'review_author': review.get('review_author')
            }
            extracted_reviews.append(extracted_review)

        return extracted_reviews


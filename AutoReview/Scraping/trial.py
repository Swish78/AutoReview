from amazon_review_fetcher import AmazonReviewFetcher
from review_cleaner import ReviewCleaner


def main():
    fetcher = AmazonReviewFetcher()

    querystring = fetcher.set_querystring(asin="B07ZPKN6YR")
    extracted_reviews = fetcher.fetch_reviews(querystring)

    cleaner = ReviewCleaner()

    all_reviews_text = ""
    for review in extracted_reviews:
        original_comment = review['review_comment']
        cleaned_comment = cleaner.clean_review(original_comment)
        all_reviews_text += cleaned_comment + " "

    summary = cleaner.generate_summary(all_reviews_text)

    print(f"Concatenated Reviews: {all_reviews_text}")
    print(f"Summary: {summary}")


if __name__ == "__main__":
    main()

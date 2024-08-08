import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class ReviewCleaner:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("paulmbw/autotrain-productkit-customer-insights-2851583532")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("paulmbw/autotrain-productkit-customer-insights-2851583532")

    def clean_review(self, review: str) -> str:
        """
        Clean the review text using regex.

        Parameters:
        - review (str): The review text.

        Returns:
        - str: The cleaned review text.
        """
        # Remove HTML tags
        review = re.sub(r'<.*?>', '', review)
        # Remove URLs
        review = re.sub(r'http\S+|www\S+|https\S+', '', review, flags=re.MULTILINE)
        # Remove special characters
        review = re.sub(r'\W', ' ', review)
        # Remove all single characters
        review = re.sub(r'\s+[a-zA-Z]\s+', ' ', review)
        # Remove single characters from the start
        review = re.sub(r'\^[a-zA-Z]\s+', ' ', review)
        # Remove numbers
        review = re.sub(r'\d+', '', review)
        # Remove multiple spaces
        review = re.sub(r'\s+', ' ', review, flags=re.I)
        # Convert to lowercase
        review = review.lower().strip()
        return review

    def generate_summary(self, review: str) -> str:
        """
        Use the pretrained model to generate a summary of the cleaned review text.

        Parameters:
        - review (str): The cleaned review text.

        Returns:
        - str: The summary of the review text.
        """
        inputs = self.tokenizer.encode("summarize: " + review, return_tensors="pt", max_length=512, truncation=True)
        outputs = self.model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4,
                                      early_stopping=True)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

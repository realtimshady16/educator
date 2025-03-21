import requests
import json

def get_news(api_key, query="top-headlines", country="us", category=None):
    """
    Fetches news articles from the News API.

    Args:
        api_key: Your News API key.
        query: The type of news to fetch (e.g., "top-headlines", "everything").
        country: The country to fetch news from (e.g., "us", "gb").
        category: The category of news to fetch (e.g., "technology", "sports").

    Returns:
        A list of news articles (dictionaries) or None if an error occurs.
    """

    url = f"https://newsapi.org/v2/{query}?country={country}"

    if category:
        url += f"&category={category}"

    headers = {"X-Api-Key": api_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        if data["status"] == "ok":
            return data["articles"]
        else:
            print(f"Error from News API: {data['message']}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON from News API.")
        return None

def display_news(articles):
    """
    Displays news articles in a formatted way.

    Args:
        articles: A list of news articles (dictionaries).
    """

    if not articles:
        print("No news to display.")
        return

    for index, article in enumerate(articles):
        print(f"\n--- Article {index + 1} ---")
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print(f"Source: {article['source']['name']}")
        print(f"Published At: {article['publishedAt']}")

def main():
    api_key = input("Enter your News API key: ")  # Replace with your actual API key

    country = input("Enter country code (e.g., us, gb): ").lower()
    category = input("Enter category (e.g., technology, sports, or leave blank): ").lower()
    if category == '':
        category = None

    news_articles = get_news(api_key, country=country, category=category)

    if news_articles:
        display_news(news_articles)

if __name__ == "__main__":
    main()
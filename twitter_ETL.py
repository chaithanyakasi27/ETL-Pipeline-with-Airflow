import tweepy
import pandas as pd
import s3fs

def run_twitter_etl():
    # Twitter API v2 credentials (replace with your actual Bearer Token)
    bearer_token = "AAAAAAAAAAAAAAAAAAAAACOCxAEAAAAApfTwlblEiexDzjDMp76Rg5MOGW8%3Da1jBVngQtXIZijNTjEU5pskPH3wC2s0tzAiqKtOHnOtgOmTWn5"

    # Initialize the Tweepy Client
    client = tweepy.Client(bearer_token=bearer_token)

    # Specify the username of the user
    username = "elonmusk"

    # Step 1: Get user ID
    try:
        user = client.get_user(username=username)
        user_id = user.data.id
    except Exception as e:
        print(f"Error fetching user ID for {username}: {e}")
        exit()

    # Step 2: Fetch recent tweets from the user's timeline
    try:
        tweets = client.get_users_tweets(
            id=user_id,
            max_results=100,  # Maximum number of tweets per request
            tweet_fields=["created_at", "text", "id", "public_metrics"]
        )
    except Exception as e:
        print(f"Error fetching tweets for user ID {user_id}: {e}")
        exit()

    # Step 3: Extract the tweet data into a structured format
    tweet_data = []
    if tweets.data:
        for tweet in tweets.data:
            tweet_data.append({
                "tweet_id": tweet.id,
                "created_at": tweet.created_at,
                "text": tweet.text,
                "retweet": tweet.public_metrics["retweet_count"],
                "like": tweet.public_metrics["like_count"],
                "replies": tweet.public_metrics["reply_count"]
            })

    # Step 4: Convert the tweet data into a pandas DataFrame
    df = pd.DataFrame(tweet_data)

    # Step 5: Save to a CSV file on S3
    s3_path = "s3://airflow-demo-project/elonmusk_tweets.csv"
    try:
        df.to_csv(s3_path, index=False)
        print(f"Saved {len(df)} tweets to {s3_path}")
    except Exception as e:
        print(f"Error saving to S3: {e}")

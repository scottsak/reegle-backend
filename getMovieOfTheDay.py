import boto3
import json
import os
from dotenv import load_dotenv

# Initialize the S3 client using environment variables
load_dotenv()
x = os.getenv('AWS_ACCESS_KEY_ID')

print('x', x)

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

def get_movie_of_the_day():
    bucket_name = 'reegle-game'
    object_key = '07-28-2024.json'

    try:
        # Fetch the object from S3
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
        content = response['Body'].read().decode('utf-8')

        # Print the content of the file
        print("Content of the file:")
        print(content)

        # You can further process the content here
        return content

    except Exception as e:
        print('no date found')
        return {
            "dayCount": 90,
            "todaysDate": "4-7-2024",
            "id": 37799,
            "imdbID": "tt1285016",
            "title": "The Social Network",
            "genre": "Biography, Drama",
            "boxOffice": "$96,962,694",
            "rated": "PG-13",
            "imageLink": "https://image.tmdb.org/t/p/original/1PXwh3nJzgRkkYnqfWInJNypeL4.jpg",
            "posterLink": "https://m.media-amazon.com/images/M/MV5BOGUyZDUxZjEtMmIzMC00MzlmLTg4MGItZWJmMzBhZjE0Mjc1XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg",
            "imdbRating": "7.8",
            "runtime": "120 min",
            "releaseDate": "01 Oct 2010",
            "director": "David Fincher",
            "actors": "Jesse Eisenberg, Andrew Garfield, Justin Timberlake"
        }

# Call the function
if __name__ == "__main__":
    get_movie_of_the_day()
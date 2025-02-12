# lib.py

import os
from dotenv import load_dotenv
from openai import OpenAI
import ast
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
from rich.console import Console
from rich.table import Table

# This is only for displaying a progress bar. Just a nice to have.
tqdm.pandas()

def get_api_key() -> str:
    # Get the api key from the .env file
    load_dotenv(override=True)
    api_key = os.getenv('OPENAI_API_KEY')    
    return api_key

def request_text_embedding(text: str, api_key: str) -> list:
    # Request a text embedding from OpenAI for the given text
    client = OpenAI(api_key=api_key)
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

def append_text_embeddings_to_search_data():
    # Read in the sample data
    df = pd.read_csv("search_data.csv")

    # Read in the api key from the .env file
    api_key = get_api_key()

    # Request a text embedding from OpenAI for each row's overview value 
    # and append it as a new column 'overview_text_embedding'
    df["overview_text_embedding"] = df["overview"].progress_apply(
        lambda text: request_text_embedding(text, api_key)
    )

    # Save the a new CSV file with the updated data
    df.to_csv("search_data_with_embeddings.csv", index=False)

def find_similar_matches(search_term: str, show_n: int = 1):
    df = pd.read_csv("search_data_with_embeddings.csv")

    # Convert the 'overview_text_embedding' from string representation to actual lists
    df['overview_text_embedding'] = df['overview_text_embedding'].apply(ast.literal_eval)
    
    api_key = get_api_key()
    
    # Obtain embedding for the search term
    search_term_text_embedding = request_text_embedding(search_term, api_key)
    
    # Convert embeddings to numpy arrays for efficient similarity computation
    search_data_text_embeddings = np.array(df['overview_text_embedding'].tolist())
    search_term_text_embedding = np.array(search_term_text_embedding).reshape(1, -1)
    
    # Here is where the magic happens. We compute the cosine similarity of the search 
    # term embedding and the search data. In "real life" you would probably want to 
    # query a vector capable database for large datasets, but this is a simple 
    # "hello world" example :)
    similarities = cosine_similarity(search_term_text_embedding, search_data_text_embeddings)[0]
    
    # Add similarity scores to the DataFrame
    df['similarity'] = similarities
    
    # Sort search data by similarity in descending order and select the top N
    df_sorted_by_similarity = df.sort_values(by='similarity', ascending=False).head(show_n)

    return df_sorted_by_similarity
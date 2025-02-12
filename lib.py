# lib.py

import os
from dotenv import load_dotenv
from openai import OpenAI

def get_api_key() -> str:
    load_dotenv(override=True)
    api_key = os.getenv('OPENAI_API_KEY')    
    return api_key


def get_text_embedding(text: str, api_key: str) -> list:
    client = OpenAI(api_key=api_key)
    response = client.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

def append_text_embedding_to_search_data():
    try:
        df = pd.read_csv("search_data.csv")
    except FileNotFoundError:
        typer.echo("Error: 'data/search_data.csv' not found.")
        raise typer.Exit(code=1)

    # Combine 'title' and 'overview' into a single text field
    df['title_overview'] = df.apply(concatenate_title_overview, axis=1)
   
    typer.echo("Generating embeddings. This may take a while depending on the dataset size...")
    api_key = load_api_key()

    # Generate embeddings for each combined text entry with a progress bar
    try:
        df["overview_text_embedding"] = df["title_overview"].progress_apply(
            lambda text: get_text_embedding(text, api_key)
        )
    except Exception:
        typer.echo("Failed to generate embeddings.")
        raise typer.Exit(code=1)

    # Remove the temporary 'title_overview' column
    df.drop(columns=['title_overview'], inplace=True)

    # Save the updated DataFrame with embeddings
    try:
        df.to_csv("data/search_data_with_embeddings.csv", index=False)
        typer.echo("Search data initialized and saved to 'data/search_data_with_embeddings.csv'.")
    except Exception:
        typer.echo("Error: Failed to save the embeddings to 'data/search_data_with_embeddings.csv'.")
        raise typer.Exit(code=1)
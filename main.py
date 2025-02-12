import argparse
import sys
import os
import lib
from rich.console import Console
from rich.table import Table

def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description='Find the best matches for a given search term.')
    parser.add_argument('search_term', type=str, help='The search term to find matches for.')
    parser.add_argument('--top_n', type=int, default=1, help='Number of top matches to display (default: 1).')
    args = parser.parse_args()
    
    # Check if the "search_data_with_embeddings.csv" file exists and if not, create it
    # This will take some time, but will only be required once
    search_data_embeddings_file = "search_data_with_embeddings.csv"
    if not os.path.exists(search_data_embeddings_file):
        print("Generating embeddings for serch data. This may take a while...but is needed only once.")
        lib.append_text_embeddings_to_search_data()
        print(f"Embeddings generated and saved to '{search_data_embeddings_file}'.")
    
    # Find similar matches for the search term
    similar_matches = lib.find_similar_matches(args.search_term, args.top_n)

    # Display results in a rich table. This is a nice to have for readable results.
    console = Console()
    table = Table(
        title=f"Top {args.top_n} Semantic Search Results for: '{args.search_term}'",
        show_lines=True
    )

    table.add_column("Similarity Score", justify="left", style="green")
    table.add_column("Title", justify="right", style="cyan", no_wrap=True)
    table.add_column("Overview", justify="left", style="magenta")

    for _, row in similar_matches.iterrows():
        table.add_row(f"{row['similarity']:.3f}", row['title'], row['overview'])

    console.print(table)
        

if __name__ == '__main__':
    main()

# Requirements
```
- macOS (I only have tested on my mac)
- python3 
- [venv](https://docs.python.org/3/library/venv.html) 
```

# Getting Set Up

## Install Dependencies

```
$ chmod +x install.sh
$ ./install.sh
```

## Create/Add Open API Key

A basic API key costs $5 and for normal learning purposes learning, lasts a long time. 

- goto https://openai.com/index/openai-api/ and create an account and log in.
- create an api key here: https://platform.openai.com/api-keys
- then copy/paste the key into .env file in root of project. If it is not there, run `./install.sh` it creates it. 

# How to use

```
# always initialize python virtual environment (venv) in a new terminal session
$ source venv/bin/activate
```

## Initializing search data

The sample data (100 popular movies) is in /search_data.csv. It is stored without text embeddings. 
To initialize text embedding data, run the search command (see *Search* section below) and the 
script will requests test embeddings for search data and create a search_data_with_embeddings.csv
in the root w/ embeddings appended.

## Search

```
# Show top result
$ python main.py "adventure heroes"

# Show top 10 results in desc sementic similarity order
$ python main.py "adventure heroes" --top_n 10

```



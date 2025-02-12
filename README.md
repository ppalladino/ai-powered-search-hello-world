# Requirements
```
- macOS (I only have tested on my mac)
- python3 
- [venv](https://docs.python.org/3/library/venv.html) 
```

# GETTING SET UP

## INSTALL DEPENDENCIES

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
$ ./start.sh 
```

## Initializing search data

The sample data (100 popular movies) is in ./data/search_data.csv. It is stores without text embeddings. To initialize text embedding data:

```
$ python3 ./cli.py init_data
```

## Search

```
# Show top result
$ python3 ./cli.py search "science fiction about technology"

# Show top 10 results in desc sementic similarity order
$ python3 ./cli.py search "science fiction about technology" --n 10

```
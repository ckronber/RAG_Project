import argparse
import json
import string
from nltk.stem import PorterStemmer

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            # print the search query here
            print(f"Searching for: {args.query}")
        case _:
            parser.print_help()
    
    with open("/home/ckronber/BootDev/rag-search-engine/data/movies.json", "r", encoding="utf-8") as file:
        movies_json = json.load(file)

    with open("/home/ckronber/BootDev/rag-search-engine/data/stopwords.txt","r") as file:
        stop_words = file.read().splitlines()

    stop_words_nopunc = [remove_puncutation_and_lower(word) for word in stop_words]
    movie_num = 1
    search_value = remove_puncutation_and_lower(args.query)

    for movie in movies_json["movies"]:
        movie_title_search = remove_puncutation_and_lower(movie["title"])
        split_in_movie = split_search(search_value,movie_title_search,stop_words_nopunc)
        
        if split_in_movie:
            movie_title = movie["title"]
            print(f"{movie_num}. {movie_title}")
            movie_num +=1
        
        if movie_num > 5:
            break

def remove_puncutation_and_lower(input_val:string) -> string:
    input_val = input_val.lower()
    return input_val.translate(str.maketrans("","",string.punctuation))

def split_search(search_in:string, movie_title:string, stop_words:list) -> bool:
    split_vals = search_in.split()
    stemmer = PorterStemmer()
    for val in split_vals:
        if (stemmer.stem(val) in movie_title) and (stemmer.stem(val) not in stop_words): 
            return True

if __name__ == "__main__":
    main()

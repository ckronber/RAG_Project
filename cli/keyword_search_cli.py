import argparse
import json
import string

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

    movie_num = 1
    search_value = remove_puncutation_and_lower(args.query)

    for movie in movies_json["movies"]:
        movie_title_search = remove_puncutation_and_lower(movie["title"])
        if(search_value in movie_title_search):
            movie_title = movie["title"]
            print(f"{movie_num}. {movie_title}")
            movie_num +=1
        if movie_num > 5:
            break

def remove_puncutation_and_lower(input_val:string) -> string:
    input_val = input_val.lower()
    return input_val.translate(str.maketrans("","",string.punctuation))

if __name__ == "__main__":
    main()

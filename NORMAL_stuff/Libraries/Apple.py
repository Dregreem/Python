import requests
import sys
import json

def fetch_itunes_songs(search_term):
    all_results = []
    limit = 50  # Number of results per page
    offset = 0  # Initial offset
    
    while True:
        # Construct the API URL with the dynamic search term, limit, and offset
        url = f"https://itunes.apple.com/search?entity=song&limit={limit}&offset={offset}&term={search_term}"
        
        # Send a GET request to the iTunes Search API
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Check if there are results
            if data['resultCount'] == 0:
                break  # No more results, break out of the loop
            
            # Append the current page of results to the list
            all_results.extend(data['results'])
            
            # Increment the offset to fetch the next page
            offset += limit
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            break
    
    return all_results

def main():
    # Check if exactly one command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python Apple.py <search_term>")
        return
    
    search_term = sys.argv[1]
    all_songs = fetch_itunes_songs(search_term)
    
    # Print the total number of songs retrieved
    print(f"Total songs found for '{search_term}': {len(all_songs)}")
    
    # Print the track names of all songs retrieved
    for song in all_songs:
        print(song["trackName"])

if __name__ == "__main__":
    main()

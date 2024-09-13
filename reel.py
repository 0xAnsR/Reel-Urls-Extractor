import re

def extract_reel_ids(text):
    # Use regex to find all reel IDs in the given text
    regex = r'/reel/(\d+)'
    matches = re.findall(regex, text)
    return matches

def generate_urls(reel_ids):
    # Generate URLs from reel IDs
    urls = [f"https://web.facebook.com/reel/{id}" for id in reel_ids]
    return urls

def main():
    # Read HTML text from the user
    print("Paste your HTML text containing reel IDs below (Ctrl+D to end input):")
    html_text = ""
    try:
        while True:
            line = input()
            html_text += line + "\n"
    except EOFError:
        pass

    # Extract reel IDs
    reel_ids = extract_reel_ids(html_text)

    # Generate URLs
    urls = generate_urls(reel_ids)

    # Output the results
    if urls:
        print("\nGenerated URLs:")
        for url in urls:
            print(url)
    else:
        print("No reel IDs found.")

if __name__ == "__main__":
    main()

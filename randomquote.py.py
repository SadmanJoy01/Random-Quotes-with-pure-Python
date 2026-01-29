import urllib.request
import json
import ssl

def get_random_quote():
    url = "https://api.quotable.io/random"

    context = ssl._create_unverified_context()

    try:
        with urllib.request.urlopen(url, context=context) as response:
            data = json.loads(response.read())

            quote = data["content"]
            author = data["author"]

            print("\n💬 Random Quote")
            print("----------------------------")
            print(f"\"{quote}\"")
            print(f"— {author}\n")
            print(input("Press enter to exit"))


    except Exception as e:
        print("❌ Failed to fetch quote")
        print("Error:", e)


if __name__ == "__main__":
    get_random_quote()

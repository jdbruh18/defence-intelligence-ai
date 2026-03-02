import requests
from bs4 import BeautifulSoup

URL = "https://www.isro.gov.in"


def fetch_isro_updates():
    updates = []

    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a")

        seen = set()

        for link in links:
            text = link.get_text(strip=True)

            if len(text) > 35 and text not in seen:
                seen.add(text)

                updates.append({
                    "source": "ISRO",
                    "category": "Space Technology",
                    "title": text
                })

        return updates[:10]

    except Exception as e:
        print(f"Error fetching ISRO updates: {e}")
        return []
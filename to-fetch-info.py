import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.olx.in/items/q-car-cover"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

  
    with open("olx_car_covers.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Price", "Location", "Link"])

       
        items = soup.find_all("li", {"data-aut-id": "itemBox"})
        for item in items:
            title = item.find("span", {"data-aut-id": "itemTitle"})
            price = item.find("span", {"data-aut-id": "itemPrice"})
            location = item.find("span", {"data-aut-id": "item-location"})
            link = item.find("a")["href"] if item.find("a") else ""

            writer.writerow([
                title.text.strip() if title else "",
                price.text.strip() if price else "",
                location.text.strip() if location else "",
                "https://www.olx.in" + link if link else ""
            ])

    print("Results saved to olx_car_covers.csv")
else:
    print("Failed to fetch OLX page, status:", response.status_code)

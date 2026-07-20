import time
import csv
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool, cpu_count


def gen_csv(quotes: list[dict[str, str]], file_name: str) -> None:
    print("Exporting scrapped data to CSV")
    with open(file_name, mode="w") as csv_file:
        fieldnames = ["text", "author", "tags"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(quotes)
    print("Quotes exported to CSV")


def scrape_page(url: str) -> list[dict[str, str]]:
    print(f"Scraping page: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    quotes = []
    quote_elements = soup.select(".quote")
    for element in quote_elements:
        text = element.select_one(".text").get_text()
        author = element.select_one(".author").get_text()
        tags = [tag.get_text() for tag in element.select(".tag")]
        quotes.append(
            {
                "text": text,
                "author": author,
                "tags": ", ".join(tags),
            }
        )
    print(f"Page '{url}' scrapped successfully")
    return quotes


def scrape_quotes() -> None:
    urls = [
        "http://quotes.toscrape.com/",
        "http://quotes.toscrape.com/page/2",
        "http://quotes.toscrape.com/page/3",
        "http://quotes.toscrape.com/page/4",
        "http://quotes.toscrape.com/page/5",
        "http://quotes.toscrape.com/page/6",
        "http://quotes.toscrape.com/page/7",
        "http://quotes.toscrape.com/page/8",
        "http://quotes.toscrape.com/page/9",
        "http://quotes.toscrape.com/page/10",
    ]
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(scrape_page, urls)
    quotes = [quote for sublist in results for quote in sublist]

    gen_csv(quotes, "quotes_multi.csv")


def main() -> None:
    scrape_quotes()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter() - start
    print(f"Execution time: {end:.2f} seconds")

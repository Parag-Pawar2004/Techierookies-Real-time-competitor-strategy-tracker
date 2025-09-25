import datetime
def scrape_iphone(model_name):
    """
    Dummy scraper: returns fake data for now.
    Later we will replace with CrawlAI
    """
    data = {
        "model": model_name,
        "price": "80,000",
        "site":"Amazon",
        "rating":"4.5",
        "review":"Battery Life is amazing ",
        "scraped_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return data
if __name__=="__main__":
    iphone = scrape_iphone("iPhone 15 Pro")
    print(iphone)
import wikipedia
import time

def crawl(start_page, end_page, previous_link = ""):
    if start_page.url == end_page.url:
        return True

    if len(start_page.links) <= 0:
        return False

    for link in start_page.links:
        previous_link = previous_link + " -> " + link
        print(previous_link)
        try:
            next_page = wikipedia.page(link)
        except wikipedia.exceptions.PageError:
            print(link + " not found")
            continue
        
        return crawl(next_page, end_page, previous_link)
        time.sleep(1)


start_location = "New York City"
end_location = "Warsaw"

start_page = wikipedia.page(start_location)
end_page = wikipedia.page(end_location)

crawl(start_page, end_page)
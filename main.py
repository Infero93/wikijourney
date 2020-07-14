import wikipedia
import time

def crawl(start_page, end_page, previous_link = "", visited = set()):
    visited.add(start_page.pageid)
    
    if start_page.url == end_page.url:
        return True

    for link in start_page.links:
        previous_link = link if len(previous_link) <= 0 else previous_link + " -> " + link
        print(previous_link)

        next_page = None
        try:
            next_page = wikipedia.page(link)
        except wikipedia.exceptions.DisambiguationError:
            #TODO: Get the titles from the exception
            print(link + " not found")
            continue
        except wikipedia.exceptions.PageError:
            print(link + " not found")
            continue
        
        if not next_page:
            return False

        if next_page.pageid in visited:
            print(link + " already visited")
            continue

        return crawl(next_page, end_page, previous_link, visited)
    return False


start_location = "New York City"
end_location = "Warsaw"

start_page = wikipedia.page(start_location)
end_page = wikipedia.page(end_location)

crawl(start_page, end_page)
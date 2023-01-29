from bs4 import BeautifulSoup
import time
import requests
from urllib.parse import urlparse
import urllib
from random import randint


USER_AGENT = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


YAHOO_SEARCH_ENDPOINT = "https://search.yahoo.com/search?p="
YAHOO_SEARCH_SELECTOR = "a.ac-algo.fz-l.ac-21th.lh-24"


class SearchEngine:

    @staticmethod
    def search(query, should_sleep=True):
        start_time = time.time()
        print('\n\nPROCESSING QUERY: ' + query)
        url = YAHOO_SEARCH_ENDPOINT + '+'.join(query.split()) + '&n=30'
        print('URL: ' + url)
        if should_sleep:
            time.sleep(randint(10, 100))

        soup = BeautifulSoup(requests.get(url, headers=USER_AGENT).text, "lxml")
        new_results = SearchEngine.scrape_search_result(soup)
        end_time = time.time()
        print('TIME TAKEN: ' + str(end_time - start_time) + ' seconds')
        return new_results

    @staticmethod
    def scrape_search_result(soup):
        raw_results = soup.find_all("a", attrs={"class": "d-ib fz-20 lh-26 td-hu tc va-bot mxw-100p"})
        # print('RAW RESULTS:')
        # print(raw_results)
        results = []
        count_found = 0
        for result in raw_results:
            # print(result)
            # get the url from the result
            link = result.get('href')
            link = '/'.join(link.split('/')[7:])
            link = urllib.parse.unquote(link)
            # If the link starts with "RU=", remove "RU="
            if link.startswith("RU="):
                link = link[3:]

            link = link.split('//RK=2')[0]

            # Check if link is legit
            if not link:
                continue
            base_url = parse_base_url_path_parameters_query_more(link)
            # If the base_url does not start with "www.", add "www."
            if not base_url.startswith("www."):
                base_url = "www." + base_url

            # If the base_url starts with "www.", remove "www."
            # if base_url.startswith("www."):
            #     base_url = base_url[4:]
            # If the base_url has "/RK=2", remove "/RK=2" and everything after it
            if "/RK=2" in base_url:
                base_url = base_url.split("/RK=2")[0]
            # If there is a trailing slash, remove it
            if base_url.endswith("/"):
                base_url = base_url[:-1]
            if base_url not in results:
                results.append(base_url)
                count_found += 1
            if count_found == 10:
                break
        return results


def parse_base_url_path_parameters_query_more(url_string: str) -> str:
    # Given a URL string, returns the base URL, path, parameters, and query
    # url_string is a string
    # returns a string
    url = urlparse(str(url_string))
    return url.netloc + url.path + url.params + url.query

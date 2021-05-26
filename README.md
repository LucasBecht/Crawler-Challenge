# Crawler-Challenge
I'll do my best to explain my thought process on the Crawler here.

After my homework for my Python class (On my other repository) i've got more practice and understanding on how to use Print/Input and If/Else.
Searching for the Definition of a Web Crawler, i've seen These websites (and more) :

https://www.webfx.com/blog/internet/what-is-a-web-crawler/

https://en.wikipedia.org/wiki/Web_crawler.

It seems a Crawler that focuses on Retrieving information from a specific Database is called a Web Scraper, that'll help me search more about it.

Installed additional tools that'll be useful for making the crawler: Request, BeautifulSoup and pandas.

After looking around on various guides, i managed to get good progress for today, i have classes now so i'll keep doing this tomorrow.
next step it seems is to set up a Loop so i can make it read the other pages as well, and then obviously, extracting the actual information i want from the stuff,
otherwise, good pace today.

After days of trial and error, i managed to replicate the Crawler from the guides i was following (Crawler Following The Guide.py), but trying to use that knowledge to create one for another website 
is giving me trouble, trying to fix the HTTP i get from the website i chose, it seems like it's getting a different HTTP than the page i wanted.

Managed to replicate a similar code from something i normally use (MyAnimeList, Crawler-MAL.py) to test the knowledge i got from the guide code. 
still having trouble doing the same in the websites i chose (Kabum, Pichau.), i would need to make pretty big alterations to the code, and i don't have enough 
knowledge to do that. still trying though.

so for now:

**Crawler Following The Guide.py** is the Crawler i made following a guide that i found, used it to test out the waters.

**Crawler-MAL.py** takes the Top 50 Animes from the website, and saves it as a .csv, managed to understand and replicate the code well enough.

**Crawler.py** is the code i wanted to try for the Hardware Websites (Kabum,Pichau), been having trouble making it work though,
when i try to scrape it using Find_all i cannot find any of the Divs i need, i need to figure out if i'm doing something wrong with the url request, or if i'm trying to find the wrong Divs, i checked robots.txt on both pages, and i think i'm allowed to scrape it normally, maybe not,

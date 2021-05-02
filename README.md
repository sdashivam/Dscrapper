Scrapy Project for extracting books details from flipkart.com, storing it in MongoDB Atlas and running on the Scrapyrt server.

Web scraping is the process of using bots to extract content and data from the website.  According to wikipedia web scraping is used for contact scraping, ans as a component of applications used for web indexing, web mining and data mining, online price change monitoring and price comparison, product review scraping(to watch competition), gathering product listings, weather data monitoring, website change detection, research, tracking online presence and reputation, web mashup and web data integration.

Web scraping and crawling aren’t illegal by themselves.but making so many requests and hitting the server make block the particular IP address or even in some cases copyright violations. So before starting to scrape any website first read terms and conditions carefully. Also we can use domain.com/robots.txt to understand the allowed areas where we can perform scraping.

In this project we are going to scrape flipkart.com books section where we will extract all the information related to the new releases. We will use Scrapy in this project, Scrapy is a free and open-source web crawling framework written in python for web scraping. Check the documentation here: https://docs.scrapy.org/en/latest/intro/tutorial.html

For starting our first spider we need to create a python virtual environment. I'm using Python 3.9.4 with VS Code. you can use any editor of your choice and follow these steps:

1. pip install virtualenv

2. pip install virtualenvwrapper

3. virtualenv snv(provide any name for environment)

4. Once a virtual environment has been created we can open the created folder and start writing the code.

5. So as we can see our virtual environment has been activated we will start installing scrapy.

6. For installing scrapy write pip install scrapy it will install all the dependent libraries with it.

7. Once we have installed scrapy we can check the version by writing scrapy -version

8. Now we have to start our project with scrapy so in command prompt enter command with project name;
scrapy startproject flipscrap 

9. It will create a project for us where we will have the following files:

10. From the starting first we have a spiders folder where we have to create a python file in that we will write code for our first spider. Here i have given bookcrawl.py name. Then we have items.py file in these file we have to write items and itemloader for our crawler. Next we have middlewears.py file here we have all the middlewares for crawler we will not make any changes as of now here. Then pipelines.py file in this file we will write code for database creation and connection with the spider so whatever details we will extract all the details stored in the database. And finally we have a settings.py file where we will make some changes accordingly.

11. Go in the bookcrawl.py file in the spiders folder and create a class in this class we will define a name for the scraper, url for data extraction and a parse method. In the parse method we will use xpath and css selector for selecting a specific html tag id. We can use BeautifulSoup or lxml also. Scrapy comes with its own mechanism for extracting data, they’re called selectors
because they “select” certain parts of the HTML document specified either by XPath  or CSS expressions.

12. In the books section of filpkart.com we are going to extract the name of the book, Author name and format, Rating, Price and Image of the book. So will select that specific id’s with the chrome developer tool (press F12 or click on inspect then hover the required information so will get the specific id for specific information).

13. Because we are using here items.py files class so we have to import class of items.py file and make a instance inside the parse method. So the order is first we will scrape the data in bookcrawl.py file, then scraped data will go in the items.py file where we will define a method for cleaning it then it will store all of that data in the database defined in pipelines.py file.

14. Here I'm using the MongoDB database so in the pipelines.py file we have to create a __init__ () method where we will establish a connection between spider and the Database. then in the process_item() method all the scraped data insert into a dict format into the DB.

15. Make sure after writing a class in pipelines.py file we have to go in settings.py file and comment in ITEM_PIPELINES.

16. Move to bookcrawl.py file as we all know ecommerce sites have a various pages for products. So if we want to extract information from multiple pages we have to write pagination for that. So with the help of that we can scarpe as many pages we want. (I'm going to scrape only 4 pages if you want, you can change the count of the pages.)
Now all the steps are done, we have created our first spider, loading all data in the Itemloader and storing all the scraped data in the mongodb.
This is the time to start the spider, go in the command shell and make sure you are in the right directory, and enter the command; we need to write here the name of the spider that we had written in the bookcrawl.py class.
scrapy crawl bookscrap   
Once, we enter these command if everything is correct it will start scraping all the desired informations those we can see in the terminal:

So now our spider is working fine and also check the DB where it will store all the information. 

Additionally, scrapy also provides more powerful  applications like scrapyrt, scrapyd and scrapywebd. The short introduction of all of these three applications is given below:-

Scrapyd:- scrapyd is an application for deploying and running scrapy spiders, it enables you to deploy your projects and control their spiders using JSON API. kindly check documentation for more details: https://scrapyd.readthedocs.io/en/stable/

Scrapydweb:- it is a web app for Scrapyd cluster management, with support for scrapy log analysis and visualization.kindly check documentation for more details:https://github.com/my8100/scrapydweb

Scrapyrt:- scrapyrt is an HTTP server that provides API for scheduling Scrapy spiders and making requests with spiders. We are going to use it in our project. kindly check documentation for more details: https://github.com/scrapinghub/scrapyrt

So for that, we just have to write a pip install scrapyrt for installation inside the project. Make sure you must have a scrapy.cfg file because when we start scrapyrt it will go and check for the scrapy.cfg file. 

To start a server we have to write in command prompt scrapyrt by default it will start server on localhost:9080 port. 

Go in the browser and in search bar enter the address:
http://localhost:9080/crawl.json?spider_name=bookscrap&url=https://www.flipkart.com/search?q=books

We have to write spider name in spider_name=bookscrap and in the url need to provide target URL that is url=https://www.flipkart.com/search?q=books

After that once we press enter it will crawl all the required data we can see in the webpage(we have crawl data in the raw JSON format to make it more readable you can add extension named  JSON formatter https://github.com/callumlocke/json-formatter)

All Done, our scraper is working fine. One more good thing about scrapyrt is that it will automatically create a log folder(named logs) inside the project directory where we can see all the details about performance of  the scraper.

Inside the logs folder’s file we can see all the outputs.

Finally, we have successfully created a spider using Scrapy framework, integrated it with the mongoDB Atlas and running on the Scrapyrt server.


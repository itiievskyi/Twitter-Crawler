# Twitter Scraper (Python3) - Get stats of user's feed
***
### What is this project about?
It's about parsing the Twitter user's feed and getting some useful info from his/her last N tweets, such as:
* Text of the tweet
* The number of reactions (comments, likes and retweets)
* Initial tweet author and his account @link (for example, you will know if user retweeted somebody's post)
* Whether the tweet contains picture, video or tweet quotation

When some piece of magic is done, you get a dataframe that contains all above mentioned data:
![Tweets in Datafarme](/images/2.png)

There is also a simple command that allows you to save the dataframe into csv-file.
***
### How to (for *nix systems):
1. **Install**
    * `git clone https://github.com/itiievskyi/Twitter-Scraper.git ~/twitter-scraper/`
    * `cd ~/twitter-scraper/`
    * `pip3 install -r requirements.txt`

2. **Use**
    * `jupyter notebook TwitterScraper.ipynb` or
    * `jupyter notebook` and open **TwitterScraper.ipynb** through the Jupyter Notebook menu
    * Press **Cell** -> **Run All**
    * Type the Twitter account link. Both @name and name are accepted. For example, if you want to get stats from Obama's account, you can use either `@BarackObama` or `barackobama`
    * Type the number of tweets you want to analyze
    ![Inputting parameteres](/images/1.png)
    * Wait until the browser window (that should be open now) is closed
***

## Developer notes

### What technologies or libraries does this project use?
In the core of the project are:
* Python 3
* [selenium](https://www.seleniumhq.org/) package
* [pandas](https://pandas.pydata.org/) package
* [Jupyter Notebook](https://jupyter.org/index.html) environment
***
### Troubleshooting
* In case of invalid result (for example, dataframe contains less tweets than it should) try to increase the sleeping time:
  ```python
  while True:
      body.send_keys(Keys.END)
      sleep(2)
  ```
  It may depend on your computer characteristics and Internet connection speed.
***
### Enjoy!

import scrapy

from time import strftime, gmtime

class TwitterSpider(scrapy.Spider):
    name = 'twitter'

    def __init__(self, user):
        self.user = user
        self.url = f'https://twitter.com/{user}'

    def parse(self, response):

        for tweet in response.css('div.tweet'):
            yield {
                'time': strftime('%d %b %Y %H:%M', gmtime(int(tweet.css('span._timestamp::attr(data-time)').extract_first()))),
                'author': tweet.css('strong.fullname::text').extract_first(),
                'account': '@' + tweet.css('span.username b::text').extract_first(),
                'text': (tweet.css('p.tweet-text::text').extract_first())[:20] + '...',
                'comments': tweet.css("span.ProfileTweet-actionCount::attr(data-tweet-stat-count)").extract()[0],
                'retweets': tweet.css("span.ProfileTweet-actionCount::attr(data-tweet-stat-count)").extract()[1],
                'likes': tweet.css("span.ProfileTweet-actionCount::attr(data-tweet-stat-count)").extract()[2]
            }

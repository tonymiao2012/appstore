import scrapy

class AppstoreItem(scrapy.Item):
	#Define fields
	title = scrapy.Field()
	url = scrapy.Field()
	appid = scrapy.Field()
	intro = scrapy.Field()


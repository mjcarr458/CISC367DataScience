import scrapy

class HotelSpider(scrapy.Spider):
    name = "monster"
    start_urls = [
        "https://monsterhunter.fandom.com/wiki/MHRise:_Monsters#Large_Monsters"
    ]

    custom_settings = {
        "DEPTH_LIMIT": 1
    }

    """
    def parse(self, response):
        for row in response.css("table"):
            for name in row.css("a::text").getall():
                print("NAME", name)
                yield {
                    "name": name
                }
    """
    """
    def parse(self, response):
        for row in response.css("table"):
            for td in row.css("td"):
                for a in td.css("a"):
                    print(a)
                yield {
                    "link": a.css("a::attr(href)").extract(),
                }
    """

    def parse(self, response):
        for row in response.css("table"):
            for td in row.css("td"):
                for a in td.css("a"):
                    '''
                    print(a)
                    '''
                    yield scrapy.Request(response.urljoin(a.css("a::attr(href)").extract()[0]), callback=self.parse_info) 
    
    '''
    def parse_info(self,repsonse):
        for info in repsonse.css("aside"):
            print("TABLE? ", info)
            yield {
                "Name" : info.xpath('//*[@id="mw-content-text"]/div/aside/h2[1]').extract(),
                "Class" : info.css("div.class::text").getall()
            }
    '''
    def parse_info(self,response):
        
        yield {
            "Name" : response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "pi-title", " " ))]/text()').extract_first(),
            "Class" : response.css('.pi-secondary-background+ .pi-border-color .pi-font a::text').getall(),
            "Weakness" : response.css('.pi-item-spacing:nth-child(5) a::text').getall(),
            "Habitat" : response.css('.pi-item-spacing:nth-child(6) a::text').getall(),
            "Size" : response.css('.pi-border-color:nth-child(7) .pi-font::text').getall()
        }
import scrapy


class SmartWatchesSpider(scrapy.Spider):
    name = 'smart_watches'
    allowed_domains =['https://www.amazon.com']
    # allowed_domains = ['https://www.amazon.com/b/?node=7939901011&ref_=Oct_s9_apbd_odnav_hd_bw_bAy3Jud_1&pf_rd_r=Y4VS50DW571EWWYNGNEY&pf_rd_p=717d8825-1df5-56b9-97ee-882992f37e32&pf_rd_s=merchandised-search-11&pf_rd_t=BROWSE&pf_rd_i=10048700011']
    start_urls = ['https://www.amazon.com/b/?node=7939901011&ref_=Oct_s9_apbd_odnav_hd_bw_bAy3Jud_1&pf_rd_r=Y4VS50DW571EWWYNGNEY&pf_rd_p=717d8825-1df5-56b9-97ee-882992f37e32&pf_rd_s=merchandised-search-11&pf_rd_t=BROWSE&pf_rd_i=10048700011']

    custom_settings={'FEED_URI': "smart_watches%(time)s.json",
                       'FEED_FORMAT': 'json'}


    def parse(self, response):
        print(f"Pprocesing: {response.url}")
        #Extract data using css selectors
        product_name = response.css(".a-size-base::text").extract()
        product_price = response.css(".a-price-whole::text").extract()

        row_data = zip(product_name, product_price)
        for item in row_data:
            scraped_info = {
            "page" : response.url,
            'product_name' : item[0],
            'product_price' : item[1],
            }
        yield scraped_info


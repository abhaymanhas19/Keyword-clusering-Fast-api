import requests
import pandas as pd
from pprint import pprint


class ProcessKeywords:
    def __init__(self, keywords_set, pivot) -> None:
        self.keywords = keywords_set
        self.url_set = {
  "best supplements for immune system": [
    "https://www.healthline.com/nutrition/immune-boosting-supplements",
    "https://health.clevelandclinic.org/vitamins-best-boosting-immunity/",
    "https://www.unitypoint.org/news-and-articles/5-immune-system-boosters-to-try---unitypoint-health",
    "https://www.cnbc.com/2022/01/30/the-4-vitamins-and-supplements-this-doctor-takes-every-day-for-a-strong-immune-system.html",
    "https://gilbertlab.com/immune-system/supplements-to-boost-immunity/",
    "https://www.mayoclinichealthsystem.org/hometown-health/speaking-of-health/fight-off-the-flu-with-nutrients",
    "https://www.forbes.com/health/body/best-foods-and-vitamins-for-immune-health/",
    "https://www.cnet.com/health/nutrition/best-immunity-supplements/",
    "https://www.mindbodygreen.com/articles/supplements-for-immunity",
    "https://www.goodrx.com/well-being/supplements-herbs/foods-vitamins-supplements-for-boost-immune-system"
  ],
  "best supplement for immune system": [
    "https://www.healthline.com/nutrition/immune-boosting-supplements",
    "https://www.unitypoint.org/news-and-articles/5-immune-system-boosters-to-try---unitypoint-health",
    "https://health.clevelandclinic.org/vitamins-best-boosting-immunity/",
    "https://www.cnbc.com/2022/01/30/the-4-vitamins-and-supplements-this-doctor-takes-every-day-for-a-strong-immune-system.html",
    "https://www.cnet.com/health/nutrition/best-immunity-supplements/",
    "https://www.forbes.com/health/body/best-foods-and-vitamins-for-immune-health/",
    "https://www.mindbodygreen.com/articles/supplements-for-immunity",
    "https://www.verywellfit.com/best-immune-supporting-supplements-4801560",
    "https://gilbertlab.com/immune-system/supplements-to-boost-immunity/",
    "https://www.goodrx.com/well-being/supplements-herbs/foods-vitamins-supplements-for-boost-immune-system"
  ],
  "best vitamin c supplement for immune system": [
    "https://www.forbes.com/health/body/best-vitamin-c-supplements/",
    "https://www.si.com/showcase/nutrition/best-vitamin-c-supplements",
    "https://greatist.com/health/best-vitamin-c-supplement",
    "https://www.medicalnewstoday.com/articles/best-vitamin-c-supplements",
    "https://www.verywellhealth.com/best-vitamin-c-supplements-5092579",
    "https://www.healthline.com/nutrition/best-vitamin-c-supplement",
    "https://www.amazon.com/Best-Sellers-Vitamin-C-Supplements/zgbs/hpc/3774771",
    "https://www.mindbodygreen.com/articles/best-vitamin-c-supplements",
    "https://www.active.com/nutrition/articles/best-vitamin-c-supplements",
    "https://www.discovermagazine.com/lifestyle/24-best-vitamin-c-supplements-in-2022"
  ],
  "best zinc supplement for immune system": [
    "https://www.si.com/showcase/nutrition/best-zinc-supplement",
    "https://www.cnet.com/health/nutrition/best-zinc-supplements/",
    "https://www.medicalnewstoday.com/articles/best-zinc-supplement",
    "https://www.forbes.com/health/body/best-zinc-supplements/",
    "https://www.verywellhealth.com/best-zinc-supplements-4688864",
    "https://www.healthline.com/nutrition/best-zinc-supplement",
    "https://www.outlookindia.com/outlook-spotlight/best-zinc-supplements-2023-top-5-zinc-supplements-gummies-for-testosterone-immune-system-acne-news-255454",
    "https://www.outlookindia.com/outlook-spotlight/10-best-zinc-supplements-on-the-market-news-257373",
    "https://www.amazon.com/Best-Sellers-Zinc-Mineral-Supplements/zgbs/hpc/3774511",
    "https://www.wishtv.com/sponsored/best-zinc-supplements-2023-top-zinc-product-brands-for-men-women-2/"
  ],
  "best magnesium supplement for immune system": [
    "https://www.healthline.com/nutrition/best-magnesium-supplement",
    "https://www.medicalnewstoday.com/articles/best-magnesium-supplement",
    "https://www.si.com/showcase/nutrition/best-magnesium-supplement",
    "https://www.outlookindia.com/outlook-spotlight/best-magnesium-supplements-2023-top-5-magnesium-supplements-for-sleep-anxiety-weight-loss-muscles-news-255109",
    "https://www.miamiherald.com/reviews/best-magnesium-supplement/",
    "https://www.verywellfit.com/best-magnesium-supplements-4688927",
    "https://www.livescience.com/best-magnesium-supplement",
    "https://www.active.com/nutrition/articles/best-magnesium-supplement",
    "https://thenutritioninsider.com/wellness/best-magnesium-supplements/"
  ]
}
        self.clusters = []
        self.pivot = pivot
        self.google_search_url = 'https://google.serper.dev/search'
        self.headers = {'X-API-KEY': '21c91b5b039ced96c328c5e2d6f8639437394b73','Content-Type': 'application/json' }

    # def __get_base_url(self, url_str):
    #     u = urlparse(url_str)
    #     return u.netloc
    
    def _process_search_data(self, data):
        organic_links = data.get("organic", [])
        # links = list(map(lambda x: self.__get_base_url(x["link"]), organic_links))
        links = list(map(lambda x: x["link"], organic_links))
        return links

    def _get_url(self, keyword):
        output = requests.post(url=self.google_search_url,headers=self.headers, json={
            "q":keyword
        })
        # pprint(output.json())
        urls = self._process_search_data(output.json())
        self.url_set[keyword] = urls

    def _generate_url_set(self):
        for keyword in self.keywords.Keyword:
            self._get_url(keyword=keyword)
        # pprint(self.url_set)
    def _generate_clusters(self):
        clusters=[]
        k=list(self.url_set.keys())
        for i in range(len(k)):
            l=[]
            for j in range(i+1,len(k)):
                common=len(set(self.url_set[k[i]]).intersection(set(self.url_set[k[j]])))
                print(common)
                if common>=self.pivot:
                    l.extend([k[i],k[j]])
            if l:
                clusters.append(set(l))
        self.clusters = clusters
        # print(self.clusters)
      

    def _generate_csv(self):
        for cluster in self.clusters:
            df=self.keywords.query(f'Keyword in {list(cluster)}')
            parent = df.max()
            keywords_list,volume_list=[],[]
            for i in df.to_dict(orient='records'):     
                keywords_list.append(i['Keyword'])   
                volume_list.append(i['Search volume'])  
            data = {
                    "parent_keyword": parent.Keyword,
                    "keywords":keywords_list,
                    "volume": volume_list
                }   
        out_df=pd.DataFrame(data)
        out_df.to_csv('output.csv',index=False)
      

    def process_keywords(self):
        # self._generate_url_set()
        self._generate_clusters()
        output =self._generate_csv()
        return output
    
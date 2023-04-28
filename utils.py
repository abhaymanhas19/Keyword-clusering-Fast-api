import requests
import pandas as pd
from pprint import pprint
import csv


class ProcessKeywords:
    def __init__(self, keywords_set, pivot) -> None:
        self.keywords = keywords_set
        self.url_set = {'best supplements for immune system':
                          ['https://www.healthline.com/nutrition/immune-boosting-supplements', 
                           'https://health.clevelandclinic.org/vitamins-best-boosting-immunity/', 
                           'https://www.unitypoint.org/news-and-articles/5-immune-system-boosters-to-try---unitypoint-health', 
                           'https://www.cnbc.com/2022/01/30/the-4-vitamins-and-supplements-this-doctor-takes-every-day-for-a-strong-immune-system.html', 
                           'https://gilbertlab.com/immune-system/supplements-to-boost-immunity/', 
                           'https://www.forbes.com/health/body/best-foods-and-vitamins-for-immune-health/', 
                           'https://www.mayoclinichealthsystem.org/hometown-health/speaking-of-health/fight-off-the-flu-with-nutrients', 
                           'https://www.mindbodygreen.com/articles/supplements-for-immunity',
                           'https://www.cnet.com/health/nutrition/best-immunity-supplements/', 
                           'https://www.goodrx.com/well-being/supplements-herbs/foods-vitamins-supplements-for-boost-immune-system'], 
                           'best supplement for immune system': 
                           ['https://www.healthline.com/nutrition/immune-boosting-supplements', 
                            'https://www.unitypoint.org/news-and-articles/5-immune-system-boosters-to-try---unitypoint-health',
                              'https://health.clevelandclinic.org/vitamins-best-boosting-immunity/', 
                              'https://www.cnbc.com/2022/01/30/the-4-vitamins-and-supplements-this-doctor-takes-every-day-for-a-strong-immune-system.html', 
                              'https://www.cnet.com/health/nutrition/best-immunity-supplements/', 
                              'https://www.verywellfit.com/best-immune-supporting-supplements-4801560', 
                              'https://www.mindbodygreen.com/articles/supplements-for-immunity', 
                              'https://www.forbes.com/health/body/best-foods-and-vitamins-for-immune-health/', 
                              'https://gilbertlab.com/immune-system/supplements-to-boost-immunity/', 
                              'https://www.goodrx.com/well-being/supplements-herbs/foods-vitamins-supplements-for-boost-immune-system'],
                            'best vitamin c supplement for immune system': 
                                ['https://www.forbes.com/health/body/best-vitamin-c-supplements/', 
                                 'https://greatist.com/health/best-vitamin-c-supplement', 
                                 'https://www.healthline.com/nutrition/best-vitamin-c-supplement', 
                                 'https://www.medicalnewstoday.com/articles/best-vitamin-c-supplements', 
                                 'https://www.si.com/showcase/nutrition/best-vitamin-c-supplements', 
                                 'https://www.verywellhealth.com/best-vitamin-c-supplements-5092579', 
                                 'https://www.amazon.com/Best-Sellers-Vitamin-C-Supplements/zgbs/hpc/3774771', 
                                 'https://www.mindbodygreen.com/articles/best-vitamin-c-supplements', 
                                 'https://www.active.com/nutrition/articles/best-vitamin-c-supplements', 
                                 'https://www.organicshortlist.com/organic-vitamin-c/'], 
                                'best zinc supplement for immune system': 
                                 ['https://www.si.com/showcase/nutrition/best-zinc-supplement', 
                                  'https://www.cnet.com/health/nutrition/best-zinc-supplements/', 
                                  'https://www.medicalnewstoday.com/articles/best-zinc-supplement',
                                   'https://www.forbes.com/health/body/best-zinc-supplements/', 
                                 'https://www.healthline.com/nutrition/best-zinc-supplement',
                                 'https://www.outlookindia.com/outlook-spotlight/best-zinc-supplements-2023-top-5-zinc-supplements-gummies-for-testosterone-immune-system-acne-news-255454', 
                               'https://www.amazon.com/Best-Sellers-Zinc-Mineral-Supplements/zgbs/hpc/3774511', 
                                 'https://www.verywellhealth.com/best-zinc-supplements-4688864', 
                                 'https://www.wishtv.com/sponsored/best-zinc-supplements-2023-top-zinc-product-brands-for-men-women-2/',
                                   'https://www.active.com/nutrition/articles/best-zinc-supplements'], 
                              'best magnesium supplement for immune system': 
                                        ['https://www.medicalnewstoday.com/articles/best-magnesium-supplement',
                                          'https://www.outlookindia.com/outlook-spotlight/best-magnesium-supplements-2023-top-5-magnesium-supplements-for-sleep-anxiety-weight-loss-muscles-news-255109', 
                                          'https://www.si.com/showcase/nutrition/best-magnesium-supplement', 
                                          'https://www.healthline.com/nutrition/best-magnesium-supplement', 
                                          'https://www.miamiherald.com/reviews/best-magnesium-supplement/', 
                                          'https://www.verywellfit.com/best-magnesium-supplements-4688927', 
                                          'https://www.livescience.com/best-magnesium-supplement', 
                                          'https://www.active.com/nutrition/articles/best-magnesium-supplement', 
                                          'https://www.prevention.com/food-nutrition/g35524386/best-magnesium-supplements/'], 
                             'best mushroom supplements for immune system': 
                                          ['https://www.outlookindia.com/outlook-spotlight/best-mushroom-supplements-2023-top-4-mushroom-supplements-to-support-your-health-news-243927', 'https://fullscript.com/blog/mushrooms-for-immune-health', 
                                           'https://thenutritioninsider.com/wellness/best-mushroom-supplements/', 
                                               'https://www.discovermagazine.com/lifestyle/25-best-mushroom-supplements-in-2022',
                                                'https://hpvhub.com/the-best-mushroom-supplements-in-2023-and-why-they-work/',
                                                 'https://www.healthline.com/health/food-nutrition/best-medicinal-mushrooms-to-try',
                                                    'https://ommushrooms.com/blogs/blog/best-mushroom-supplement-for-immune-system-m2', 
                                                    'https://www.rollingstone.com/product-recommendations/lifestyle/best-mushroom-supplements-1322448/', 
                                                    'https://www.timesofisrael.com/spotlight/best-mushroom-supplements-top-7-medicinal-mushroom-product-brands-ranked/'], 
                                            'best garlic supplement for immune system': 
                                            ['https://www.amazon.com/Best-Sellers-Garlic-Herbal-Supplements/zgbs/hpc/3765651', 
                                             'https://www.khon2.com/reviews/br/health-wellness-br/supplements-br/best-garlic-supplement/', 
                                             'https://totalshape.com/supplements/best-garlic-supplements/', 
                                             'https://www.livestrong.com/article/216492-the-best-garlic-capsules/', 
                                             'https://kdvr.com/reviews/br/health-wellness-br/supplements-br/best-garlic-supplement/',
                                               'https://jackedgorilla.com/best-garlic-supplements/', 'https://www.onegreenplanet.org/natural-health/boost-immune-system-12-amazing-garlic-supplements/', 'https://kyolic.com/garlic-supplements-guide/', 'https://kyolic.com/product/kyolic-formula-103/', 'https://realsport101.com/real-kit/best-garlic-supplement-allium-sativum/'], 'best fiber supplement for constipation': ['https://www.medicalnewstoday.com/articles/best-fiber-supplements', 'https://www.discovermagazine.com/lifestyle/21-best-fiber-supplements-for-constipation-in-2022', 'https://www.garagegymreviews.com/best-fiber-supplement-for-constipation', 'https://www.verywellhealth.com/best-fiber-supplements-4687136', 'https://www.outlookindia.com/outlook-spotlight/best-fiber-supplements-2023-top-5-fiber-supplements-for-weight-loss-ibs-constipation-news-274956', 'https://www.outlookindia.com/outlook-spotlight/23-best-fiber-supplements-for-constipation-news-256587', 'https://www.health.com/news/psyllium-fiber-chronic-constipation', 'https://www.sltrib.com/sponsored/2023/04/27/24-best-fiber-supplement/', 'https://www.forbes.com/health/body/best-fiber-supplements/', 'https://www.verywellfit.com/best-fiber-supplements-4165391'], 'best fiber supplements for constipation': ['https://www.medicalnewstoday.com/articles/best-fiber-supplements', 'https://www.outlookindia.com/outlook-spotlight/23-best-fiber-supplements-for-constipation-news-256587', 'https://www.outlookindia.com/outlook-spotlight/best-fiber-supplements-2023-top-5-fiber-supplements-for-weight-loss-ibs-constipation-news-274956', 'https://www.discovermagazine.com/lifestyle/21-best-fiber-supplements-for-constipation-in-2022', 'https://www.sltrib.com/sponsored/2023/04/27/24-best-fiber-supplement/', 'https://www.orlandomagazine.com/best-fiber-supplements-constipation/', 'https://www.verywellfit.com/best-fiber-supplements-4165391', 'https://www.verywellhealth.com/best-fiber-supplements-4687136', 'https://www.si.com/showcase/nutrition/best-fiber-supplement', 'https://www.garagegymreviews.com/best-fiber-supplement-for-constipation'], 'best fiber supplement for pregnancy constipation': ['https://www.outlookindia.com/outlook-spotlight/15-best-fiber-supplements-for-pregnancy-news-257851', 'https://www.whattoexpect.com/baby-products/pregnancy/products-help-constipation/', 'https://www.discovermagazine.com/lifestyle/13-best-fiber-supplements-for-pregnancy-in-2022', 'https://www.metamucil.com/en-us/articles/constipation/how-to-relieve-constipation-during-pregnancy', 'https://sunfiber.com/fiber-health-benefits/constipated-and-pregnant-heres-a-natural-way-to-find-relief/', 'https://natalist.com/products/fiber', 'https://natalist.com/blogs/learn/why-fiber-is-the-magic-pregnancy-supplement', 'https://www.livestrong.com/article/460259-safe-fiber-supplements-during-pregnancy/', 'https://www.momjunction.com/articles/amazing-benefits-of-fiber-during-pregnancy_0081238/', 'https://www.mayoclinic.org/healthy-lifestyle/pregnancy-week-by-week/expert-answers/pregnancy-constipation/faq-20058550'], 'what is the best fiber supplement for constipation': ['https://www.medicalnewstoday.com/articles/best-fiber-supplements', 'https://www.discovermagazine.com/lifestyle/21-best-fiber-supplements-for-constipation-in-2022', 'https://www.verywellhealth.com/best-fiber-supplements-4687136', 'https://www.garagegymreviews.com/best-fiber-supplement-for-constipation', 'https://www.outlookindia.com/outlook-spotlight/best-fiber-supplements-2023-top-5-fiber-supplements-for-weight-loss-ibs-constipation-news-274956', 'https://www.outlookindia.com/outlook-spotlight/23-best-fiber-supplements-for-constipation-news-256587', 'https://www.health.com/news/psyllium-fiber-chronic-constipation', 'https://www.sltrib.com/sponsored/2023/04/27/24-best-fiber-supplement/', 'https://www.verywellfit.com/best-fiber-supplements-4165391', 'https://www.forbes.com/health/body/best-fiber-supplements/'], 'best time to take fiber supplement for constipation': ['https://www.naturemade.com/blogs/health-articles/when-to-take-fiber-supplements', 'https://welltech.com/content/best-time-to-take-fiber-supplements-and-consume-dietary-fiber/', 'https://www.medicinenet.com/when_should_you_take_fiber_supplements/article.htm', 'https://www.eatingenlightenment.com/when-to-take-fiber-supplements/', 'https://drruscio.com/when-to-take-fiber-supplements/', 'https://healthreporter.com/best-time-to-take-a-fiber-supplement/', 'https://www.livestrong.com/article/287184-the-best-time-to-take-fiber-supplements/', 'https://healthyeating.sfgate.com/dosage-timing-soluble-fiber-10933.html', 'https://www.healthgrades.com/right-care/food-nutrition-and-diet/when-should-you-take-a-fiber-supplement'], 'best daily fiber supplement for constipation': ['https://www.medicalnewstoday.com/articles/best-fiber-supplements', 'https://www.discovermagazine.com/lifestyle/21-best-fiber-supplements-for-constipation-in-2022', 'https://www.garagegymreviews.com/best-fiber-supplement-for-constipation', 'https://www.sltrib.com/sponsored/2023/04/27/24-best-fiber-supplement/', 'https://www.verywellhealth.com/best-fiber-supplements-4687136', 'https://www.outlookindia.com/outlook-spotlight/best-fiber-supplements-2023-top-5-fiber-supplements-for-weight-loss-ibs-constipation-news-274956', 'https://www.outlookindia.com/outlook-spotlight/23-best-fiber-supplements-for-constipation-news-256587', 'https://www.orlandomagazine.com/best-fiber-supplements-constipation/', 'https://www.verywellfit.com/best-fiber-supplements-4165391', 'https://www.forbes.com/health/body/best-fiber-supplements/'], 'best supplements for muscle growth reddit': ['https://www.reddit.com/r/leangains/comments/bi3mfv/best_supplements_for_muscle_gains/', 'https://www.reddit.com/r/Supplements/comments/uy9uoo/best_products_for_muscle_growth/', 'https://www.reddit.com/r/bodybuilding/comments/1h2864/your_top_5_muscle_building_supps/', 'https://www.reddit.com/r/AskReddit/comments/bt2ac/dear_reddit_which_if_any_muscle_building/', 'https://www.reddit.com/r/Supplements/comments/lq1h7h/best_supplements_for_muscle_growth/', 'https://www.reddit.com/r/Supplements/comments/11dequw/best_otc_supplements_for_muscle_growthstrength/', 'https://www.reddit.com/r/Fitness/comments/3qcmn9/what_are_the_essential_supplements_for_muscle/', 'https://www.reddit.com/r/loseweightreddit/comments/j7bbe0/best_supplements_for_muscle_growth_reddit_2020/', 'https://www.reddit.com/r/naturalbodybuilding/comments/z8xrm6/are_there_any_vitamins_that_can_help_with_muscle/', 'https://www.reddit.com/r/Fitness/comments/9ou0rf/upping_the_muscle_mass_also_need_advice_on/'], 'best legal supplements for muscle growth reddit': ['https://www.reddit.com/r/Supplements/comments/zbt2e3/safe_legal_supplements_to_gain_muscle/', 'https://www.reddit.com/r/lifting/comments/aw7b3a/best_types_of_legal_supplements/', 'https://www.reddit.com/r/Supplements/comments/uy9uoo/best_products_for_muscle_growth/', 'https://www.reddit.com/r/bodybuilding/comments/1h2864/your_top_5_muscle_building_supps/', 'https://www.reddit.com/r/AskReddit/comments/bt2ac/dear_reddit_which_if_any_muscle_building/', 'https://www.reddit.com/r/leangains/comments/bi3mfv/best_supplements_for_muscle_gains/', 'https://www.reddit.com/r/Supplements/comments/11dequw/best_otc_supplements_for_muscle_growthstrength/', 'https://www.reddit.com/r/Supplements/comments/lq1h7h/best_supplements_for_muscle_growth/', 'https://www.reddit.com/r/Fitness/comments/37cz5e/is_there_anything_besides_steroids_that_you_can/', 'https://www.reddit.com/r/Supplements/comments/zm54pe/supplements_that_i_take_for_bodybuildingmuscle/']}
            


        
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
        i,j=0,100
        while i<= len(self.keywords):
            df=self.keywords.iloc[i:j]
            for keyword in df.Keyword:
                self._get_url(keyword=keyword)
            i,j=j,j+100
      
            # self._get_url(keyword=keyword)
        # pprint(self.url_set)
    def _generate_clusters(self):
        clusters=[]
        k=list(self.url_set.keys())
        for i in range(len(k)):
            l=[]
            for j in range(i+1,len(k)):
                common=set(self.url_set[k[i]]).intersection(set(self.url_set[k[j]]))
                if len(common)>=self.pivot:
                    # print(k[i],':',common)
                    l.extend([k[i],k[j]])
            if l:
                clusters.append(set(l))
        self.clusters = clusters
        # print(self.clusters)
      

    def _generate_csv(self):
        final_cluster=[]
        max_volume=[]
        for cluster in self.clusters:
            df=self.keywords.query(f'Keyword in {list(cluster)}')
            parent=df.loc[df['Search volume']==df['Search volume'].max()]
            max_volume.append(list(parent['Keyword']))
            d=df.to_dict()
            final_cluster.append(d)
            df=None
        # print(max_volume[0].Keyword)
        with open('output.csv','w') as f:
            csvWriter=csv.DictWriter(f, fieldnames=['Parent_keyword','Keyword_name','volume'] )
            csvWriter.writeheader()
            for j,k in zip(final_cluster, max_volume):
                csvWriter.writerow({"Parent_keyword":k[0]})
                for i in pd.DataFrame(j).to_dict(orient='records'):
                        data={"Keyword_name":i['Keyword'], "volume":i['Search volume']}  
                        csvWriter.writerow(data)
                        
         # keywords_list,volume_list=[],[]
        #     for i in df.to_dict(orient='records'):
        #         keywords_list.append(i['Keyword'])   
        #         volume_list.append(i['Search volume'])  
        
        #     data ={
        #            "parent_keyword":parent.Keyword,
        #             "keyword":keywords_list ,
        #             "volume":volume_list }
        #     out_df=pd.DataFrame(data)
        # out_df.to_csv('output.csv',index=False)
      

    def process_keywords(self):
        # self._generate_url_set()
        self._generate_clusters()
        output =self._generate_csv()
        return output
    
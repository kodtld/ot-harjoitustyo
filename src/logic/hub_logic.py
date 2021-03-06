from pathlib import Path
from datetime import datetime
import requests
script_location = Path("src/data_files").absolute()
cur_code_location = script_location / 'cur_code_by_a2.txt'
latest_cur_location = script_location / 'latest_cur.txt'

class HubLogic:
    """ Class in charge of logistic operations of hub page, also reads and writes to data_files.
    """
    def __init__(self):
        """ Class in charge of logistic operations of hub page, also reads and writes to data_files.

        Attributes:
        self.cur_data = placeholder for cur_code_by_a2.txt
        self.rate_data: placeholder for latest_cur.txt
        self.full_country_name: placeholder for country name
        self.alpha_2: placeholder for currency value
        self.currency_name: placeholder for currency name
        self.currency_code: placeholder for currency code
        """
        self.cur_data = {}
        self.rate_data = {}
        self.full_country_name = ""
        self.alpha_2 = ""
        self.currency_name = ""
        self.currency_code = ""

    def get_weather(self, lat, lon):
        """ Makes API call to get weather based on latitude and longitude

        Args:
            lat (float): latitude of city
            lon (float): longitude of city

        Returns:
            List of weather values (average weather, min weather, date, icon)
            for current day and 4 preceeding days.
        """
        weather_key = "10ab2060f30ce15d80acaef3490a3c36"
        weather_call = (f"https://api.openweathermap.org/data/2.5/onecall?"
         f"lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts"
         f"&appid={weather_key}&units=metric")
        request_weather = requests.get(weather_call)
        got_weather = request_weather.json()
        return_list = {}
        try:
            for i in range(0,5):
                current_weather = got_weather['daily'][i]['temp']['day']
                current_weather_min = got_weather['daily'][i]['temp']['min']
                current_date = datetime.utcfromtimestamp(
                got_weather['daily'][i]['dt']).strftime('%d-%m')
                curr_icon_for_call = (got_weather['daily'][i]['weather'][0]['icon'])
                current_iconcall = f"http://openweathermap.org/img/wn/{curr_icon_for_call}@2x.png"
                return_list[i] = []
                return_list[i] += [{'weather':current_weather,
                'weather_min':current_weather_min,
                'date':current_date,
                'icon':current_iconcall}]
        except (KeyError,IndexError):
            return_list = "None"
        return return_list

    def get_news(self,city):
        """ Makes API call to get news based on city name

        Args:
            city (str): Name of city

        Returns:
            List of (news, sources, and links) for latest top news
        """
        news_key = "pub_65366296de188355aee04321d64daafeca16"
        news_call = (f"https://newsdata.io/api/1/news?"
         f"apikey={news_key}&q={city}&language=en&category=top,world")
        request_news = requests.get(news_call)
        got_news = request_news.json()
        return_list = {}

        for i in range(0,4):
            try:
                title = got_news['results'][i]['title']
                source = got_news['results'][i]['source_id']
                link = got_news['results'][i]['link']
                return_list[i] = []
                return_list[i] = [{'title':title,'source':source,'link':link}]

            except IndexError:
                title = "Couldn't find more news..."
                source = ""
                link = ""
                return_list[i] = []
                return_list[i] = [{'title':title,'source':source,'link':link}]

        return return_list

    def get_currency(self,amount,country,currency_name,currency_code):
        """ Gets how much local currency you get with Euros (from latest_cur.txt)

        Args:
            amount (int): amount of money to be checked
            country (str): name of country
            currency_name (str): name of currency
            currency_code (str): currency code

        Returns:
            country_name, currency_name, amount that was changed,
            how much was gotten in exchange, currency_code
        """
        with open (latest_cur_location,"r",encoding="utf8") as rate_file:
            for line in rate_file:
                split_line = line.split(',')
                c_code = split_line[0]
                c_rate = split_line[1]
                self.rate_data[c_code] = c_rate

            rate = self.rate_data[currency_code]
            rate = float(rate.strip('\n'))
            ratesum = amount*rate
            return (country,currency_name,amount,ratesum,currency_code)

    def check_currency(self):
        """ Checks if last API call was made over a day ago, if so,
        makes new call and writes the result to latest_cur.txt.
        If there's no need for a new call, Pass,
        so get_currency can use old data from latest_cur.txt
        """

        current_date = datetime.today().strftime('%d-%m-%Y')
        with open (latest_cur_location,'r',encoding="utf8") as checkdate:
            latest=checkdate.readline().split(',')


            if current_date == latest[1].strip('\n'):
                pass


            else:
                curre_key = "dec91b528e3e153051ddb55d9c26f488"
                currency_call = f"http://data.fixer.io/api/latest?access_key={curre_key}&base=EUR"
                request_currency = requests.get(currency_call)
                got_currency = request_currency.json()
                with open (latest_cur_location,'w',encoding="utf8") as w_file:
                    w_file.write(f"Latest_request,{current_date}")
                    w_file.write('\n')
                    for line in got_currency['rates']:
                        rate = got_currency['rates'][line]
                        w_file.write(f"{line},{rate}")
                        w_file.write('\n')
                    w_file.write(f"ZAF,{17.01}")


    def setup_currency_code(self,country):
        """ Gets 3 letter currency code from cur_code_by_a2.txt by country name

        Args:
            country (str): name of country

        Returns:
            country name, currency name, currency code

        """
        with open(cur_code_location,'r',encoding="utf8") as r_file:
            for line in r_file:
                split_line = line.split(',')
                self.full_country_name = split_line[0]
                self.alpha_2 = split_line[1]
                self.currency_name = split_line[2]
                self.currency_code = split_line[3].strip("\n")
                self.cur_data[self.alpha_2] = [self.full_country_name,self.currency_name
                 ,self.currency_code]

        valid_country_name = self.cur_data[country][0]
        valid_currency_name = self.cur_data[country][1]
        valid_currency_code = self.cur_data[country][2]
        return (valid_country_name,valid_currency_name,valid_currency_code)


    def get_attractions(self,lat,lon,city):
        """ Makes API call to get attractions based on latitude, longitude, name of city
        Args:
            lat (float): latitude of city
            lon (float): longitude of city
            city (str): name of city

        Returns:
            List of three atrractions and their details (name, distance from center, tags, link)
        """
        attractions_key = "5ae2e3f221c38a28845f05b6a26705706c72ab688b5936158c2d8685"
        attractions_call = (f"http://api.opentripmap.com/0.1/en/places/autosuggest?"
         f"lon={lon}&lat={lat}&name={city}&radius=10000"
         f"&format=json&apikey={attractions_key}")
        request_attractions = requests.get(attractions_call)
        got_attractions = request_attractions.json()
        return_list = {}
        for i in range(0,3):
            try:
                name = got_attractions[i]['name']
                dist = got_attractions[i]['dist']*0.001
                dist = f"{dist:.1f}"
                tags = [got_attractions[i]['kinds'].split(",")]

            except IndexError:
                name = "Couldn't find an attraction"
                dist = ""
                tags = ""
                wikidata = "No available wikidata"

            try:
                wikidata = got_attractions[i]['wikidata']
                wiki_link = f"https://www.wikidata.org/wiki/{wikidata}"
            except (KeyError,IndexError):
                wikidata = "No available wikidata"
                wiki_link = "None"

            return_list[i] = []
            return_list[i] = [{'name':name,'dist':dist,'tags':tags,'link':wiki_link}]
        return return_list

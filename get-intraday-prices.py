import requests

'''
API service: Up to 5 API requests per minute and 500 requests per day
'''

APIKEY = 'LRX7WU92ANYM3KYA'
TIME_SERIES_DAILY = 'Time Series (Daily)'
OPEN = '1. open'

if __name__ == "__main__":
    with open('symbols.txt', 'r') as file:
        symbols = file.read().split('\n')
    file.closed

    # demo_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo'
    for symbol in symbols:
        my_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + symbol + '&apikey=' + APIKEY
        print(my_url)
        response = requests.get(url=my_url)
        # pprint(r.json())
        time_series_daily_json = response.json()  # dict
        day_count = 0
        prev = 0
        print_value = ''
        for date in time_series_daily_json[TIME_SERIES_DAILY]:
            open_price_str = time_series_daily_json[TIME_SERIES_DAILY][date][OPEN]
            open_price = float(open_price_str)
            if day_count >= 5:
                print("Time to invest in ::: " + symbol)
                print(print_value)
                break
            if prev > open_price:
                print("Price went up on " + date + ". Do not invest in ::: " + symbol)
                break
            day_count += 1
            print_value += date + '\t' + open_price_str + '\n'
            prev = open_price

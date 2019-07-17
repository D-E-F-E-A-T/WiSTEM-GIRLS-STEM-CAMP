import weather_custom
import schedule
import time


def get_weather():
    condition = weather_custom.get_condition("Kumasi")
    print (condition)
    
schedule.every(5).seconds.do(get_weather)
    
while True:
    schedule.run_pending()
    time.sleep(1)
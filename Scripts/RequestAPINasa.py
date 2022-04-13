import requests

#------------------------------------------------------------------------------------------------------
# ------------------------------------------ ASTEROIDS NeoWS ------------------------------------------
#------------------------------------------------------------------------------------------------------
# NeoWs (Near Earth Object Web Service) is a RESTful web service for near earth Asteroid information. 
# With NeoWs a user can: search for Asteroids based on their closest approach date to Earth, 
# lookup a specific Asteroid with its NASA JPL small body id, as well as browse the overall data-set.
#------------------------------------------------------------------------------------------------------
def AsteroidsNeoWs(token, start_date, end_date):
    
    if token and start_date and end_date:
        print(token, start_date, end_date)
    else:
        print('Invalid params. Try Again!')
        return 
    
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={token}"
    print(url)

    r = requests.get(url)
    
    data = r.json()
    
    if data:
        print(data)
    else:
        print('Nothing to print.')       


#------------------------------------------------------------------------------------------------------
# ----------------------------------- InSight: Mars Weather Service API -------------------------------
#------------------------------------------------------------------------------------------------------
# This API provides per-Sol summary data for each of the last seven available Sols (Martian Days). 
# As more data from a particular Sol are downlinked from the spacecraft (sometimes several days later), 
# these values are recalculated, and consequently may change as more data are received on Earth. 
# Additionally, please note that wind and other sensor data may not exist for certain date ranges. 
# You can check out https://mars.nasa.gov/insight/weather/ and scroll down to the 'seasonal weather report' 
# you'll see the gaps where no data exists for some sensors.
#------------------------------------------------------------------------------------------------------

def MarsWeather(token, version, feedtype):
    
    if token and version and feedtype:
        print({'token': token, 'version': version, 'feedtype': feedtype})
    else:
        print('Invalid params. Try Again!')
    
    url = f"https://api.nasa.gov/insight_weather/?api_key={token}&feedtype={feedtype}&ver={version}"
    print(url)
    
    r = requests.get(url)
    
    data = r.json()
    
    if data:
        print(data)
    else:
        print('Nothing to print.')
        

#------------------------------------------------------------------------------------------------------
# ---------------------------------------------- TechPort ---------------------------------------------
#------------------------------------------------------------------------------------------------------
# Welcome to TechPort - NASA's resource for collecting and sharing information about NASA-funded 
# technology development. Techport allows the public to discover the technologies NASA is working on 
# every day to explore space, understand the universe, and improve aeronautics. NASA is developing 
# technologies in areas such as propulsion, nanotechnology, robotics, and human health. NASA is 
# committed to making its data available and machine-readable through an Application 
# Programming Interface (API) to better serve its user communities. 
#------------------------------------------------------------------------------------------------------

def TechPort(token):
    if token:
        print(token)
    else:
        print('Invalid params. Try again')
    
    url = f"https://api.nasa.gov/techport/api/projects?api_key={token}"    
    print(url)
    
    r = requests.get(url)
    
    data = r.json()
    
    if data:
        print(data)
    else:
        print('Invalid params. Try again!')
        

def main(): 
    token = input()
    start_date = input()
    end_date = input()
    
    AsteroidsNeoWs(token, start_date, end_date)
    
    version = input()
    feedtype = input()
    
    MarsWeather(token, version, feedtype)
    
    TechPort(token)
    

if __name__ == "__main__":
    main()
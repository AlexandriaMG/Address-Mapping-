import pandas as  pd


def LatLonConverter(filename):
    'Searches for Long and Lat a file of addresses and writes the results to a CSV file'
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="my_request")
    df = pd.read_csv(filename)
    lat = []
    long = []
    dw = []
    for address in df["Address"]:
        try: 
            loc = geolocator.geocode(address)
            lat.append(loc.latitude)
            long.append(loc.longitude)
        except:
            dw.append(address)
            lat.append('')
            long.append('')
    df["Latitude"] = lat
    df["Longitude"] = long
    df.to_excel('pdLoctations.xlsx')
    



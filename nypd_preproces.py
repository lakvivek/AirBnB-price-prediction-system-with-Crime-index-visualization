import reverse_geocoder as rg
import pandas as pd

filePath = "/Users/lvivek/Downloads/NYPD_Complaint_Data_Historic.csv"


df = pd.read_csv(filePath, usecols=['CMPLNT_FR_DT','CMPLNT_FR_TM','LAW_CAT_CD','Latitude','Longitude','OFNS_DESC'])
location = []
df = df.dropna()
for index, row in df.iterrows():
        if index%100==0:
			print "processed %d rows" %(index)
	if index == 1000:
        	break
	latlng = (df['Latitude'][index],df['Longitude'][index])
        location.append(latlng)
df['location'] = location
coordinates = df['location'].tolist()
print type(coordinates[0])
results = rg.search(coordinates) # default mode = 2
addresses = []
for _ in results:
    addresses.append(_.get('name'))
df['Neighbourhood'] = addresses

print df.Neighbourhood.unique()

df.to_csv('processed_NYPD.csv', sep=',', encoding='utf-8', header=True, index=False)

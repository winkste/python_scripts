#%%
import requests
import pprint
import rki_data
from matplotlib import pyplot
import pandas as pd

#%%
res = requests.get('https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=OBJECTID%20%3E%3D%2034%20AND%20OBJECTID%20%3C%3D%2035&outFields=OBJECTID,GEN,BEZ,death_rate,cases,deaths,cases_per_100k,cases_per_population,last_update,cases7_per_100k,recovered,cases7_bl_per_100k,cases7_bl,death7_bl,cases7_lk,death7_lk,cases7_per_100k_txt,AdmUnitId&outSR=4326&f=json').json()
#res.raise_for_status()
#pprint.pprint(res)
#%%
#for key, value in res.items():
#    print(key)
#pprint.pprint(res)
#%%
features = res.get('features')
#pprint.pprint(features)

# %%
feat = features[0]
#print(type(feat))

# %%
attrib = feat.get('attributes')
pprint.pprint(attrib)
# %%
date_key = attrib.get('last_update')
new_dict = {}
new_dict[date_key] = attrib
file = open('rki_data.py', 'w')
file.write('data = ' + pprint.pformat(new_dict))
file.close()

# %%
import rki_data
date_key = attrib.get('last_update')
rki_data.data[date_key] = attrib
file = open('rki_data.py', 'w')
file.write('data =' + pprint.pformat(rki_data.data))
file.close()
pprint.pprint(rki_data.data)

#%%
date_key = update_rki_data_file()

# %%
def update_rki_data_file():
    res = requests.get('https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=OBJECTID%20%3E%3D%2034%20AND%20OBJECTID%20%3C%3D%2035&outFields=OBJECTID,GEN,BEZ,death_rate,cases,deaths,cases_per_100k,cases_per_population,last_update,cases7_per_100k,recovered,cases7_bl_per_100k,cases7_bl,death7_bl,cases7_lk,death7_lk,cases7_per_100k_txt,AdmUnitId&outSR=4326&f=json').json()
    features = res.get('features')
    feat = features[0]
    attrib = feat.get('attributes')
    #pprint.pprint(attrib)
    date_key = attrib.get('last_update')
    rki_data.data[date_key] = attrib
    file = open('rki_data.py', 'w')
    file.write('data =' + pprint.pformat(rki_data.data))
    file.close()
    pprint.pprint(rki_data.data)
    return date_key

# %%
import pandas as pd

my_panda = pd.DataFrame.from_dict(rki_data.data, orient='index')
print(my_panda)
# %%

#my_panda.plot()
my_panda.plot(subplots=True, legend=False)
pyplot.show()
# %%
my_panda['cases7_per_100k']

#%%
print(my_panda[my_panda.columns[0]])
my_panda[my_panda.columns[0]].plot()
pyplot.show()

# %%
print(my_panda['cases7_per_100k'])
my_panda['cases7_per_100k'].plot()
pyplot.show()
# %%
actual = round(rki_data.data[date_key]['cases7_per_100k'], 3)
print(actual)
#%%
import paho.mqtt.publish as publish
publish.single("std/dev999/test", str(actual), hostname="192.168.178.45", port=1883, client_id="mac_python", auth={'username':"winkste", 'password':"sw10950"})


# %%

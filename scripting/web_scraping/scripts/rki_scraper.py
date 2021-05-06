#%%
import requests
import pprint
import celle
import noh
from matplotlib import pyplot
import pandas as pd
import paho.mqtt.publish as publish
import logging
import logging.config
import datetime
import secrets



# %%
def reduce_timestamp(stamp):
    var = stamp.split(',')
    print(var[0])
    var1 = var[0].split('.')
    var1[2] = str(int(var1[2]) - 2000)
    print(var1)
    var2 = '' + var1[0] + '.' + var1[1] + '.' + var1[2]
    print(var2)
    return(var2)

def update_rki_data_file(location, dataset, api_link):
    res = requests.get(api_link).json()
    features = res.get('features')
    feat = features[0]
    attrib = feat.get('attributes')
    date_key = attrib.get('last_update')
    date_key = reduce_timestamp(date_key)
    dataset.data[date_key] = attrib
    file = open(location + '.py', 'w')
    file.write('data =' + pprint.pformat(dataset.data))
    file.close()
    return date_key

def plot_cases7_100k(location, dataset):
    x = datetime.datetime.now()
    file_name = x.strftime('%y%m%d%H%M') + '_' + location + '.png'
    my_panda = pd.DataFrame.from_dict(dataset.data, orient='index')
    my_panda['cases7_per_100k'].plot()
    pyplot.title("7 day incident per 100k for: " + location)
    pyplot.xlabel('Time')
    pyplot.ylabel('7 day incident per 100k')
    pyplot.savefig(file_name)
    pyplot.show()

def subplot_cases7_100k(loc1, data1, loc2, data2):
    x = datetime.datetime.now()
    file_name = x.strftime('%y%m%d%H%M') + '_' + loc1 + '-' + loc2 + '.png'
    p1 = pd.DataFrame.from_dict(data1.data, orient='index')
    p2 = pd.DataFrame.from_dict(data2.data, orient='index')
    fig, ax = pyplot.subplots()
    ax.plot(p1['cases7_per_100k'], 'o-')
    ax.plot(p2['cases7_per_100k'], '.-')
    legend = ax.legend([loc1, loc2], loc='best', shadow=True, fontsize='x-large')
    pyplot.savefig(file_name)
    pyplot.show()

def publish_actual_cases(topic, payload): 
    #publish.single(topic, payload, hostname="192.168.178.45", port=1883, client_id="pi_python", auth={'username':"winkste", 'password':"sw10950"})
    publish.single(topic, payload, hostname=secrets.hostname, port=secrets.port, client_id=secrets.client_id, auth=secrets.auth)
#%%
if __name__ == '__main__':
#%%
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('rki_scraper')
    
    logger.info('retrieve latest values from RKI...')
    date_key = update_rki_data_file('celle', celle, 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=OBJECTID%20%3E%3D%2034%20AND%20OBJECTID%20%3C%3D%2035&outFields=OBJECTID,GEN,BEZ,death_rate,cases,deaths,cases_per_100k,cases_per_population,last_update,cases7_per_100k,recovered,cases7_bl_per_100k,cases7_bl,death7_bl,cases7_lk,death7_lk,cases7_per_100k_txt,AdmUnitId&outSR=4326&f=json')
    update_rki_data_file('noh', noh, 'https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=OBJECTID%20%3E%3D%2055%20AND%20OBJECTID%20%3C%3D%2056&outFields=OBJECTID,GEN,BEZ,death_rate,cases,deaths,cases_per_100k,cases_per_population,last_update,cases7_per_100k,recovered,cases7_bl_per_100k,cases7_bl,death7_bl,cases7_lk,death7_lk,cases7_per_100k_txt,AdmUnitId&outSR=4326&f=json')
    
    logger.info('plot curve...')
    plot_cases7_100k('Celle', celle)
    plot_cases7_100k('Nordhorn', noh)
    subplot_cases7_100k('Celle', celle, 'Nordhorn', noh)

    logger.info('publish latest case to MQTT broker...')
    actual = str(round(celle.data[date_key]['cases7_per_100k'], 3))
    topic = "std/dev200/s/rki/ce/c7"
    publish_actual_cases(topic, actual)
    actual = str(round(noh.data[date_key]['cases7_per_100k'], 3))
    topic = "std/dev200/s/rki/noh/c7"
    publish_actual_cases(topic, actual)

#%%
    my_panda = pd.DataFrame.from_dict(celle.data, orient='index')
    p = my_panda['cases7_per_100k']
    print(type(p))

# %%
    d1 = p.to_dict()

# %%
print(d1)
# %%
print(date_key)
# %%
var = date_key.split(',')
print(var[0])
var1 = var[0].split('.')
var1[2] = str(int(var1[2]) - 2000)
print(var1)
var2 = '' + var1[0] + '.' + var1[1] + '.' + var1[2]
print(var2)
# %%

print(os.getcwd())
os.chdir("/Volumes/Macintosh HD/Users/stephan_wink")
print(os.getcwd())
print(os.path.dirname(os.path.realpath(__file__)))
#os.chdir("/var/www/html" )

# %%

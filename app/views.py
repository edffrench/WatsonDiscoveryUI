from app import app

from flask import render_template, request

from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import string

apikey ='7dOTS6YQInAIFTNG9n_kQbp-PGVhyzJ0Q0KECjzjkqnD'
watsonversion= '2019-04-30'
url = 'https://api.eu-gb.discovery.watson.cloud.ibm.com'

authenticator = IAMAuthenticator(apikey)
discovery = DiscoveryV1(
    version = watsonversion,
    authenticator = authenticator
)

discovery.set_service_url(url)

@app.route('/')
def index():
    return render_template('public/main.html')

@app.route('/search-page', methods=['GET', 'POST'])
def search():
    searchquery = request.args.get('query')
    print(searchquery)
    
    environment_id = '200a459f-203a-4f47-944b-d328f64f11fd'  
    collection_id = 'e5347b2a-5ba7-4288-911b-083d0dddd20c'

    result = discovery.query(environment_id, collection_id, natural_language_query = searchquery, count = 1)
    # dp = json.dumps(result, indent=2)
    # file = json.loads(dp)
    responsestring = str(result)
    indexstart = responsestring.find("text") + 8 
    indexend = responsestring.find("enriched_text") - 20
    responsetext = responsestring[indexstart:indexend]
    print(responsetext)
    return render_template('public/search-page.html', result_text = responsetext)

@app.route('/admin/dashboard')
def admin():
    return render_template('admin/dashboard.html')




# coding: utf-8

# In[197]:


import ssl, urllib, requests, os, sys, getpass, pprint

ssl._create_default_https_context = ssl._create_unverified_context
from arcgis.gis import GIS
from IPython.display import display
from urllib.request import urlopen
from arcgis.features.manage_data import extract_data

print("\n\nPortal-tier Authentication with LDAP - enterprise user")
gisldap = GIS(r"https://tpa-gip01-vp.tampaairport.com:7443/arcgis", "portaladmin", "YvMMUaZUmly5ZADCVLcq")
print("Logged in as: " + gisldap.properties.user.username)
token = gisldap._con.token

# Create csv file and write the header in csv
dir = r"C:\Projects\airports\tampa"
log_path = os.path.join(dir,'log.csv')
logger = open(log_path,"w")
logger.write("owner,id,title,type,url" + "\n")


# In[198]:


type(gisldap.content)


# In[199]:


Users = gisldap.users.search(query="")
Users


# In[200]:


logger.write ("title,id,itemType,owner,item,type")
for user in Users:
    userResp = gisldap.users.get(user['username'])
    searchURL = "{0}/sharing/search".format(r"https://tpa-gip01-vp.tampaairport.com:7443/arcgis")
    #print (searchURL)
    query = "owner: {0}".format(user['username'])
    params = {"q": query,"f": "pjson", "token": token}
    request = requests.get(searchURL,params=params,verify=False,timeout=5)
    rjson = request.json()
    results = rjson['results']
    
    for aresult in results:
        aresult["id"]
        #print (aresult)
        if aresult:
            logger.write (aresult['title'] + "," + aresult['id'] + "," + aresult["itemType"] + "," + aresult['owner'] + "," + aresult['item'] + "," + aresult['type'] + "\n")


# In[201]:


request.status_code


# In[202]:


#print(request.json())


# In[203]:


logger.close()


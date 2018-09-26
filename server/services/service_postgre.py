from ibmcloudenv import IBMCloudEnv
import psycopg2

url = IBMCloudEnv.getString('postgre_uri')

def getService():
    client = psycopg2.connect(url)
    return 'postgre-client', client


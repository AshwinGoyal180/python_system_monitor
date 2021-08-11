# imports
import psutil          # system monitoring library
import pandas as pd    # dataframe library
from elasticsearch import Elasticsearch   # python client for elasticsearch
from elasticsearch import helpers


# Get Process information and save them as a list
# Iterate over all running processes
def get_process_pid(listOfProcessNames):
    for proc in psutil.process_iter():
       # Get process detail as dictionary
       process_dict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
       # Append dict of process detail in list
       listOfProcessNames.append(process_dict)
    return listOfProcessNames

# convert to pandas dataframe
def construct_dataframe(processes):
    df = pd.DataFrame(processes)
    df.set_index('pid', inplace=True)
    return df

use_these_keys = ['pid', 'name', 'cpu_percent', 'memory_percent']

# filtering of pandas data frame
def filterKeys(document):
    return {key: document[key] for key in use_these_keys }


# generator to send data to elastic client by creating elastic document
def doc_generator(df):
    df_iter = df.iterrows()
    for index, document in df_iter:
        yield {
                "_index": 'stats3',
                "_id" : f"{document['pid'] + index}",
                "_source": filterKeys(document),
            }

if __name__ == "__main__":
    es_client = Elasticsearch([{'host': '192.168.1.104', 'port': 9200}], http_compress=True)
    list_of_Process = list()
    listOfProcessNames = get_process_pid(list_of_Process)

    # creating pandas dataframe
    dataFrame = construct_dataframe(listOfProcessNames)
    dataFrame = dataFrame.rename_axis('pid').reset_index()

    dataFrame_iter = dataFrame.iterrows()
    index, document = next(dataFrame_iter)

    # loading data to es using es.bulk api
    helpers.bulk(es_client, doc_generator(dataFrame))



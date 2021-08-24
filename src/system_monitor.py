# imports
import psutil          # system monitoring library
import pandas as pd    # dataframe library
from elasticsearch import Elasticsearch   # python client for elasticsearch
from elasticsearch import helpers
import datetime 
import time


# Get Process information and save them as a list
# Iterate over all running processes
def get_process_pid(listOfProcessNames, start_time, end_time, time_interval):
    for time_now in range(int(start_time), int(end_time), time_interval):
        for proc in psutil.process_iter():
            # Get process detail as dictionary
            process_dict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
            # p_time = proc.create_time()
            # p_time_h = datetime.datetime.fromtimestamp(p_time).strftime("%Y-%m-%d %H:%M:%S")
            process_dict['time'] = time_now
            listOfProcessNames.append(process_dict)
        # Append dict of process detail in list
        time.sleep(5)
    df = pd.DataFrame(listOfProcessNames)
    df.set_index('pid', inplace=True)
    return df




# # convert to pandas dataframe
# def construct_dataframe(processes):

use_these_keys = ['pid', 'name', 'cpu_percent', 'memory_percent', 'time']

# filtering of pandas data frame
def filterKeys(document):
    return {key: document[key] for key in use_these_keys }


# generator to send data to elastic client by creating elastic document
def doc_generator(df):
    df_iter = df.iterrows()
    for index, document in df_iter:
        yield {
                "_index": 'stats',
                "_id" : f"{document['pid'] + index}",
                "_source": filterKeys(document),
            }

if __name__ == "__main__":
    es_client = Elasticsearch(http_compress=True)
    list_of_Process = list()
    start_time = 0
    end_time  = 300
    time_interval = 5


    # listOfProcessNames = get_process_pid(list_of_Process, start_time, end_time, time_interval)
    # print(listOfProcessNames)

    # creating pandas dataframe
    dataFrame = get_process_pid(list_of_Process, start_time, end_time, time_interval)
    dataFrame = dataFrame.rename_axis('pid').reset_index()

    dataFrame_iter = dataFrame.iterrows()
    index, document = next(dataFrame_iter)

    # loading data to es using es.bulk api
    helpers.bulk(es_client, doc_generator(dataFrame))



# Python System Monitor

### Assignment:

1. Write a python program to read system stats from local machine ( CPU%, Memory%, …), per process(pid) and store them in Elasticsearch database.

2. Use Kibana/Redash to visualise the data in Elasticsearch.

   2.1. Timechart widget grouped by metrics ( CPU%, Memory%) collected ( For all PIDs), showing them in a single widget.

   2.2  [Bonus] List the PIDs taking more than 40% of CPU, Memory.

        You can visualise in a way that you think is the best representation of this data.
[Bonus] Do the installations of Elastic, Kibana, python application in docker.

# This repositry contains :

  1.  Python code of the application.
  2.  Data model of Elasticsearch (in a text files, under export_files dir).
  3.  Screenshot of the dashboard in Kibana (under pictures dir)
  4.  JSON export of dashboard in Kibana (export_files dir)
  5.  The DockerCompose file for Kibana and ElasticSearch only


## Project Hierarchy

```
.
├── config
│   └── requirements.pip
├── docker-compose.yml
├── Dockerfile
├── export_files
│   ├── elastic_datamodel.json
│   ├── elastic_index_settings.json
│   ├── elastic_info.txt
│   └── kibana_export.ndjson
├── pictures
│   └── kibana_dash.png
├── README.md
├── src
│   └── system_monitor.py
└── volumes
    └── data01

6 directories, 10 files
```


### Important Notes

Elastic container requires high vm memory, so need may rise to run this command

```bash
sudo sysctl -w vm.max_map_count=262144
```

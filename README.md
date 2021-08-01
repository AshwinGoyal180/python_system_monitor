# Python System Monitor

### Assignment:

1. Write a python program to read system stats from local machine ( CPU%, Memory%, …), per process(pid) and store them in Elasticsearch database.

2. Use Kibana/Redash to visualise the data in Elasticsearch.

   2.1. Timechart widget grouped by metrics ( CPU%, Memory%) collected ( For all PIDs), showing them in a single widget.

   2.2  [Bonus] List the PIDs taking more than 40% of CPU, Memory.

        You can visualise in a way that you think is the best representation of this data.
[Bonus] Do the installations of Elastic, Kibana, python application in docker.



## Project Hierarchy

```
.
├── config
│   └── requirements.pip
├── docker-compose.yml
├── Dockerfile
├── export_files
│   ├── elastic_export_kibana.txt
│   ├── elastic_export.txt
│   ├── elastic_info.txt
│   └── export.ndjson
├── pictures
│   ├── kibana_dashboard_full.png
│   └── kibana_dashboard_onewidget.png
├── README.md
├── src
│   ├── __pycache__
│   ├── stats.ipynb
│   └── system_monitor.py
└── volumes
    └── data01

7 directories, 12 files
```


### Important Notes

Elastic container requires high vm memory, so need may rise to run this command

```bash
sudo sysctl -w vm.max_map_count=262144
```

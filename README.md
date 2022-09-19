# AF_TimeTable

The script currently doesn't work.

It is easier to create several DAGs in case it's not connected

Import to be verified

DAG tbc too

Possibly should simply add __init__.py file in the folder

[Source of code](https://www.astronomer.io/guides/scheduling-in-airflow/)

[Official doc](https://airflow.apache.org/docs/apache-airflow/2.2.0/howto/timetable.html)

AF settings and params are [here](https://airflow.apache.org/docs/apache-airflow/1.10.1/scheduler.html)

In case basic scheduling is enough, cron can be used:  
```
https://crontab.guru/
```
Ex: each working day at 8h30    
```
30 8 * * 1,2,3,4,5
```

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=(r"C:\\Users\\Arpita\\Downloads\\data-engineering-2-project-e3159b5b3366.json")

import time
import io
import requests
from google.cloud import bigquery
csv_url="https://dev.azure.com/tankerkoenig/_git/tankerkoenig-data?path=/prices/2022/12"

client = bigquery.Client(r"C:\\Users\\Arpita\\Downloads\\data-engineering-2-project-e3159b5b3366.json")

table_id = "data-engineering-2-project.prices.1"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
)
response = requests.get(csv_url)
print(response.status_code)
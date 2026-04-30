# -*- coding: utf-8 -*-
"""
@author: Daniel Maeztu
http://danimaeztu.com
version: 0.2
"""

from datetime import datetime
import sqlalchemy
from sqlalchemy import text
import psutil
from jinja2 import Template
import requests
import config as cf

def logger():
    """Feed a log with system status and Dynu."""
    # Dynu Update
    try:
        r = requests.get(f'https://api.dynu.com/nic/update?username={cf.dynu_user}&password={cf.dynu_pass}', timeout=10)
        dynu = r.text
    except requests.RequestException:
        dynu = "Error_Timeout"

    # Get system stats
    now = datetime.now()
    cpu_load = psutil.cpu_percent()
    ram_load = psutil.virtual_memory().percent
    
    # Load SQL template
    with open(f'{cf.templates_path}/log_insert.sql') as f:
        tm = Template(f.read())
        
    # Render SQL
    sql = tm.render(timestamp=now.strftime('%d-%m-%Y %H:%M:%S'),
                    cpu_load=cpu_load,
                    ram_load=ram_load,
                    dynu=dynu)
                    
    connection.execute(text(sql))
    connection.commit()

# Set current time and date
now = datetime.now()

# Connection to Mysql
mysql = "mysql://{}:{}@localhost/botlpf".format(
        cf.sql_user, cf.sql_pw)
engine = sqlalchemy.create_engine(mysql)
connection = engine.connect()

# Execute Logger
logger()

connection.close()
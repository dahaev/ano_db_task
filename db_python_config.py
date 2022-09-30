import psycopg2
from main import insert_data
host = '127.0.0.1'
user = 'postgres'
password = 'Cib3jj7yz123'
name = 'ano_rsi_db'
port = 5432

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=name
)
connection.autocommit = True
try:
    with connection.cursor() as cursor:
        cursor.execute('CREATE TABLE ano_tasks('
                       'id serial PRIMARY KEY,'
                       'project_id VARCHAR(50),'
                       'project_name VARCHAR(250),'
                       'task_code VARCHAR(50),'
                       'task_name VARCHAR(250),'
                       'task_date_start DATE,'
                       'task_date_end DATE,'
                       'task_done_percent FLOAT,'
                       'task_base_start DATE,'
                       'task_base_end DATE,'
                       'task_status VARCHAR(50),'
                       'task_active VARCHAR(50),'
                       'reaper_task VARCHAR(50),'
                       'reaper_3Q2022_plan DATE,'
                       'reaper_4Q2022_plan DATE,'
                       'reaper_1Q2023_plan DATE,'
                       'reaper_2Q2023_plan DATE,'
                       'reaper_3Q2023_plan DATE'
                       ')')

except:
    print('Table ano_rsi_db already created')

with connection.cursor() as cursor:

    sql = """INSERT INTO ano_tasks(
                   project_id,
                   project_name,
                   task_code,
                   task_name,
                   task_date_start,
                   task_date_end,
                   task_done_percent,
                   task_base_end,
                   task_base_start,
                   task_status,
                   task_active,
                   reaper_task,
                   reaper_3Q2022_plan,
                   reaper_4Q2022_plan,
                   reaper_1Q2023_plan,
                   reaper_2Q2023_plan,
                   reaper_3Q2023_plan
                   ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                   """

    cursor.executemany(sql, insert_data)
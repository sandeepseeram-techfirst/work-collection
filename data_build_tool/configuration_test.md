##### Test your configuration

The debug command tests your dbt configuration and notifies you if there are any errors with the connection you just set up. 

$ dbt debug
Running with dbt=0.19.2
dbt version: 0.19.2
python version: 3.8.10
python path: /usr/bin/python3
os info: Linux-5.4.0-126-generic-x86_64-with-glibc2.29
Using profiles.yml file at /root/.dbt/profiles.yml
Using dbt_project.yml file at /root/dbt_demo/dbt_project.yml

Configuration:
  profiles.yml file [OK found and valid]
  dbt_project.yml file [OK found and valid]

Required dependencies:
 - git [OK found]

Connection:
  host: localhost
  port: 5432
  user: demo_user
  database: postgres
  schema: public
  search_path: None
  keepalives_idle: 0
  sslmode: None
  Connection test: OK connection ok

$ 
###### Install the dbt package 

pip install dbt==0.19.2 --ignore-installed; pip install --upgrade markupsafe==2.0.1 



$ dbt --version 
installed version: 0.19.2
   latest version: 1.0.0

Your version of dbt is out of date! You can find instructions for upgrading here:
https://docs.getdbt.com/docs/installation

Plugins:
  - snowflake: 0.19.2
  - bigquery: 0.19.2
  - redshift: 0.19.2
  - postgres: 0.19.2
$ 


######## Initialize a Project 

$ dbt init dbt_demo

Running with dbt=0.19.2
Creating dbt configuration folder at /root/.dbt
With sample profiles.yml for redshift

Your new dbt project "dbt_demo" was created! If this is your first time
using dbt, you'll need to set up your profiles.yml file (we've created a sample
file for you to connect to redshift) -- this file will tell dbt how
to connect to your database. You can find this file by running:

  xdg-open /root/.dbt

For more information on how to configure the profiles.yml file,
please consult the dbt documentation here:

  https://docs.getdbt.com/docs/configure-your-profile

One more thing:

Need help? Don't hesitate to reach out to us via GitHub issues or on Slack --
There's a link to our Slack group in the GitHub Readme. Happy modeling!


##############################################################

$ cd dbt_demo
$ ls
analysis  data  dbt_project.yml  macros  models  README.md  snapshots  tests
$ 
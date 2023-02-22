##### Inspect and Run the dbt Sample Models 

A model in dbt corresponds to a .sql file containing a SQL query. 

Model files in dbt look very much like regular SQL queries, but they may contain some additional instructions using Jina template syntax in the form of curly braces {{}}. For example, by using {{ ref('my_first_dbt_model') you can reference a model called my_first_dbt_model and can use it in a SQL query as you would any regular database table. 


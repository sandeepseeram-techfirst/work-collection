$ dbt run
Running with dbt=0.19.2
Found 2 models, 4 tests, 0 snapshots, 0 analyses, 138 macros, 0 operations, 0 seed files, 0 sources, 0 exposures

11:40:47 | Concurrency: 1 threads (target='dev')
11:40:47 | 
11:40:47 | 1 of 2 START table model public.my_first_dbt_model................... [RUN]
11:40:47 | 1 of 2 OK created table model public.my_first_dbt_model.............. [SELECT 2 in 0.07s]
11:40:47 | 2 of 2 START view model public.my_second_dbt_model................... [RUN]
11:40:47 | 2 of 2 OK created view model public.my_second_dbt_model.............. [CREATE VIEW in 0.06s]
11:40:47 | 
11:40:47 | Finished running 1 table model, 1 view model in 0.24s.

Completed successfully

Done. PASS=2 WARN=0 ERROR=0 SKIP=0 TOTAL=2
$ 


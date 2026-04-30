INSERT INTO performance_log (timestamp, CPU, RAM, dynu) 
VALUES (STR_TO_DATE("{{timestamp}}", '%d-%m-%Y %H:%i:%s'), "{{cpu_load}}", "{{ram_load}}", "{{dynu}}");
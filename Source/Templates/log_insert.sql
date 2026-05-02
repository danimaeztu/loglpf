INSERT INTO performance_log (timestamp, CPU, RAM, CPU_TEMP, dynu) 
VALUES (STR_TO_DATE("{{timestamp}}", '%d-%m-%Y %H:%i:%s'), "{{cpu_load}}", "{{ram_load}}", "{{cpu_temp}}", "{{dynu}}");
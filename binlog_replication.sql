SELECT variable_value as bin_log_status
FROM performance_schema.global_variables
WHERE variable_name='log_bin';

SELECT variable_value as bin_log_format
FROM performance_schema.global_variables
WHERE variable_name='binlog_format';


alter session set NLS_DATE_FORMAT = 'YYYY-MM-DD';
alter session set NLS_FIRST_DAY_OF_WEEK = 7;
alter session set NLS_TIMESTAMP_FORMAT = 'YYYY-MM-DD HH:MI:SS.FF6';
alter session set NLS_NUMERIC_CHARACTERS = '.,';
alter session set NLS_DATE_LANGUAGE = 'ENG';
alter session set QUERY_TIMEOUT = 0;
alter session set SQL_PREPROCESSOR_SCRIPT = '';

export (select * from "EXA_DB_SIZE_HOURLY" where INTERVAL_START > ADD_DAYS(systimestamp, -90) ORDER BY INTERVAL_START) into local csv file 'C:\\Users\\joas\\Desktop\\Exasol\\IGAPA\\EXA-28615\\exa_db_size_hourly.csv' WITH COLUMN NAMES;
export (select * from "EXA_DB_SIZE_DAILY"  where INTERVAL_START > ADD_DAYS(systimestamp, -90) ORDER BY INTERVAL_START) into local csv file 'C:\\Users\\joas\\Desktop\\Exasol\\IGAPA\\EXA-28615\\exa_db_size_daily.csv' WITH COLUMN NAMES;
export (select * from "EXA_MONITOR_HOURLY" where INTERVAL_START > ADD_DAYS(systimestamp, -90) ORDER BY INTERVAL_START) into local csv file 'C:\\Users\\joas\\Desktop\\Exasol\\IGAPA\\EXA-28615\\exa_monitor_hourly.csv' WITH COLUMN NAMES;
export (select * from "EXA_MONITOR_DAILY"  where INTERVAL_START > ADD_DAYS(systimestamp, -90) ORDER BY INTERVAL_START) into local csv file 'C:\\users\\joas\\Desktop\\Exasol\\IGAPA\\EXA-28615\\exa_monitor_daily.csv' WITH COLUMN NAMES;
export (select * from "EXA_USAGE_DAILY"    where INTERVAL_START > ADD_DAYS(systimestamp, -90) ORDER BY INTERVAL_START) into local csv file 'C:\\Users\\joas\\Desktop\\Exasol\\IGAPA\\EXA-28615\\exa_usage_daily.csv' WITH COLUMN NAMES;
export (select * from "EXA_USAGE_HOURLY"   where INTERVAL_START > ADD_DAYS(systimestamp, -90) ORDER BY INTERVAL_START) into local csv file 'C:\\Users\\joas\\Desktop\\Exasol\\IGAPA\\EXA-28615\\exa_usage_hourly.csv' WITH COLUMN NAMES;
export (select * from "EXA_SQL_HOURLY"     where INTERVAL_START > ADD_DAYS(systimestamp, -90) ORDER BY INTERVAL_START) into local csv file 'C:\\Users\\joas\\Desktop\\Exasol\\IGAPA\\EXA-28615\\exa_sql_hourly.csv' WITH COLUMN NAMES;
export (select * from "EXA_SQL_DAILY"      where INTERVAL_START > ADD_DAYS(systimestamp, -90) ORDER BY INTERVAL_START) into local csv file 'C:\\Users\\joas\\Desktop\\Exasol\\IGAPA\\EXA-28615\\exa_sql_daily.csv' WITH COLUMN NAMES;


export (select * from "EXA_SYSTEM_EVENTS"  where MEASURE_TIME >= (SELECT LEAST(ADD_DAYS(systimestamp, - 5), MAX(MEASURE_TIME)) FROM "EXA_SYSTEM_EVENTS" WHERE EVENT_TYPE='STARTUP')) into local csv file 'C:\\Users\\joas\\Desktop\\Exasol\\IGAPA\\exa_system_events.csv' WITH COLUMN NAMES;
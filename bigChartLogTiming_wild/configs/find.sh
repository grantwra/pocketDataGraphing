python process.py YCSB_WorkloadA_LogTimingbdb.log.gz --summary > YCSB_WorkloadA_LogTimingbdb.info
python process.py YCSB_WorkloadB_LogTimingbdb.log.gz --summary > YCSB_WorkloadB_LogTimingbdb.info
python process.py YCSB_WorkloadC_LogTimingbdb.log.gz --summary > YCSB_WorkloadC_LogTimingbdb.info
python process.py YCSB_WorkloadD_LogTimingbdb.log.gz --summary > YCSB_WorkloadD_LogTimingbdb.info
python process.py YCSB_WorkloadE_LogTimingbdb.log.gz --summary > YCSB_WorkloadE_LogTimingbdb.info
python process.py YCSB_WorkloadF_LogTimingbdb.log.gz --summary > YCSB_WorkloadF_LogTimingbdb.info
python process.py YCSB_WorkloadIA_LogTimingbdb.log.gz --summary > YCSB_WorkloadIA_LogTimingbdb.info
python process.py YCSB_WorkloadIB_LogTimingbdb.log.gz --summary > YCSB_WorkloadIB_LogTimingbdb.info
python process.py YCSB_WorkloadIC_LogTimingbdb.log.gz --summary > YCSB_WorkloadIC_LogTimingbdb.info

python readjson.py YCSB_WorkloadA_LogTimingbdb.info BDB > info/A_BDB
python readjson.py YCSB_WorkloadB_LogTimingbdb.info BDB > info/B_BDB
python readjson.py YCSB_WorkloadC_LogTimingbdb.info BDB > info/C_BDB
python readjson.py YCSB_WorkloadD_LogTimingbdb.info BDB > info/D_BDB
python readjson.py YCSB_WorkloadE_LogTimingbdb.info BDB > info/E_BDB
python readjson.py YCSB_WorkloadF_LogTimingbdb.info BDB > info/F_BDB
python readjson.py YCSB_WorkloadIA_LogTimingbdb.info BDB > info/IA_BDB
python readjson.py YCSB_WorkloadIB_LogTimingbdb.info BDB > info/IB_BDB
python readjson.py YCSB_WorkloadIC_LogTimingbdb.info BDB > info/IC_BDB

python process.py YCSB_WorkloadA_LogTimingsql.log.gz --summary > YCSB_WorkloadA_LogTimingsql.info
python process.py YCSB_WorkloadB_LogTimingsql.log.gz --summary > YCSB_WorkloadB_LogTimingsql.info
python process.py YCSB_WorkloadC_LogTimingsql.log.gz --summary > YCSB_WorkloadC_LogTimingsql.info
python process.py YCSB_WorkloadD_LogTimingsql.log.gz --summary > YCSB_WorkloadD_LogTimingsql.info
python process.py YCSB_WorkloadE_LogTimingsql.log.gz --summary > YCSB_WorkloadE_LogTimingsql.info
python process.py YCSB_WorkloadF_LogTimingsql.log.gz --summary > YCSB_WorkloadF_LogTimingsql.info
python process.py YCSB_WorkloadIA_LogTimingsql.log.gz --summary > YCSB_WorkloadIA_LogTimingsql.info
python process.py YCSB_WorkloadIB_LogTimingsql.log.gz --summary > YCSB_WorkloadIB_LogTimingsql.info
python process.py YCSB_WorkloadIC_LogTimingsql.log.gz --summary > YCSB_WorkloadIC_LogTimingsql.info

python readjson.py YCSB_WorkloadA_LogTimingsql.info SQL > info/A_SQL
python readjson.py YCSB_WorkloadB_LogTimingsql.info SQL > info/B_SQL
python readjson.py YCSB_WorkloadC_LogTimingsql.info SQL > info/C_SQL
python readjson.py YCSB_WorkloadD_LogTimingsql.info SQL > info/D_SQL
python readjson.py YCSB_WorkloadE_LogTimingsql.info SQL > info/E_SQL
python readjson.py YCSB_WorkloadF_LogTimingsql.info SQL > info/F_SQL
python readjson.py YCSB_WorkloadIA_LogTimingsql.info SQL > info/IA_SQL
python readjson.py YCSB_WorkloadIB_LogTimingsql.info SQL > info/IB_SQL
python readjson.py YCSB_WorkloadIC_LogTimingsql.info SQL > info/IC_SQL

python process.py YCSB_WorkloadA_LogTimingbdb100.log.gz --summary > YCSB_WorkloadA_LogTimingbdb100.info
python process.py YCSB_WorkloadB_LogTimingbdb100.log.gz --summary > YCSB_WorkloadB_LogTimingbdb100.info
python process.py YCSB_WorkloadC_LogTimingbdb100.log.gz --summary > YCSB_WorkloadC_LogTimingbdb100.info
python process.py YCSB_WorkloadD_LogTimingbdb100.log.gz --summary > YCSB_WorkloadD_LogTimingbdb100.info
python process.py YCSB_WorkloadE_LogTimingbdb100.log.gz --summary > YCSB_WorkloadE_LogTimingbdb100.info
python process.py YCSB_WorkloadF_LogTimingbdb100.log.gz --summary > YCSB_WorkloadF_LogTimingbdb100.info
python process.py YCSB_WorkloadIA_LogTimingbdb100.log.gz --summary > YCSB_WorkloadIA_LogTimingbdb100.info
python process.py YCSB_WorkloadIB_LogTimingbdb100.log.gz --summary > YCSB_WorkloadIB_LogTimingbdb100.info
python process.py YCSB_WorkloadIC_LogTimingbdb100.log.gz --summary > YCSB_WorkloadIC_LogTimingbdb100.info

python readjson.py YCSB_WorkloadA_LogTimingbdb100.info BDB > info/A_BDB100
python readjson.py YCSB_WorkloadB_LogTimingbdb100.info BDB > info/B_BDB100
python readjson.py YCSB_WorkloadC_LogTimingbdb100.info BDB > info/C_BDB100
python readjson.py YCSB_WorkloadD_LogTimingbdb100.info BDB > info/D_BDB100
python readjson.py YCSB_WorkloadE_LogTimingbdb100.info BDB > info/E_BDB100
python readjson.py YCSB_WorkloadF_LogTimingbdb100.info BDB > info/F_BDB100
python readjson.py YCSB_WorkloadIA_LogTimingbdb100.info BDB > info/IA_BDB100
python readjson.py YCSB_WorkloadIB_LogTimingbdb100.info BDB > info/IB_BDB100
python readjson.py YCSB_WorkloadIC_LogTimingbdb100.info BDB > info/IC_BDB100

python append_waiting.py Workload_A_BDB.waiting_on_io_summary >> info/A_BDB
python append_waiting.py Workload_B_BDB.waiting_on_io_summary >> info/B_BDB
python append_waiting.py Workload_C_BDB.waiting_on_io_summary >> info/C_BDB
python append_waiting.py Workload_D_BDB.waiting_on_io_summary >> info/D_BDB
python append_waiting.py Workload_E_BDB.waiting_on_io_summary >> info/E_BDB
python append_waiting.py Workload_F_BDB.waiting_on_io_summary >> info/F_BDB
python append_waiting.py Workload_IA_BDB.waiting_on_io_summary >> info/IA_BDB
python append_waiting.py Workload_IB_BDB.waiting_on_io_summary >> info/IB_BDB
python append_waiting.py Workload_IC_BDB.waiting_on_io_summary >> info/IC_BDB

python append_waiting.py Workload_A_BDB100.waiting_on_io_summary >> info/A_BDB100
python append_waiting.py Workload_B_BDB100.waiting_on_io_summary >> info/B_BDB100
python append_waiting.py Workload_C_BDB100.waiting_on_io_summary >> info/C_BDB100
python append_waiting.py Workload_D_BDB100.waiting_on_io_summary >> info/D_BDB100
python append_waiting.py Workload_E_BDB100.waiting_on_io_summary >> info/E_BDB100
python append_waiting.py Workload_F_BDB100.waiting_on_io_summary >> info/F_BDB100
python append_waiting.py Workload_IA_BDB100.waiting_on_io_summary >> info/IA_BDB100
python append_waiting.py Workload_IB_BDB100.waiting_on_io_summary >> info/IB_BDB100
python append_waiting.py Workload_IC_BDB100.waiting_on_io_summary >> info/IC_BDB100

python append_waiting.py Workload_A_SQL.waiting_on_io_summary >> info/A_SQL
python append_waiting.py Workload_B_SQL.waiting_on_io_summary >> info/B_SQL
python append_waiting.py Workload_C_SQL.waiting_on_io_summary >> info/C_SQL
python append_waiting.py Workload_D_SQL.waiting_on_io_summary >> info/D_SQL
python append_waiting.py Workload_E_SQL.waiting_on_io_summary >> info/E_SQL
python append_waiting.py Workload_F_SQL.waiting_on_io_summary >> info/F_SQL
python append_waiting.py Workload_IA_SQL.waiting_on_io_summary >> info/IA_SQL
python append_waiting.py Workload_IB_SQL.waiting_on_io_summary >> info/IB_SQL
python append_waiting.py Workload_IC_SQL.waiting_on_io_summary >> info/IC_SQL


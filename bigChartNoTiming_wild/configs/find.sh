python process.py YCSB_WorkloadA_NoTimingbdb.log.gz --summary > YCSB_WorkloadA_NoTimingbdb.info
python process.py YCSB_WorkloadB_NoTimingbdb.log.gz --summary > YCSB_WorkloadB_NoTimingbdb.info
python process.py YCSB_WorkloadC_NoTimingbdb.log.gz --summary > YCSB_WorkloadC_NoTimingbdb.info
python process.py YCSB_WorkloadD_NoTimingbdb.log.gz --summary > YCSB_WorkloadD_NoTimingbdb.info
python process.py YCSB_WorkloadE_NoTimingbdb.log.gz --summary > YCSB_WorkloadE_NoTimingbdb.info
python process.py YCSB_WorkloadF_NoTimingbdb.log.gz --summary > YCSB_WorkloadF_NoTimingbdb.info
python process.py YCSB_WorkloadIA_NoTimingbdb.log.gz --summary > YCSB_WorkloadIA_NoTimingbdb.info
python process.py YCSB_WorkloadIB_NoTimingbdb.log.gz --summary > YCSB_WorkloadIB_NoTimingbdb.info
python process.py YCSB_WorkloadIC_NoTimingbdb.log.gz --summary > YCSB_WorkloadIC_NoTimingbdb.info

python readjson.py YCSB_WorkloadA_NoTimingbdb.info BDB > info/A_BDB
python readjson.py YCSB_WorkloadB_NoTimingbdb.info BDB > info/B_BDB
python readjson.py YCSB_WorkloadC_NoTimingbdb.info BDB > info/C_BDB
python readjson.py YCSB_WorkloadD_NoTimingbdb.info BDB > info/D_BDB
python readjson.py YCSB_WorkloadE_NoTimingbdb.info BDB > info/E_BDB
python readjson.py YCSB_WorkloadF_NoTimingbdb.info BDB > info/F_BDB
python readjson.py YCSB_WorkloadIA_NoTimingbdb.info BDB > info/IA_BDB
python readjson.py YCSB_WorkloadIB_NoTimingbdb.info BDB > info/IB_BDB
python readjson.py YCSB_WorkloadIC_NoTimingbdb.info BDB > info/IC_BDB

python process.py YCSB_WorkloadA_NoTimingsql.log.gz --summary > YCSB_WorkloadA_NoTimingsql.info
python process.py YCSB_WorkloadB_NoTimingsql.log.gz --summary > YCSB_WorkloadB_NoTimingsql.info
python process.py YCSB_WorkloadC_NoTimingsql.log.gz --summary > YCSB_WorkloadC_NoTimingsql.info
python process.py YCSB_WorkloadD_NoTimingsql.log.gz --summary > YCSB_WorkloadD_NoTimingsql.info
python process.py YCSB_WorkloadE_NoTimingsql.log.gz --summary > YCSB_WorkloadE_NoTimingsql.info
python process.py YCSB_WorkloadF_NoTimingsql.log.gz --summary > YCSB_WorkloadF_NoTimingsql.info
python process.py YCSB_WorkloadIA_NoTimingsql.log.gz --summary > YCSB_WorkloadIA_NoTimingsql.info
python process.py YCSB_WorkloadIB_NoTimingsql.log.gz --summary > YCSB_WorkloadIB_NoTimingsql.info
python process.py YCSB_WorkloadIC_NoTimingsql.log.gz --summary > YCSB_WorkloadIC_NoTimingsql.info

python readjson.py YCSB_WorkloadA_NoTimingsql.info SQL > info/A_SQL
python readjson.py YCSB_WorkloadB_NoTimingsql.info SQL > info/B_SQL
python readjson.py YCSB_WorkloadC_NoTimingsql.info SQL > info/C_SQL
python readjson.py YCSB_WorkloadD_NoTimingsql.info SQL > info/D_SQL
python readjson.py YCSB_WorkloadE_NoTimingsql.info SQL > info/E_SQL
python readjson.py YCSB_WorkloadF_NoTimingsql.info SQL > info/F_SQL
python readjson.py YCSB_WorkloadIA_NoTimingsql.info SQL > info/IA_SQL
python readjson.py YCSB_WorkloadIB_NoTimingsql.info SQL > info/IB_SQL
python readjson.py YCSB_WorkloadIC_NoTimingsql.info SQL > info/IC_SQL

python process.py YCSB_WorkloadA_NoTimingbdb100.log.gz --summary > YCSB_WorkloadA_NoTimingbdb100.info
python process.py YCSB_WorkloadB_NoTimingbdb100.log.gz --summary > YCSB_WorkloadB_NoTimingbdb100.info
python process.py YCSB_WorkloadC_NoTimingbdb100.log.gz --summary > YCSB_WorkloadC_NoTimingbdb100.info
python process.py YCSB_WorkloadD_NoTimingbdb100.log.gz --summary > YCSB_WorkloadD_NoTimingbdb100.info
python process.py YCSB_WorkloadE_NoTimingbdb100.log.gz --summary > YCSB_WorkloadE_NoTimingbdb100.info
python process.py YCSB_WorkloadF_NoTimingbdb100.log.gz --summary > YCSB_WorkloadF_NoTimingbdb100.info
python process.py YCSB_WorkloadIA_NoTimingbdb100.log.gz --summary > YCSB_WorkloadIA_NoTimingbdb100.info
python process.py YCSB_WorkloadIB_NoTimingbdb100.log.gz --summary > YCSB_WorkloadIB_NoTimingbdb100.info
python process.py YCSB_WorkloadIC_NoTimingbdb100.log.gz --summary > YCSB_WorkloadIC_NoTimingbdb100.info

python readjson.py YCSB_WorkloadA_NoTimingbdb100.info BDB > info/A_BDB100
python readjson.py YCSB_WorkloadB_NoTimingbdb100.info BDB > info/B_BDB100
python readjson.py YCSB_WorkloadC_NoTimingbdb100.info BDB > info/C_BDB100
python readjson.py YCSB_WorkloadD_NoTimingbdb100.info BDB > info/D_BDB100
python readjson.py YCSB_WorkloadE_NoTimingbdb100.info BDB > info/E_BDB100
python readjson.py YCSB_WorkloadF_NoTimingbdb100.info BDB > info/F_BDB100
python readjson.py YCSB_WorkloadIA_NoTimingbdb100.info BDB > info/IA_BDB100
python readjson.py YCSB_WorkloadIB_NoTimingbdb100.info BDB > info/IB_BDB100
python readjson.py YCSB_WorkloadIC_NoTimingbdb100.info BDB > info/IC_BDB100

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


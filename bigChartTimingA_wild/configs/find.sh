python process.py YCSB_WorkloadA_TimingAbdb.log.gz --summary > YCSB_WorkloadA_TimingAbdb.info
python process.py YCSB_WorkloadB_TimingAbdb.log.gz --summary > YCSB_WorkloadB_TimingAbdb.info
python process.py YCSB_WorkloadC_TimingAbdb.log.gz --summary > YCSB_WorkloadC_TimingAbdb.info
python process.py YCSB_WorkloadD_TimingAbdb.log.gz --summary > YCSB_WorkloadD_TimingAbdb.info
python process.py YCSB_WorkloadE_TimingAbdb.log.gz --summary > YCSB_WorkloadE_TimingAbdb.info
python process.py YCSB_WorkloadF_TimingAbdb.log.gz --summary > YCSB_WorkloadF_TimingAbdb.info
python process.py YCSB_WorkloadIA_TimingAbdb.log.gz --summary > YCSB_WorkloadIA_TimingAbdb.info
python process.py YCSB_WorkloadIB_TimingAbdb.log.gz --summary > YCSB_WorkloadIB_TimingAbdb.info
python process.py YCSB_WorkloadIC_TimingAbdb.log.gz --summary > YCSB_WorkloadIC_TimingAbdb.info

python readjson.py YCSB_WorkloadA_TimingAbdb.info BDB > info/A_BDB
python readjson.py YCSB_WorkloadB_TimingAbdb.info BDB > info/B_BDB
python readjson.py YCSB_WorkloadC_TimingAbdb.info BDB > info/C_BDB
python readjson.py YCSB_WorkloadD_TimingAbdb.info BDB > info/D_BDB
python readjson.py YCSB_WorkloadE_TimingAbdb.info BDB > info/E_BDB
python readjson.py YCSB_WorkloadF_TimingAbdb.info BDB > info/F_BDB
python readjson.py YCSB_WorkloadIA_TimingAbdb.info BDB > info/IA_BDB
python readjson.py YCSB_WorkloadIB_TimingAbdb.info BDB > info/IB_BDB
python readjson.py YCSB_WorkloadIC_TimingAbdb.info BDB > info/IC_BDB

python process.py YCSB_WorkloadA_TimingAsql.log.gz --summary > YCSB_WorkloadA_TimingAsql.info
python process.py YCSB_WorkloadB_TimingAsql.log.gz --summary > YCSB_WorkloadB_TimingAsql.info
python process.py YCSB_WorkloadC_TimingAsql.log.gz --summary > YCSB_WorkloadC_TimingAsql.info
python process.py YCSB_WorkloadD_TimingAsql.log.gz --summary > YCSB_WorkloadD_TimingAsql.info
python process.py YCSB_WorkloadE_TimingAsql.log.gz --summary > YCSB_WorkloadE_TimingAsql.info
python process.py YCSB_WorkloadF_TimingAsql.log.gz --summary > YCSB_WorkloadF_TimingAsql.info
python process.py YCSB_WorkloadIA_TimingAsql.log.gz --summary > YCSB_WorkloadIA_TimingAsql.info
python process.py YCSB_WorkloadIB_TimingAsql.log.gz --summary > YCSB_WorkloadIB_TimingAsql.info
python process.py YCSB_WorkloadIC_TimingAsql.log.gz --summary > YCSB_WorkloadIC_TimingAsql.info

python readjson.py YCSB_WorkloadA_TimingAsql.info SQL > info/A_SQL
python readjson.py YCSB_WorkloadB_TimingAsql.info SQL > info/B_SQL
python readjson.py YCSB_WorkloadC_TimingAsql.info SQL > info/C_SQL
python readjson.py YCSB_WorkloadD_TimingAsql.info SQL > info/D_SQL
python readjson.py YCSB_WorkloadE_TimingAsql.info SQL > info/E_SQL
python readjson.py YCSB_WorkloadF_TimingAsql.info SQL > info/F_SQL
python readjson.py YCSB_WorkloadIA_TimingAsql.info SQL > info/IA_SQL
python readjson.py YCSB_WorkloadIB_TimingAsql.info SQL > info/IB_SQL
python readjson.py YCSB_WorkloadIC_TimingAsql.info SQL > info/IC_SQL

python process.py YCSB_WorkloadA_TimingAbdb100.log.gz --summary > YCSB_WorkloadA_TimingAbdb100.info
python process.py YCSB_WorkloadB_TimingAbdb100.log.gz --summary > YCSB_WorkloadB_TimingAbdb100.info
python process.py YCSB_WorkloadC_TimingAbdb100.log.gz --summary > YCSB_WorkloadC_TimingAbdb100.info
python process.py YCSB_WorkloadD_TimingAbdb100.log.gz --summary > YCSB_WorkloadD_TimingAbdb100.info
python process.py YCSB_WorkloadE_TimingAbdb100.log.gz --summary > YCSB_WorkloadE_TimingAbdb100.info
python process.py YCSB_WorkloadF_TimingAbdb100.log.gz --summary > YCSB_WorkloadF_TimingAbdb100.info
python process.py YCSB_WorkloadIA_TimingAbdb100.log.gz --summary > YCSB_WorkloadIA_TimingAbdb100.info
python process.py YCSB_WorkloadIB_TimingAbdb100.log.gz --summary > YCSB_WorkloadIB_TimingAbdb100.info
python process.py YCSB_WorkloadIC_TimingAbdb100.log.gz --summary > YCSB_WorkloadIC_TimingAbdb100.info

python readjson.py YCSB_WorkloadA_TimingAbdb100.info BDB > info/A_BDB100
python readjson.py YCSB_WorkloadB_TimingAbdb100.info BDB > info/B_BDB100
python readjson.py YCSB_WorkloadC_TimingAbdb100.info BDB > info/C_BDB100
python readjson.py YCSB_WorkloadD_TimingAbdb100.info BDB > info/D_BDB100
python readjson.py YCSB_WorkloadE_TimingAbdb100.info BDB > info/E_BDB100
python readjson.py YCSB_WorkloadF_TimingAbdb100.info BDB > info/F_BDB100
python readjson.py YCSB_WorkloadIA_TimingAbdb100.info BDB > info/IA_BDB100
python readjson.py YCSB_WorkloadIB_TimingAbdb100.info BDB > info/IB_BDB100
python readjson.py YCSB_WorkloadIC_TimingAbdb100.info BDB > info/IC_BDB100

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


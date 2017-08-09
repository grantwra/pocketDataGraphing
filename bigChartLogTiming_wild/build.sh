#cd configs/
#sh build.sh
#cd ../

python barGraph.py CPU A
python barGraph.py CPU B
python barGraph.py CPU C
python barGraph.py CPU D
python barGraph.py CPU E
python barGraph.py CPU F
python barGraph.py CPU IA
python barGraph.py CPU IB
python barGraph.py CPU IC

python barGraph.py RUN A
python barGraph.py RUN B
python barGraph.py RUN C
python barGraph.py RUN D
python barGraph.py RUN E
python barGraph.py RUN F
python barGraph.py RUN IA
python barGraph.py RUN IB
python barGraph.py RUN IC

python barGraph.py IO A
python barGraph.py IO B
python barGraph.py IO C
python barGraph.py IO D
python barGraph.py IO E
python barGraph.py IO F
python barGraph.py IO IA
python barGraph.py IO IB
python barGraph.py IO IC

python barGraphByDB.py SQL A
python barGraphByDB.py SQL B
python barGraphByDB.py SQL C
python barGraphByDB.py SQL D
python barGraphByDB.py SQL E
python barGraphByDB.py SQL F
python barGraphByDB.py SQL IA
python barGraphByDB.py SQL IB
python barGraphByDB.py SQL IC

python barGraphByDB.py BDB A
python barGraphByDB.py BDB B
python barGraphByDB.py BDB C
python barGraphByDB.py BDB D
python barGraphByDB.py BDB E
python barGraphByDB.py BDB F
python barGraphByDB.py BDB IA
python barGraphByDB.py BDB IB
python barGraphByDB.py BDB IC

python barGraphByDB.py H2 A
python barGraphByDB.py H2 B
python barGraphByDB.py H2 C
python barGraphByDB.py H2 D
python barGraphByDB.py H2 E
python barGraphByDB.py H2 F
python barGraphByDB.py H2 IA
python barGraphByDB.py H2 IB
python barGraphByDB.py H2 IC

python barGraphKV.py KV A
python barGraphKV.py KV B
python barGraphKV.py KV C
python barGraphKV.py KV D
python barGraphKV.py KV E
python barGraphKV.py KV F

python chart.py

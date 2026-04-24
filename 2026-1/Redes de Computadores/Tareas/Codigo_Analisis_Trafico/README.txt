PACK CÓDIGO BASE – ANÁLISIS DE TRÁFICO

Archivos incluidos:
- server_tcp.py: Servidor TCP simple
- client_tcp.py: Cliente TCP configurable
- pcap_analysis.py: Script de análisis básico de PCAP

Flujo recomendado:
1. Ejecutar server_tcp.py
2. Iniciar captura en Wireshark (tcp.port == 5000)
3. Ejecutar client_tcp.py
4. Detener captura y guardar PCAP
5. Ejecutar: python pcap_analysis.py captura.pcap

El análisis del PCAP es complementario y no reemplaza el análisis manual en Wireshark.

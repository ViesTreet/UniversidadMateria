"""
Análisis simple de un archivo PCAP usando Scapy.
Requiere: scapy (pip install scapy)
Uso: python pcap_analysis.py captura.pcap
"""
from scapy.all import rdpcap, TCP
import sys

pcap_file = sys.argv[1]
packets = rdpcap(pcap_file)

timestamps = [p.time for p in packets]
duration = max(timestamps) - min(timestamps)

tcp_packets = [p for p in packets if TCP in p]

total_bytes = sum(len(p) for p in tcp_packets)
throughput = total_bytes / duration if duration > 0 else 0

print("===== Estadísticas básicas del PCAP =====")
print(f"Paquetes totales: {len(packets)}")
print(f"Paquetes TCP: {len(tcp_packets)}")
print(f"Duración de la captura: {duration:.4f} s")
print(f"Bytes TCP transmitidos: {total_bytes}")
print(f"Throughput promedio: {throughput:.2f} bytes/s")
"""
Nota para el informe:
- Compare este throughput con el estimado manualmente en Wireshark.
- Relacione la duración con el comportamiento de TCP observado.
"""

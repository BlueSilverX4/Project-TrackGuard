import json
import socket
import random
import time
from datetime import datetime, timezone

WAZUH_HOST = "127.0.0.1"
WAZUH_PORT = 514

# Diverse physical security and infrastructure events
EVENTS = [
    {"event_type": "TRACK_INTRUSION", "severity": "CRITICAL", "confidence": 0.94},
    {"event_type": "BYPASS_GATE_FORCED", "severity": "HIGH", "confidence": 0.88},
    {"event_type": "THIRD_RAIL_POWER_CUT", "severity": "CRITICAL", "confidence": 1.0},
    {"event_type": "FALSE_ALARM_DEBRIS", "severity": "LOW", "confidence": 0.42}
]

LOCATIONS = ["Segment_1_Track_1", "Segment_4_Track_2", "Station_A_Turnstile_3", "Substation_B_Power_Grid"]

def send_random_event():
    event_data = random.choice(EVENTS)
    location = random.choice(LOCATIONS)
    
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "app_name": "trackguard_telemetry",
        "event_type": event_data["event_type"],
        "facility": "Subway_Line_1",
        "location": location,
        "severity": event_data["severity"],
        "cctv_confidence": event_data["confidence"],
        "status": "ALERT" if event_data["severity"] != "LOW" else "INFO"
    }
    
    json_str = json.dumps(payload)
    syslog_msg = f"<134>trackguard_telemetry: {json_str}\n"
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(syslog_msg.encode('utf-8'), (WAZUH_HOST, WAZUH_PORT))
    sock.close()
    print(f"[+] Telemetry sent: {event_data['event_type']} [{event_data['severity']}] at {location}")

if __name__ == "__main__":
    print("[*] Starting Multi-Event TrackGuard Simulation (Press Ctrl+C to stop)...")
    try:
        while True:
            send_random_event()
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n[*] Simulation stopped by user.")

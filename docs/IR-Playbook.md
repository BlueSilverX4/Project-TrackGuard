# Project TrackGuard: Incident Response Playbook
**Framework:** NIST SP 800-61 / PICERL Lifecycle  
**Target Infrastructure:** Subway Line 1 & Station Physical/Sensory Telemetry Grid

---

## 1. Preparation
* **Telemetry Sensors:** Optical beam line breaks, AI-enabled CCTV motion feeds, automated door/turnstile access logs (PACS), and SCADA third-rail power grid monitors.
* **Baseline Operations:** Normal scheduling runs between 05:00 and 01:00. Unauthorized movement outside these hours or during active service windows triggers automated triage flags.
* **SIEM Integration:** Real-time log aggregation via Rsyslog (`UDP 514`) into Wazuh and Grafana Loki.

## 2. Detection & Analysis
* **Primary Alert:** Wazuh rule matches incoming JSON syslog payloads tagged under `trackguard_telemetry`.
* **Severity Matrix:**
  * **Critical (P1):** `TRACK_INTRUSION` combined with CCTV AI verification confidence greater than 0.90, or any unauthorized `THIRD_RAIL_POWER_CUT`.
  * **High (P2):** `BYPASS_GATE_FORCED` at secure station boundaries.
  * **Low (P3):** `FALSE_ALARM_DEBRIS` (animal or track debris detection with low AI confidence).

## 3. Containment
* **Immediate Automated Actions:**
  * Signal lights for preceding train segments automatically hold at Red.
  * Dispatch SOC dashboard triggers priority audio/visual warning alarms.
* **Manual Analyst Actions:**
  * Issue remote SCADA command to isolate third-rail power on the affected track segment.
  * Lock local station access control turnstiles to prevent further unauthorized entry.

## 4. Eradication & Recovery
* **Physical Clearance Sweep:** Mobile inspection unit physically verifies the track segment is clear of humans and foreign objects.
* **Interlock Reset:** Station supervisor inputs hardware security override key.
* **Service Restoration:** Lift signal holds to Green/Auto and restore third-rail power distribution.

## 5. Lessons Learned
* Review log timelines from initial sensor break to power isolation.
* Adjust CCTV AI confidence weightings to minimize false positives caused by wind-blown debris or wildlife.

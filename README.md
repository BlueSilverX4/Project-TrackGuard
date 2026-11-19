# 🚇 Project TrackGuard: Subway Infrastructure Security & Incident Response Suite

*A Hybrid Physical-to-Cyber SOC Laboratory for Transit Infrastructure Monitoring*

## 🛡️ Project Overview

**Project TrackGuard** is a hybrid physical-to-cyber Security Operations Center (SOC) laboratory designed to simulate security monitoring and incident response within a municipal subway transit environment.

The project models a fictional subway network, **Subway Line 1**, as an enterprise IT/OT security environment. It demonstrates how physical infrastructure events—such as simulated track intrusions, unauthorized access, power disruptions, and environmental hazards—can be represented as structured security telemetry and investigated using conventional SOC workflows.

Built on **Kali Purple**, the laboratory integrates simulated physical security events with defensive monitoring technologies, including:

- **Wazuh SIEM:** Security event monitoring, correlation, and alert generation.
- **Grafana Loki:** Centralized log aggregation and querying.
- **Grafana Alloy:** Telemetry collection and forwarding.
- **Rsyslog:** Local syslog ingestion.
- **Python 3:** Custom infrastructure event and telemetry simulation.

Project TrackGuard emphasizes the intersection of physical security, cybersecurity monitoring, operational technology (OT), and incident response.

> **Safety & Scope:** This project is an isolated cybersecurity simulation. It does not connect to, control, or interact with real railway signaling equipment, public transit infrastructure, SCADA installations, or electrical distribution systems. All physical infrastructure events and responses are simulated.

---

## 🏗️ Repository Architecture

The repository is organized around selected functions of the **NIST Cybersecurity Framework (CSF)** and the incident response lifecycle described in **NIST SP 800-61**.

### Directory Structure

```text
Project-TrackGuard/
│
├── docs/
│   ├── 01-Preparation.md
│   ├── 02-Detection-Analysis.md
│   ├── 03-Containment-Eradication.md
│   ├── 04-Recovery-Lessons-Learned.md
│   ├── IR-Playbook.md
│   │
│   └── screenshots/
│       └── # Dashboard and laboratory evidence
│
├── grafana/
│   └── data/
│       └── project_trackguard-subway_soc_dashboard.json
│
├── siem-rules/
│   ├── sigma/
│   │
│   └── wazuh-rules/
│       └── trackguard_rules.xml
│
├── telemetry-generator/
│   └── mock_track_events.py
│
└── triggers/
    └── syslogs/
        └── # Simulated event and syslog data
```

### Documentation Organization

| Documentation | Purpose |
|---|---|
| `01-Preparation.md` | Laboratory preparation, assumptions, and monitoring baselines |
| `02-Detection-Analysis.md` | Event identification, validation, and severity assessment |
| `03-Containment-Eradication.md` | Simulated containment and remediation procedures |
| `04-Recovery-Lessons-Learned.md` | Recovery validation and post-incident review |
| `IR-Playbook.md` | Consolidated incident response procedures |

---

## 🔄 Physical-to-Cyber Event Mapping

Project TrackGuard translates simulated transit infrastructure events into recognizable cybersecurity incident categories.

| Simulated Physical Event | Cybersecurity Equivalent | Simulated Telemetry Source |
|---|---|---|
| Track intrusion | Unauthorized access / Intrusion Detection | Optical beam sensor, motion detection, pressure sensor |
| Access gate forced | Access control violation / IAM bypass | Physical Access Control System (PACS) event generator |
| Third-rail power interruption | Service disruption / Availability incident | Simulated SCADA power telemetry |
| Debris or wildlife detection | False-positive security alert | Simulated CCTV classification and confidence score |

### Event Classification

The laboratory uses structured telemetry to represent different event categories:

- **Unauthorized Access:** Simulated perimeter or restricted-area violations.
- **Access Control Anomalies:** Unexpected gate activity and authorization failures.
- **Infrastructure Availability:** Simulated electrical or service interruptions.
- **Environmental Events:** Debris, wildlife, and other non-malicious detections.

The objective is to demonstrate how a SOC analyst can distinguish between security incidents, operational disruptions, and false-positive alerts.

---

## 🛠️ Operational Toolchain

| Component | Technology | Function |
|---|---|---|
| Operating System | Kali Purple | Primary security laboratory platform |
| SIEM | Wazuh Manager | Event correlation and security alerting |
| Log Collection | Rsyslog | Local syslog ingestion |
| Log Aggregation | Grafana Loki | Centralized telemetry storage |
| Telemetry Forwarding | Grafana Alloy | Log collection and forwarding |
| Visualization | Grafana | SOC dashboards and monitoring |
| Simulation Engine | Python 3 | Synthetic infrastructure event generation |

### Telemetry Pipeline

```text
       PYTHON TELEMETRY GENERATOR
                  |
                  v
       SIMULATED SUBWAY EVENTS
                  |
                  v
           SYSLOG / JSON
                  |
                  v
             RSYSLOG
                  |
                  v
          LOG COLLECTION
                  |
             GRAFANA ALLOY
                  |
                  v
             GRAFANA LOKI
                  |
                  v
          GRAFANA SOC DASHBOARD
```

Wazuh provides the complementary SIEM monitoring and detection layer for supported event sources and configured rules.

---

## 🚀 Quick Start & Usage

### 1. Generate Simulated Infrastructure Events

Execute the Python telemetry generator:

```bash
python3 telemetry-generator/mock_track_events.py
```

The script generates synthetic subway infrastructure events for laboratory monitoring.

Depending on the configured implementation, events are formatted as structured JSON and forwarded to the local syslog ingestion pipeline.

### 2. Verify Log Ingestion

Monitor the TrackGuard event log:

```bash
sudo tail -f /var/log/trackguard/events.log
```

Confirm that generated events are arriving and that their timestamps, event categories, and location attributes are being parsed correctly.

### 3. Import the Grafana Dashboard

1. Open the Grafana interface:

   `http://localhost:3000`

2. Navigate to **Dashboards → Import**.

3. Upload the dashboard configuration:

   ```text
   grafana/data/project_trackguard-subway_soc_dashboard.json
   ```

4. Select the appropriate configured data source.

5. Verify that dashboard panels display the expected telemetry.

---

## 📊 SOC Dashboard & Monitoring

The TrackGuard Grafana dashboard is designed to provide a centralized overview of simulated subway infrastructure security events.

### Dashboard Components

| Dashboard Panel | Monitoring Objective |
|---|---|
| Critical Incident Counter | Track high-severity simulated alerts |
| Event Distribution | Categorize intrusion, access, power, and environmental events |
| Event Frequency | Monitor event rates and activity trends |
| Live Sensor Stream | Display incoming structured telemetry |
| Location-Based Events | Identify simulated infrastructure locations associated with alerts |

### Structured Telemetry Attributes

The monitoring pipeline can use the following JSON attributes:

| Attribute | Description |
|---|---|
| `event_type` | Classification of the simulated event |
| `location` | Simulated subway infrastructure location |
| `cctv_confidence` | Synthetic classification confidence score |
| `timestamp` | Event generation timestamp |
| `severity` | Assigned event severity |
| `source` | Originating simulated sensor or system |

**Detection consideration:** CCTV confidence scores should be treated as supporting evidence rather than definitive proof. A low-confidence detection should trigger additional validation, not automatic dismissal of a potential safety incident.

---

## 📄 Incident Response Playbook

The primary incident response documentation is maintained in:

`docs/IR-Playbook.md`

The playbook follows a structured incident response workflow informed by NIST guidance.

### 1. Preparation

- Establish simulated subway infrastructure asset inventories.
- Define event severity classifications.
- Establish normal operating-hour baselines (05:00–01:00).
- Configure telemetry collection and monitoring.
- Document escalation procedures and analyst responsibilities.

### 2. Detection & Analysis

- Identify unusual infrastructure telemetry.
- Correlate events across simulated sensor sources.
- Investigate unauthorized access and potential track intrusion events.
- Differentiate environmental detections from suspicious activity.
- Review CCTV confidence scores alongside other available evidence.
- Document findings and escalate potential life-safety incidents.

### 3. Containment & Eradication

Within the isolated simulation, demonstrate incident containment concepts through:

- Simulated restricted-area access alerts.
- Documented signal-hold scenarios.
- Simulated infrastructure isolation events.
- Review of potentially compromised access credentials.
- Validation of affected systems and telemetry sources.

No real railway signaling or electrical isolation operations are performed.

### 4. Recovery & Lessons Learned

- Validate simulated infrastructure status.
- Review event logs and incident timelines.
- Confirm that monitoring and alerting functionality has recovered.
- Document lessons learned and detection improvements.
- Update incident response procedures based on laboratory findings.

---

## 🎯 Project Objectives & Learning Outcomes

Project TrackGuard demonstrates practical defensive security concepts across several domains:

- **SOC Operations:** Event monitoring, triage, prioritization, and escalation.
- **SIEM Engineering:** Custom security rules and structured event correlation.
- **Log Management:** Centralized telemetry ingestion and visualization.
- **Physical Security Integration:** Mapping physical security events to cybersecurity incident categories.
- **OT Security Awareness:** Understanding the security implications of industrial and transportation infrastructure.
- **Incident Response:** Applying NIST-aligned investigation, containment, and recovery concepts.
- **Python Automation:** Generating repeatable synthetic security telemetry.

---

## 🔐 Safety, Limitations & Responsible Use

Project TrackGuard is intended exclusively for educational, defensive cybersecurity research and portfolio demonstration.

- All infrastructure events are simulated.
- No real transit systems or operational technology environments are accessed.
- No physical signaling, electrical switching, or railway control operations are performed.
- No real CCTV feeds or passenger information are collected.
- Automated response examples are limited to isolated laboratory simulations.
- Operational procedures are illustrative and are not substitutes for authorized transit operator safety protocols.

---

## 📌 Project Status

**Project TrackGuard — Subway Infrastructure Security & Incident Response Laboratory**

A defensive cybersecurity laboratory exploring how SOC monitoring, SIEM correlation, structured telemetry, and incident response workflows can be applied to simulated transportation infrastructure.

**Core Technologies:** Kali Purple · Wazuh · Grafana · Loki · Alloy · Rsyslog · Python

**Framework Alignment:** NIST Cybersecurity Framework · NIST SP 800-61

*Monitor the infrastructure. Investigate the anomaly. Protect the operation.*

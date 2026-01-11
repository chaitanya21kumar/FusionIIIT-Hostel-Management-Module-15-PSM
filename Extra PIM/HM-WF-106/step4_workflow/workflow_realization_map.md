# HM-WF-106 — Step 4 Workflow Realization Map

| Step | Use Case Code | Actor / Lane   | Input / Trigger                     | Process Description                                       | Output / End State                        | Business Rules  |
|------|---------------|----------------|-----------------------------------|----------------------------------------------------------|-------------------------------------------|----------------|
| 1    | HM-UC-004B    | Super Admin    | All mandatory staff assigned (D1) | Super Admin activates the hostel status                 | Hostel status updated to Active           | BR-HM-008      |
| 2    | -             | System         | Activation request received        | System updates hostel status, validates activation      | Hostel becomes operational                | BR-HM-008      |
| 3    | -             | System         | Activation completed               | System confirms hostel is ready for room allocation     | END-1: Hostel Active and Operational     | BR-HM-008      |

## Workflow Realization Map
### HM-WF-111 — Staff Report Generation Workflow

This document maps each workflow activity of HM-WF-111 to the
corresponding PIM artifacts to ensure full realization and traceability.

---

### 1. Workflow → Use Case Mapping

| Workflow Step | Use Case |
|--------------|----------|
| Create Reports | HM-UC-034 |
| Validate Report Parameters | HM-UC-034 |
| Generate Report | HM-UC-034 |
| Review Generated Report | HM-UC-034 |
| Submit Report to Super Admin | HM-UC-035 |
| Review Report | HM-UC-035 |
| Request Revision | HM-UC-035 |
| Approve Report | HM-UC-035 |
| Export Report | HM-UC-035 |
| Archive Report | HM-UC-035 |

---

### 2. Workflow → Sequence Diagram Mapping

| Workflow Step | Sequence Diagram |
|--------------|-----------------|
| Report Generation & Validation | HM-UC-034 Sequence |
| Report Review by Warden | HM-UC-034 Sequence |
| Report Submission | HM-UC-035 Sequence |
| Super Admin Review | HM-UC-035 Sequence |
| Export & Archival | HM-UC-035 Sequence |

---

### 3. Workflow → State Diagram Mapping

| Workflow Condition | Report State |
|-------------------|--------------|
| Report Created | Draft |
| Report Generated | Generated |
| Report Submitted | Submitted |
| Report Under Review | Reviewed |
| Report Requires Revision | RevisionRequired |
| Report Approved | Approved |
| Report Exported | Exported |
| Report Archived | Archived |

---

### 4. Workflow → EBC Domain Mapping

| Workflow Responsibility | Domain Element |
|------------------------|----------------|
| Parameter Selection | ReportGenerationUI |
| Parameter Validation | ReportValidationController |
| Report Generation | ReportGenerationController |
| Submission Handling | ReportSubmissionController |
| Review & Approval | ReportReviewController |
| Notification | NotificationService |
| Export | ReportExportController |
| Archival & Audit | ReportArchiveController |

---

### Conclusion

All activities and decisions of workflow HM-WF-111 are explicitly
realized through corresponding use cases, sequence diagrams,
state transitions, and EBC domain components.

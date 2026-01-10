## Step 1 — PIM Class Table (Report Generation)

| Class | Stereotype | Attributes | Methods | UC IDs |
|-----|------------|-----------|--------|-------|
| Warden | Entity | staffID, supervisedHostels | generateReport(), submitReport() | UC-034, UC-035 |
| Caretaker | Entity | staffID, assignedHostels | generateReport() | UC-034 |
| SuperAdmin | Entity | adminID | reviewReport(), approveReport() | UC-035 |
| Report | Entity | reportID, type, status, generatedAt | generate(), submit(), approve(), archive() | UC-034, UC-035 |
| ReportParameters | Entity | dateRange, filters, scope | validate() | UC-034 |
| ReportData | Entity | rawData, aggregates | process() | UC-034 |
| ArchivedReport | Entity | reportID, archivedAt | retrieve() | UC-035 |
| ReportGenerationUI | Boundary | — | collectParameters(), previewReport() | UC-034 |
| ReportPreviewUI | Boundary | — | displayReport() | UC-034 |
| ReportSubmissionUI | Boundary | — | submitReport() | UC-035 |
| ReportReviewUI | Boundary | — | displayReport(), captureFeedback() | UC-035 |
| ReportValidationController | Control | — | validateParameters() | UC-034 |
| ReportGenerationController | Control | — | generateReport() | UC-034 |
| ReportSubmissionController | Control | — | submitReport() | UC-035 |
| ReportReviewController | Control | — | reviewReport() | UC-035 |
| ReportExportController | Control | — | exportPDF(), exportExcel() | UC-035 |
| ReportArchiveController | Control | — | archiveReport(), logAccess() | UC-035 |
| NotificationService | Control | — | notifySuperAdmin() | UC-035 |

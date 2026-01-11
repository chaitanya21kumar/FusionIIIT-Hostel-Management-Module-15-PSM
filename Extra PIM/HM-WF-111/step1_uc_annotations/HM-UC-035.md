## UC: HM-UC-035 — Submit and Review Reports

### Annotated Flow (EBC)

M1. Warden submits generated report  
(Boundary: ReportSubmissionUI)

M2. System validates submission  
(Control: ReportSubmissionController)  
[BR-HM-045]

M3. System records submission and updates status  
(Control) → Report.status = Submitted  
(Entity)

M4. System notifies Super Admin  
(Control: NotificationService)

M5. Super Admin reviews report  
(Boundary: ReportReviewUI)

M6. Super Admin approves / requests revision  
(Control: ReportReviewController)  
[BR-HM-046]

M7. If approved, Super Admin downloads report  
(Control: ReportExportController)  
[BR-HM-050]

M8. System archives report and logs access  
(Control: ReportArchiveController)

Postcondition: Report reviewed, archived, exported

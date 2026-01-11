## UC: HM-UC-034 — Create Reports

### Annotated Flow (EBC)

M1. Staff opens Report Generation page  
(Boundary: ReportGenerationUI)

M2. Staff selects report type, date range, filters  
(Boundary) → ReportParameters  
(Entity)

M3. System validates parameters  
(Control: ReportValidationController)  
[BR-HM-040, BR-HM-043]

M4. System retrieves and aggregates data  
(Control: ReportGenerationController) →  
ReportData  
(Entity)

M5. System generates report with charts and statistics  
(Control) → Report  
(Entity)  
[BR-HM-044]

M6. System displays generated report  
(Boundary: ReportPreviewUI)

M7. Staff reviews report  
(Result: Report in Generated state)

Postcondition: Report ready for submission

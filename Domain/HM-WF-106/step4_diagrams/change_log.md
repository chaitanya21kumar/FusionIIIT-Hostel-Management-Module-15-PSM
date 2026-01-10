# change_log.md

## Workflow-6 artifacts (fixed for mermaidchart.com)

Files and descriptions:
- HM-UC-005_EBC.png — Detailed Generate Leave Report flowchart (validation, aggregation, export, scheduling).
- initial_merged_EBC.png — Merged leave flows: submit, process, attendance update, reporting, archive.
- HM-UC-032.png — Create and Publish Notice lifecycle with attachments, target selection, priority, auto-archive.
- HM-UC-033.png — Student notice board: view, filter, download, archive, search and report.
- updated_domain_EBC.png — Domain mapping (hostel staffing, notices, leave, vacation) with BR callouts.
- final_domain_EBC.png — Final domain view including notifications & audit services.

## Notes on fixes
- Replaced `\n` with `<br>` inside quoted labels to avoid parser issues.
- Removed unquoted parentheses and some special characters from labels.
- Kept `graph LR` and `subgraph` groups to preserve the long, detailed layout you requested.

## Next steps
- Paste each snippet into mermaidchart.com as a separate project. They should render cleanly.
- If you still get an error, copy the exact error message and paste it here and I will patch that specific line immediately.

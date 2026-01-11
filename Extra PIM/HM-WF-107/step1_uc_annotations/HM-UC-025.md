# HM-UC-025 — Review Hostel Security Status

## Primary Actor
Warden / Security Supervisor

## Stakeholders
- Hostel Management
- Students
- Security Team

## Preconditions
- User authenticated
- Security data available

## Trigger
User requests security overview

## Main Success Scenario
1. User opens DashboardView
2. Aggregator collects IncidentReport and GuardCheckIn data
3. DashboardView displays security status
4. User requests report export
5. ReportService generates file

## Alternate Flows
A1. No data available → show empty state  
A2. Export fails → retry or cancel  

## Postconditions
- Security status viewed
- Report generated if requested

## Business Rules
BR-HM-012 Access control  
BR-HM-027 Incident monitoring  

## Entities
IncidentReport, GuardCheckIn

## Boundaries
DashboardView, ReportGenerator

## Controls
Aggregator, ReportService

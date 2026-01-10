# HM-UC-038: Apply for Extended Stay

**Trigger:** Student navigates to **"Extended Stay" section** [Boundary] and clicks **"Apply for Extended Stay"** [User Action].

**Main Flow:**
1. Student clicks 'Apply for Extended Stay' button.
2. System displays available **vacation periods** [Entity: VacationPeriod.name, VacationPeriod.startDate, VacationPeriod.endDate].
3. Student selects **vacation period** from list [Entity: ExtendedStayApplication.vacationPeriod].
4. Student enters **extended stay start date** [Entity: ExtendedStayApplication.startDate].
5. Student enters **extended stay end date** [Entity: ExtendedStayApplication.endDate].
6. Student provides detailed **reason for extended stay request** [Entity: ExtendedStayApplication.reason].
7. Student uploads **faculty authorization/approval letter** [Entity: AuthorizationDocument.file].
8. System validates document **format and size** [Entity: AuthorizationDocument.metadata].
9. System calculates **estimated charges** based on duration [Entity: StayCharge.estimatedAmount].
10. System displays **charge breakdown (per-day rate × number of days)** [Entity: StayCharge.breakdown].
11. Student reviews charges and acknowledges extra fees.
12. Student checks acknowledgment checkbox for terms and conditions.
13. Student clicks 'Submit Application'.
14. System validates complete form.
15. System records extended stay application with **status='Pending'** [Entity: ExtendedStayApplication.status].
16. System sends notification to **Caretaker/Warden** [Actor].
17. System displays confirmation message with **application ID** [Entity: ExtendedStayApplication.applicationId].
18. System sends acknowledgment notification to student.
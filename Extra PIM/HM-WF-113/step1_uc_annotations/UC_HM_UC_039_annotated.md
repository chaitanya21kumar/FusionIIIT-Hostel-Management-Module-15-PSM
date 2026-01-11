# HM-UC-039: Review and Approve Application

**Trigger:** Caretaker/Warden receives notification... and navigates to **"Extended Stay Management" section** [Boundary].

**Main Flow:**
1. Caretaker/Warden accesses **'Pending Extended Stay Applications' dashboard** [Boundary].
2. System displays list of pending applications.
3. Caretaker/Warden selects an application to review.
4. System displays complete application details: **Student information** [Entity: Student], **Requested vacation period** [Entity: ExtendedStayApplication.dates], **Reason** [Entity: ExtendedStayApplication.reason], **Uploaded faculty authorization** [Entity: AuthorizationDocument], **Calculated charges** [Entity: StayCharge].
5. Caretaker/Warden views and verifies **faculty authorization document** [Entity: AuthorizationDocument].
6. Caretaker/Warden checks **authorization authenticity** (signature, date, authorized faculty).
7. System displays **room availability** during requested vacation period [Entity: Room.availabilityStatus].
8. Caretaker/Warden reviews **student's hostel behavior record**: **Fine history** [Entity: Student.fineHistory], **Disciplinary actions** [Entity: Student.disciplinaryRecord], **Complaint history** [Entity: Student.complaintHistory], **Attendance record** [Entity: Student.attendance].
9. Caretaker/Warden makes decision:
    * If Approving:
10. Caretaker/Warden clicks 'Approve Application'.
11. System prompts for **approval comments** [Entity: ExtendedStayApplication.approvalComments].
12. Caretaker/Warden confirms approval.
13. System updates application **status to 'Approved'** [Entity: ExtendedStayApplication.status].
14. System sends approval notification to student with stay details and charges.
    * If Rejecting:
    * Caretaker enters **rejection reason** [Entity: ExtendedStayApplication.rejectionReason].
    * System updates application **status to 'Rejected'** [Entity: ExtendedStayApplication.status].
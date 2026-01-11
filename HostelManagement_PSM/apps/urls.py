"""
urls.py
Logical Endpoint Mapping — Hostel Management PSM
"""

URLS = {
    # WF-101
    "POST /leave/apply": "submit_leave_view",

    # WF-102
    "POST /complaint/submit": "submit_complaint_view",

    # WF-105
    "POST /fine/impose": "impose_fine_view",

    # WF-110
    "POST /notice/create": "create_notice_view",

    # WF-111
    "POST /report/generate": "generate_report_view",
    
    # ======================================================
    # ======================================================
    
    # WF-103 — Room Allotment
    "POST /room/allot": "allot_room_view",
    
    # WF-104 — Room Change
    "POST /room/change/request": "request_room_change_view",
    "POST /room/change/approve": "approve_room_change_view",
    
    # WF-106 — Hostel Setup & Staffing
    "POST /hostel/create": "create_hostel_view",
    "POST /hostel/staff/assign": "assign_staff_view",
    
    # WF-107 — Security & Guard Management
    "POST /security/guard/assign": "assign_guard_view",
    "POST /security/incident/log": "log_incident_view",
    
    # WF-108 — Visitor Management
    "POST /visitor/request": "request_visit_view",
    "POST /visitor/entry/log": "log_visit_entry_view",
    "POST /visitor/exit/log": "log_visit_exit_view",
    
    # WF-109 — Room Vacation
    "POST /room/vacation/request": "request_vacation_view",
    "POST /room/vacation/clearance": "verify_clearance_view",
    
    # WF-112 — Guest Room Booking
    "POST /guestroom/request": "request_guest_room_view",
    "POST /guestroom/approve": "approve_guest_booking_view",
    "POST /guestroom/checkin": "checkin_guest_view",
    "POST /guestroom/checkout": "checkout_guest_view",
    
    # WF-113 — Extended Stay
    "POST /extendedstay/apply": "apply_extended_stay_view",
    "POST /extendedstay/review": "review_extended_stay_view",
    "POST /extendedstay/payment": "process_stay_payment_view",
}

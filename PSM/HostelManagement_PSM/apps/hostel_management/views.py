"""
views.py
Boundary Layer — Hostel Management PSM
"""

from datetime import date, datetime

from .services import (
    apply_leave,
    submit_complaint,
    impose_fine,
    create_notice,
    generate_report,
    # PHASE 2: Additional service imports
    allot_room, request_room_change, approve_room_change,
    create_hostel, assign_staff,
    assign_guard, log_incident,
    request_visit, log_visit,
    request_vacation, perform_clearance,
    request_guest_room, approve_guest_booking, checkin_guest, checkout_guest,
    apply_extended_stay, review_extended_stay, process_stay_payment
)
from .serializers import (
    leave_request_to_dict,
    complaint_to_dict,
    fine_to_dict,
    notice_to_dict,
    report_to_dict,
    # PHASE 2: Additional serializer imports
    room_allocation_to_dict, room_change_request_to_dict,
    hostel_to_dict, staff_assignment_to_dict,
    guard_to_dict, incident_report_to_dict,
    visit_request_to_dict, visit_log_to_dict,
    room_vacation_request_to_dict, clearance_record_to_dict,
    guest_room_booking_to_dict, extended_stay_application_to_dict
)


# -------------------------
# WF-101 — Leave Boundary
# -------------------------

def submit_leave_view(payload: dict):
    leave = apply_leave(
        student_id=payload["student_id"],
        hostel_status=payload["hostel_status"],
        start_date=payload["start_date"],
        end_date=payload["end_date"],
        reason=payload["reason"],
        docs_attached=payload["docs_attached"],
    )
    return leave_request_to_dict(leave)


# -------------------------
# WF-102 — Complaint Boundary
# -------------------------

def submit_complaint_view(payload: dict):
    complaint = submit_complaint(
        student_id=payload["student_id"],
        hostel_status=payload["hostel_status"],
        category=payload["category"],
        description=payload["description"],
    )
    return complaint_to_dict(complaint)


# -------------------------
# WF-105 — Fine Boundary
# -------------------------

def impose_fine_view(payload: dict):
    fine = impose_fine(
        role=payload["role"],
        student_id=payload["student_id"],
        amount=payload["amount"],
        reason=payload["reason"],
    )
    return fine_to_dict(fine)


# -------------------------
# WF-110 — Notice Boundary
# -------------------------

def create_notice_view(payload: dict):
    notice = create_notice(
        title=payload["title"],
        description=payload["description"],
        priority=payload["priority"],
        title_len=len(payload["title"]),
        desc_len=len(payload["description"]),
    )
    return notice_to_dict(notice)


# -------------------------
# WF-111 — Report Boundary
# -------------------------

def generate_report_view(payload: dict):
    report = generate_report(
        role=payload["role"],
        report_type=payload["report_type"],
        params=payload["params"],
    )
    return report_to_dict(report)


# ======================================================
# PHASE 2: ADDITIONAL BOUNDARY LAYER VIEWS
# ======================================================

# -------------------------
# WF-103 — Room Allotment Boundary
# -------------------------

def allot_room_view(payload: dict):
    """Allocate room to student"""
    allocation = allot_room(
        role=payload["role"],
        window_status=payload["window_status"],
        room=payload["room"],
        student_id=payload["student_id"],
    )
    return room_allocation_to_dict(allocation)


# -------------------------
# WF-104 — Room Change Boundary
# -------------------------

def request_room_change_view(payload: dict):
    """Submit room change request"""
    request = request_room_change(
        student_id=payload["student_id"],
        reason=payload["reason"],
    )
    return room_change_request_to_dict(request)


def approve_room_change_view(payload: dict):
    """Approve room change request"""
    history = approve_room_change(
        req=payload["request"],
        caretaker_ok=payload["caretaker_approved"],
        warden_ok=payload["warden_approved"],
        old_room=payload["old_room"],
        new_room=payload["new_room"],
    )
    return {"student_id": history.student_id, "old_room": history.old_room, "new_room": history.new_room}


# -------------------------
# WF-106 — Hostel Setup Boundary
# -------------------------

def create_hostel_view(payload: dict):
    """Create new hostel"""
    hostel = create_hostel(
        admin_id=payload["admin_id"],
        name=payload["name"],
        hostel_type=payload["hostel_type"],
        address=payload["address"],
        capacity=payload["capacity"],
    )
    return hostel_to_dict(hostel)


def assign_staff_view(payload: dict):
    """Assign staff to hostel"""
    assignment = assign_staff(
        staff_id=payload["staff_id"],
        hostel_id=payload["hostel_id"],
        role=payload["role"],
    )
    return staff_assignment_to_dict(assignment)


# -------------------------
# WF-107 — Security/Guard Boundary
# -------------------------

def assign_guard_view(payload: dict):
    """Assign guard"""
    guard = assign_guard(
        guard_id=payload["guard_id"],
        name=payload["name"],
        phone=payload["phone"],
    )
    return guard_to_dict(guard)


def log_incident_view(payload: dict):
    """Log security incident"""
    incident = log_incident(
        description=payload["description"],
        severity=payload["severity"],
    )
    return incident_report_to_dict(incident)


# -------------------------
# WF-108 — Visitor Management Boundary
# -------------------------

def request_visit_view(payload: dict):
    """Request visitor entry"""
    visit_request = request_visit(
        visit_date=payload["visit_date"],
    )
    return visit_request_to_dict(visit_request)


def log_visit_entry_view(payload: dict):
    """Log visitor entry"""
    visit_log = log_visit(
        entry_time=payload["entry_time"],
        exit_time=None,
    )
    return visit_log_to_dict(visit_log)


def log_visit_exit_view(payload: dict):
    """Log visitor exit"""
    visit_log = log_visit(
        entry_time=payload["entry_time"],
        exit_time=payload["exit_time"],
    )
    return visit_log_to_dict(visit_log)


# -------------------------
# WF-109 — Room Vacation Boundary
# -------------------------

def request_vacation_view(payload: dict):
    """Request room vacation"""
    vacation_request = request_vacation(
        student_id=payload["student_id"],
        vacation_date=payload["vacation_date"],
    )
    return room_vacation_request_to_dict(vacation_request)


def verify_clearance_view(payload: dict):
    """Verify and perform clearance"""
    clearance = perform_clearance(
        student_id=payload["student_id"],
        cleared_by=payload["cleared_by"],
        pending_dues=payload["pending_dues"],
        inventory_clear=payload["inventory_clear"],
    )
    return clearance_record_to_dict(clearance)


# -------------------------
# WF-112 — Guest Room Booking Boundary
# -------------------------

def request_guest_room_view(payload: dict):
    """Request guest room booking"""
    booking = request_guest_room(
        student_id=payload["student_id"],
    )
    return guest_room_booking_to_dict(booking)


def approve_guest_booking_view(payload: dict):
    """Approve guest room booking"""
    booking = approve_guest_booking(
        booking=payload["booking"],
        role=payload["role"],
        hostel_status=payload["hostel_status"],
        outstanding_fines=payload["outstanding_fines"],
        disciplinary_status=payload["disciplinary_status"],
    )
    return guest_room_booking_to_dict(booking)


def checkin_guest_view(payload: dict):
    """Check in guest"""
    booking = checkin_guest(
        booking=payload["booking"],
        guest_identity=payload["guest_identity"],
    )
    return guest_room_booking_to_dict(booking)


def checkout_guest_view(payload: dict):
    """Check out guest"""
    booking, fine = checkout_guest(
        booking=payload["booking"],
        inspection=payload["inspection"],
    )
    result = guest_room_booking_to_dict(booking)
    if fine:
        result["fine"] = fine_to_dict(fine)
    return result


# -------------------------
# WF-113 — Extended Stay Boundary
# -------------------------

def apply_extended_stay_view(payload: dict):
    """Apply for extended stay"""
    application = apply_extended_stay(
        student_id=payload["student_id"],
        reason=payload["reason"],
        academic_standing=payload["academic_standing"],
        faculty_ok=payload["faculty_approval"],
    )
    return extended_stay_application_to_dict(application)


def review_extended_stay_view(payload: dict):
    """Review extended stay application"""
    application = review_extended_stay(
        application=payload["application"],
        role=payload["role"],
        approved=payload["approved"],
        remarks=payload.get("remarks"),
    )
    return extended_stay_application_to_dict(application)


def process_stay_payment_view(payload: dict):
    """Process extended stay payment"""
    application = process_stay_payment(
        application=payload["application"],
        payment_received=payload["payment_received"],
        payment_date=payload["payment_date"],
    )
    return extended_stay_application_to_dict(application)

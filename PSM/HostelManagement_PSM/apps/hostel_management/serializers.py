"""
serializers.py
DTO Mappers — Hostel Management PSM
"""

def leave_request_to_dict(leave):
    return {
        "request_id": leave.request_id,
        "student_id": leave.student_id,
        "start_date": leave.start_date,
        "end_date": leave.end_date,
        "status": leave.status,
        "remarks": leave.remarks,
    }


def complaint_to_dict(complaint):
    return {
        "complaint_id": complaint.complaint_id,
        "student_id": complaint.student_id,
        "category": complaint.category,
        "description": complaint.description,
        "status": complaint.status,
    }


def fine_to_dict(fine):
    return {
        "fine_id": fine.fine_id,
        "student_id": fine.student_id,
        "amount": fine.amount,
        "reason": fine.reason,
        "status": fine.status,
    }


def notice_to_dict(notice):
    return {
        "notice_id": notice.notice_id,
        "title": notice.title,
        "description": notice.description,
        "priority": notice.priority,
        "status": notice.status,
    }


def report_to_dict(report):
    return {
        "report_id": report.report_id,
        "type": report.type,
        "status": report.status,
        "generated_at": report.generated_at,
    }


# ======================================================
# PHASE 2: ADDITIONAL SERIALIZERS
# ======================================================

# -------------------------
# WF-103 — Room Allotment Serializers
# -------------------------

def room_to_dict(room):
    return {
        "room_id": room.room_id,
        "capacity": room.capacity,
        "occupancy": room.occupancy,
        "hostel_id": room.hostel_id,
        "room_number": room.room_number,
        "room_type": room.room_type,
        "floor": room.floor,
    }


def room_allocation_to_dict(allocation):
    return {
        "allocation_id": allocation.allocation_id,
        "student_id": allocation.student_id,
        "room_id": allocation.room_id,
        "allocated_at": allocation.allocated_at,
    }


# -------------------------
# WF-104 — Room Change Serializers
# -------------------------

def room_change_request_to_dict(request):
    return {
        "request_id": request.request_id,
        "student_id": request.student_id,
        "reason": request.reason,
        "status": request.status,
    }


def room_assignment_history_to_dict(history):
    return {
        "student_id": history.student_id,
        "old_room": history.old_room,
        "new_room": history.new_room,
        "changed_at": history.changed_at,
    }


# -------------------------
# WF-106 — Hostel Setup Serializers
# -------------------------

def hostel_to_dict(hostel):
    return {
        "hostel_id": hostel.hostel_id,
        "name": hostel.name,
        "type": hostel.type,
        "address": hostel.address,
        "capacity": hostel.capacity,
        "status": hostel.status,
        "created_at": hostel.created_at,
    }


def staff_assignment_to_dict(assignment):
    return {
        "assignment_id": assignment.assignment_id,
        "staff_id": assignment.staff_id,
        "hostel_id": assignment.hostel_id,
        "role": assignment.role,
        "assigned_at": assignment.assigned_at,
    }


# -------------------------
# WF-107 — Security/Guard Serializers
# -------------------------

def guard_to_dict(guard):
    return {
        "guard_id": guard.guard_id,
        "name": guard.name,
        "phone": guard.phone,
        "status": guard.status,
    }


def shift_assignment_to_dict(shift):
    return {
        "shift_id": shift.shift_id,
        "guard_id": shift.guard_id,
        "start_time": shift.start_time,
        "end_time": shift.end_time,
        "location": shift.location,
        "status": shift.status,
    }


def incident_report_to_dict(incident):
    return {
        "report_id": incident.report_id,
        "description": incident.description,
        "severity": incident.severity,
        "status": incident.status,
        "logged_at": incident.logged_at,
    }


# -------------------------
# WF-108 — Visitor Management Serializers
# -------------------------

def visitor_to_dict(visitor):
    return {
        "name": visitor.name,
        "phone": visitor.phone,
    }


def visit_request_to_dict(visit_request):
    return {
        "request_id": visit_request.request_id,
        "visit_date": visit_request.visit_date,
        "status": visit_request.status,
    }


def visit_log_to_dict(visit_log):
    return {
        "log_id": visit_log.log_id,
        "entry_time": visit_log.entry_time,
        "exit_time": visit_log.exit_time,
    }


# -------------------------
# WF-109 — Room Vacation Serializers
# -------------------------

def room_vacation_request_to_dict(request):
    return {
        "request_id": request.request_id,
        "student_id": request.student_id,
        "vacation_date": request.vacation_date,
        "status": request.status,
    }


def clearance_record_to_dict(clearance):
    return {
        "record_id": clearance.record_id,
        "student_id": clearance.student_id,
        "cleared_by": clearance.cleared_by,
        "cleared_at": clearance.cleared_at,
    }


# -------------------------
# WF-112 — Guest Room Serializers
# -------------------------

def guest_room_to_dict(guest_room):
    return {
        "room_id": guest_room.room_id,
        "hostel_id": guest_room.hostel_id,
        "status": guest_room.status,
    }


def guest_room_booking_to_dict(booking):
    return {
        "booking_id": booking.booking_id,
        "student_id": booking.student_id,
        "status": booking.status,
        "check_in_date": booking.check_in_date,
        "check_out_date": booking.check_out_date,
        "guest_name": booking.guest_name,
        "guest_contact": booking.guest_contact,
        "booking_date": booking.booking_date,
    }


def guest_identity_to_dict(identity):
    return {
        "identity_id": identity.identity_id,
        "id_type": identity.id_type,
        "id_number": identity.id_number,
        "verified": identity.verified,
        "verified_at": identity.verified_at,
    }


def room_inspection_to_dict(inspection):
    return {
        "inspection_id": inspection.inspection_id,
        "booking_id": inspection.booking_id,
        "room_id": inspection.room_id,
        "damage_found": inspection.damage_found,
        "damage_description": inspection.damage_description,
        "estimated_cost": inspection.estimated_cost,
        "inspected_at": inspection.inspected_at,
    }


# -------------------------
# WF-113 — Extended Stay Serializers
# -------------------------

def extended_stay_application_to_dict(application):
    return {
        "application_id": application.application_id,
        "student_id": application.student_id,
        "reason": application.reason,
        "status": application.status,
        "start_date": application.start_date,
        "end_date": application.end_date,
        "approval_date": application.approval_date,
        "faculty_approval": application.faculty_approval,
        "payment_status": application.payment_status,
    }


def vacation_period_to_dict(period):
    return {
        "period_id": period.period_id,
        "period_name": period.period_name,
        "start_date": period.start_date,
        "end_date": period.end_date,
        "period_type": period.period_type,
    }


def stay_charge_to_dict(charge):
    return {
        "charge_id": charge.charge_id,
        "application_id": charge.application_id,
        "base_amount": charge.base_amount,
        "facility_charges": charge.facility_charges,
        "tax": charge.tax,
        "total_amount": charge.total_amount,
        "payment_status": charge.payment_status,
    }


def authorization_document_to_dict(doc):
    return {
        "doc_id": doc.doc_id,
        "student_id": doc.student_id,
        "faculty_name": doc.faculty_name,
        "verification_status": doc.verification_status,
        "verified_at": doc.verified_at,
    }

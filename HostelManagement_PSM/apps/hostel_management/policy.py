"""
policy.py
Business Rules Layer — Hostel Management PSM

Source of truth:
- RE Business Rules (BR-HM-xxx)
- UC ↔ BR ↔ WF Traceability
"""

from datetime import date
from typing import List, Optional


# =====================================================
# WF-101 — LEAVE MANAGEMENT
# =====================================================

def br_hm_101_student_must_be_active(hostel_status: str) -> bool:
    return hostel_status == "ACTIVE"


def br_hm_102_leave_dates_valid(start_date: date, end_date: date) -> bool:
    return start_date <= end_date


def br_hm_103_leave_requires_reason_and_docs(reason: Optional[str], docs_attached: bool) -> bool:
    return bool(reason) and docs_attached


def br_hm_104_only_assigned_caretaker_can_approve(
    role: str,
    caretaker_hostels: List[str],
    student_hostel: str
) -> bool:
    return role == "CARETAKER" and student_hostel in caretaker_hostels


def br_hm_105_attendance_updated_on_approval(status: str) -> bool:
    return status == "APPROVED"


# =====================================================
# WF-102 — COMPLAINT MANAGEMENT
# =====================================================

def br_hm_106_active_students_only(hostel_status: str) -> bool:
    return hostel_status == "ACTIVE"


def br_hm_107_security_routes_to_warden(category: str) -> bool:
    return category.upper() == "SECURITY"


def br_hm_108_resolution_requires_remarks(status: str, remarks: Optional[str]) -> bool:
    return status == "RESOLVED" and bool(remarks)


def br_hm_109_escalation_only_if_unresolved(status: str) -> bool:
    return status in ("OPEN", "IN_PROGRESS")


def br_hm_110_only_warden_resolves_security(role: str) -> bool:
    return role == "WARDEN"


# =====================================================
# WF-103 — ROOM ALLOTMENT
# =====================================================

def br_hm_111_allotment_window_open(window_status: str) -> bool:
    return window_status == "OPEN"


def br_hm_112_room_capacity_available(capacity: int, occupancy: int) -> bool:
    return occupancy < capacity


def br_hm_113_only_superadmin_bulk_allot(role: str) -> bool:
    return role == "SUPERADMIN"


# =====================================================
# WF-104 — ROOM CHANGE
# =====================================================

def br_hm_115_student_must_have_room(has_room: bool) -> bool:
    return has_room


def br_hm_116_dual_approval_required(caretaker: bool, warden: bool) -> bool:
    return caretaker and warden


def br_hm_117_room_occupancy_must_update() -> bool:
    return True


def br_hm_118_student_notified_on_change() -> bool:
    return True


# =====================================================
# WF-105 — FINE MANAGEMENT
# =====================================================

def br_hm_012_authorized_roles_impose_fine(role: str) -> bool:
    return role in ("CARETAKER", "WARDEN")


def br_hm_013_fine_amount_positive(amount: float) -> bool:
    return amount > 0


def br_hm_014_fine_initial_status() -> str:
    return "UNPAID"


def br_hm_022_fines_must_be_cleared(amount_due: float) -> bool:
    return amount_due == 0


# =====================================================
# WF-106 — HOSTEL SETUP & STAFFING
# =====================================================

def br_hm_008_hostel_deactivation_requires_zero_occupancy(occupied_rooms: int) -> bool:
    return occupied_rooms == 0


def br_hm_019_activation_requires_staff(warden_count: int, caretaker_count: int) -> bool:
    return warden_count > 0 and caretaker_count > 0


def br_hm_025_configuration_is_source_of_truth() -> bool:
    return True


# =====================================================
# WF-107 — SECURITY
# =====================================================

def br_hm_026_authorized_security_roles(role: str) -> bool:
    return role in ("WARDEN", "CARETAKER")


def br_hm_027_no_shift_overlap(overlap: bool) -> bool:
    return not overlap


def br_hm_028_incident_must_have_severity(severity: Optional[str]) -> bool:
    return bool(severity)


# =====================================================
# WF-108 — VISITOR / INVENTORY
# =====================================================

def br_hm_021_inventory_updates_logged() -> bool:
    return True


def br_hm_030_resource_request_approved(approved: bool) -> bool:
    return approved


def br_hm_031_inventory_update_authorized(role: str) -> bool:
    return role in ("CARETAKER", "WARDEN")


# =====================================================
# WF-109 — ROOM VACATION
# =====================================================

def br_hm_015_vacation_request_required(has_request: bool) -> bool:
    return has_request


def br_hm_016_clearance_requires_no_dues(pending_dues: float, inventory_clear: bool) -> bool:
    return pending_dues == 0 and inventory_clear


def br_hm_017_all_departments_clear(flags: List[bool]) -> bool:
    return all(flags)


def br_hm_018_vacation_date_future(vacation_date: date, today: date) -> bool:
    return vacation_date > today


# =====================================================
# WF-110 — NOTICE
# =====================================================

def br_hm_029_notice_length_valid(title_len: int, desc_len: int) -> bool:
    return 5 <= title_len <= 200 and 20 <= desc_len <= 5000


def br_hm_033_only_staff_publish(role: str) -> bool:
    return role in ("CARETAKER", "WARDEN")


def br_hm_035_students_view_published(status: str) -> bool:
    return status == "PUBLISHED"


def br_hm_039_notice_target_matches(student_hostel: str, notice_hostel: Optional[str], scope: str) -> bool:
    return scope == "ALL" or student_hostel == notice_hostel


# =====================================================
# WF-111 — REPORTS
# =====================================================

def br_hm_040_authorized_generate_reports(role: str) -> bool:
    return role in ("CARETAKER", "WARDEN")


def br_hm_045_reports_require_submission(status: str) -> bool:
    return status == "GENERATED"


def br_hm_046_superadmin_reviews(role: str) -> bool:
    return role == "SUPERADMIN"


def br_hm_050_reports_archived() -> bool:
    return True


# =====================================================
# WF-112 — GUEST ROOM
# =====================================================

def br_hm_051_guest_room_eligibility(
    hostel_status: str,
    outstanding_fines: float,
    disciplinary_status: str
) -> bool:
    return (
        hostel_status == "ACTIVE"
        and outstanding_fines == 0
        and disciplinary_status != "SERIOUS"
    )


def br_hm_052_guest_booking_dates_valid(check_in: date, check_out: date, today: date) -> bool:
    return today <= check_in < check_out


# =====================================================
# WF-113 — EXTENDED STAY
# =====================================================

def br_hm_061_extended_stay_eligibility(
    academic_standing: str,
    faculty_approval: bool
) -> bool:
    return academic_standing == "GOOD" and faculty_approval

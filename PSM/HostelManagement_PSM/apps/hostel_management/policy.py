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
# WF-112 — GUEST ROOM (ADDITIONAL RULES - PHASE 1)
# =====================================================

def br_hm_053_guest_info_required(guest_name: Optional[str], guest_contact: Optional[str]) -> bool:
    """Guest information must be provided"""
    return bool(guest_name) and bool(guest_contact)


def br_hm_054_advance_booking_window(check_in: date, booking_date: date, max_advance_days: int) -> bool:
    """Bookings cannot be made too far in advance"""
    days_ahead = (check_in - booking_date).days
    return 0 <= days_ahead <= max_advance_days


def br_hm_055_max_booking_duration(check_in: date, check_out: date, max_days: int) -> bool:
    """Guest room bookings have maximum duration limit"""
    duration = (check_out - check_in).days
    return 0 < duration <= max_days


def br_hm_056_identity_verification_required(id_type: Optional[str], id_number: Optional[str]) -> bool:
    """Identity documents must be verified"""
    return bool(id_type) and bool(id_number)


def br_hm_057_damage_assessment_required(checkout_status: str) -> bool:
    """Room inspection required during checkout"""
    return checkout_status in ("CHECKED_OUT", "COMPLETED")


def br_hm_058_damage_fine_calculation(damage_found: bool, estimated_cost: float) -> float:
    """Calculate fine for damages"""
    if damage_found and estimated_cost > 0:
        return estimated_cost * 1.1  # 10% penalty
    return 0.0


def br_hm_059_guest_room_charges(duration_days: int, base_rate: float) -> float:
    """Calculate total guest room charges"""
    return duration_days * base_rate


# =====================================================
# WF-113 — EXTENDED STAY
# =====================================================

def br_hm_061_extended_stay_eligibility(
    academic_standing: str,
    faculty_approval: bool
) -> bool:
    return academic_standing == "GOOD" and faculty_approval


# =====================================================
# WF-113 — EXTENDED STAY (ADDITIONAL RULES - PHASE 1)
# =====================================================

def br_hm_062_vacation_dates_valid(start_date: date, end_date: date, vacation_period_start: date, vacation_period_end: date) -> bool:
    """Stay dates must fall within official vacation period"""
    return vacation_period_start <= start_date <= end_date <= vacation_period_end


def br_hm_063_authorization_docs_required(faculty_approval: bool, authorization_doc_id: Optional[str]) -> bool:
    """Faculty authorization document required"""
    return faculty_approval and bool(authorization_doc_id)


def br_hm_064_stay_charges_calculation(duration_days: int, base_rate: float, facility_charges: float) -> float:
    """Calculate extended stay charges with facilities"""
    base_amount = duration_days * base_rate
    total = base_amount + facility_charges
    tax = total * 0.18  # 18% GST
    return total + tax


def br_hm_066_document_verification(doc_verified: bool, faculty_name: Optional[str]) -> bool:
    """Authorization document must be verified"""
    return doc_verified and bool(faculty_name)


def br_hm_067_capacity_check(current_occupancy: int, max_capacity: int) -> bool:
    """Check if hostel has capacity for extended stay"""
    return current_occupancy < max_capacity


def br_hm_073_payment_deadline(payment_status: str, deadline_date: date, current_date: date) -> bool:
    """Payment must be completed before deadline"""
    if payment_status == "PAID":
        return True
    return current_date <= deadline_date


def br_hm_074_services_coordination(mess_available: bool, security_available: bool) -> bool:
    """Essential services must be available during vacation"""
    return mess_available and security_available


def br_hm_076_violation_handling(conduct_violations: int, max_allowed: int) -> bool:
    """Check for conduct violations"""
    return conduct_violations <= max_allowed


# =====================================================
# WF-109 — ROOM VACATION (ADDITIONAL RULES - PHASE 1)
# =====================================================

def br_hm_041_clearance_verification(all_departments_clear: bool) -> bool:
    """All departments must clear student"""
    return all_departments_clear


def br_hm_042_room_clearance(room_inspection_done: bool, inventory_verified: bool) -> bool:
    """Room must be physically cleared and verified"""
    return room_inspection_done and inventory_verified


# =====================================================
# WF-111 — REPORTS (ADDITIONAL RULES - PHASE 1)
# =====================================================

def br_hm_043_report_data_validation(data_complete: bool, date_range_valid: bool) -> bool:
    """Report data must be complete and valid"""
    return data_complete and date_range_valid


def br_hm_044_report_format_requirements(format_type: str) -> bool:
    """Report must be in acceptable format"""
    return format_type in ("PDF", "EXCEL", "CSV")

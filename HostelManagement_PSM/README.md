# Hostel Management Module — Platform Specific Model (PSM)
# FusionIIIT-Hostel-Management-Module-15-PSM

## Overview

This repository contains the **Platform Specific Model (PSM)** implementation for the Hostel Management Module of the FusionIIIT ERP Portal. The PSM provides a complete, framework-agnostic implementation following the Entity-Boundary-Control (EBC) architectural pattern.

**Implementation Status:** ✅ 100% Complete

## Architecture

The PSM follows the **Entity-Boundary-Control (EBC)** architectural pattern with clear separation of concerns:

```
apps/hostel_management/
├── models.py          # Entity Layer - 38 domain entities
├── policy.py          # Policy Layer - 59 business rules
├── services.py        # Control Layer - 26+ service functions
├── views.py           # Boundary Layer - 30+ view functions
├── serializers.py     # Serialization - 25+ serializers
├── urls.py            # URL Routing - 30+ endpoints
├── events.py          # Event Handlers - 32+ audit/notification handlers
└── __init__.py        # Module exports
```

### Layer Responsibilities

- **Entity Layer (models.py):** Domain model definitions including Student, Room, Hostel, Leave, Complaint, Fine, Guest, etc.
- **Policy Layer (policy.py):** Business rules validation (BR-HM-001 through BR-HM-076)
- **Control Layer (services.py):** Use case implementations and business logic orchestration
- **Boundary Layer (views.py):** API view functions for external interaction
- **Serialization (serializers.py):** DTO converters for entity-to-dict transformations
- **Event Handlers (events.py):** Audit logging and side-effects for workflow actions
- **URL Routing (urls.py):** REST endpoint mappings

## Workflows Implemented

This PSM implements **all 13 workflows** from the Domain specifications:

| Workflow | Name | Use Cases | Status |
|----------|------|-----------|--------|
| **HM-WF-101** | Leave Management | UC-001 to UC-004 | ✅ Complete |
| **HM-WF-102** | Complaint Resolution | UC-006 to UC-009 | ✅ Complete |
| **HM-WF-103** | Room Allotment | UC-012 to UC-014 | ✅ Complete |
| **HM-WF-104** | Room Change | UC-013 to UC-015 | ✅ Complete |
| **HM-WF-105** | Fine Management | UC-016 to UC-018 | ✅ Complete |
| **HM-WF-106** | Hostel Setup | UC-005A, UC-005B | ✅ Complete |
| **HM-WF-107** | Security & Guard | UC-024, UC-025 | ✅ Complete |
| **HM-WF-108** | Visitor Management | UC-026 to UC-028 | ✅ Complete |
| **HM-WF-109** | Room Vacation | UC-029 to UC-031 | ✅ Complete |
| **HM-WF-110** | Notice Management | UC-032, UC-033 | ✅ Complete |
| **HM-WF-111** | Report Generation | UC-034, UC-035 | ✅ Complete |
| **HM-WF-112** | Guest Room Booking | UC-036, UC-037 | ✅ Complete |
| **HM-WF-113** | Extended Stay | UC-038 to UC-040 | ✅ Complete |

## Business Rules Coverage

The implementation enforces **59 business rules** across all workflows:

- **BR-HM-001 to BR-HM-018:** Leave Management validation
- **BR-HM-019 to BR-HM-028:** Complaint handling rules
- **BR-HM-029 to BR-HM-040:** Room allotment & allocation rules
- **BR-HM-041 to BR-HM-044:** Room vacation & clearance rules
- **BR-HM-045 to BR-HM-052:** Fine & payment validation
- **BR-HM-053 to BR-HM-061:** Guest room booking rules
- **BR-HM-062 to BR-HM-076:** Extended stay authorization rules

All business rules are implemented in `policy.py` with descriptive names (e.g., `br_hm_001_leave_balance_check`, `br_hm_053_guest_identity_verification`).

## Domain Entities

The PSM includes **38 comprehensive domain entities**:

### Core Entities
- Student, Room, Hostel, Hall, Floor
- RoomAllocation, RoomChangeRequest
- Staff, Guard, ShiftAssignment

### Leave Management
- Leave, LeaveQuota, LeaveBalance, LeaveApproval

### Complaint & Fine Management
- Complaint, ComplaintResponse, ComplaintResolution
- Fine, FinePayment, FineCategory

### Visitor & Guest Management
- Visitor, VisitRequest, VisitLog
- GuestRoomBooking, GuestIdentity, RoomInspection

### Extended Stay
- ExtendedStayApplication, VacationPeriod, StayCharge
- AuthorizationDocument, DisciplinaryReport

### Hostel Operations
- Notice, IncidentReport, ClearanceRecord
- ResourceRequest, Inventory

## API Endpoints

### Leave Management (WF-101)
- `POST /leave/request` - Submit leave request
- `POST /leave/approve` - Approve/reject leave
- `POST /leave/cancel` - Cancel leave

### Complaint Resolution (WF-102)
- `POST /complaint/lodge` - Lodge new complaint
- `POST /complaint/respond` - Add response to complaint
- `POST /complaint/close` - Close complaint

### Room Operations (WF-103, WF-104)
- `POST /room/allot` - Allot room to student
- `POST /room/change/request` - Request room change
- `POST /room/change/approve` - Approve room change

### Fine Management (WF-105)
- `POST /fine/impose` - Impose fine on student
- `POST /fine/pay` - Record fine payment

### Hostel Setup (WF-106)
- `POST /hostel/create` - Create new hostel
- `POST /hostel/staff/assign` - Assign staff to hostel

### Security (WF-107)
- `POST /security/guard/assign` - Assign guard to shift
- `POST /security/incident/log` - Log security incident

### Visitor Management (WF-108)
- `POST /visitor/request` - Request visitor permission
- `POST /visitor/entry` - Log visitor entry
- `POST /visitor/exit` - Log visitor exit

### Room Vacation (WF-109)
- `POST /vacation/request` - Request room vacation
- `POST /vacation/clearance/verify` - Verify clearance

### Notice Management (WF-110)
- `POST /notice/create` - Create hostel notice

### Report Generation (WF-111)
- `POST /report/generate` - Generate hostel report

### Guest Room Booking (WF-112)
- `POST /guest/booking/request` - Request guest room
- `POST /guest/booking/approve` - Approve guest booking
- `POST /guest/checkin` - Check-in guest
- `POST /guest/checkout` - Check-out guest

### Extended Stay (WF-113)
- `POST /extended-stay/apply` - Apply for extended stay
- `POST /extended-stay/review` - Review extended stay application
- `POST /extended-stay/payment` - Process extended stay payment

## Usage

### Basic Service Call
```python
from apps.hostel_management.services import request_leave
from apps.hostel_management.models import Student

student = Student(...)
result = request_leave(
    student=student,
    leave_type="home_visit",
    start_date="2026-01-15",
    end_date="2026-01-20",
    reason="Family function"
)
```

### Policy Validation
```python
from apps.hostel_management.policy import br_hm_001_leave_balance_check

is_valid = br_hm_001_leave_balance_check(student, leave_days=5)
```

### Event Handler
```python
from apps.hostel_management.events import audit_leave_request

audit_leave_request(leave_id, student_id, action="submitted")
```

## Code Organization

### Verification
All Python files pass syntax validation:
```bash
python -m py_compile models.py
python -m py_compile policy.py
python -m py_compile services.py
python -m py_compile views.py
python -m py_compile serializers.py
python -m py_compile events.py
python -m py_compile urls.py
```

## Design Decisions

1. **Framework-Agnostic:** No specific framework dependencies (Django/JPA/etc.)
2. **EBC Pattern:** Clear separation of entity, boundary, and control layers
3. **Explicit Business Rules:** All BR rules implemented as named functions
4. **Audit Trail:** Comprehensive event logging for all workflow actions
5. **Type Safety:** Clear entity definitions with explicit attributes
6. **RESTful API:** Standard REST endpoint conventions

## Testing Recommendations

1. **Unit Tests:** Test individual service functions with mock entities
2. **Integration Tests:** Test complete workflows end-to-end
3. **Policy Tests:** Verify all 59 business rules with edge cases
4. **API Tests:** Test all REST endpoints with valid/invalid inputs


## License

Part of the FusionIIIT project.

---

**Last Updated:** January 11, 2026  


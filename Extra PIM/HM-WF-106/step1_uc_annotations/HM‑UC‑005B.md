## **classDiagram**

##     **class SuperAdmin {**

##         **+adminId**

##         **+name**

##         **+assignCaretaker()**

##     **}**

## 

##     **class Hostel {**

##         **+hostelId**

##         **+name**

##         **+status**

##     **}**

## 

##     **class Staff {**

##         **+staffId**

##         **+name**

##         **+role**

##         **+isEligible()**

##     **}**

## 

##     **class CaretakerAssignment {**

##         **+assignmentId**

##         **+assignedDate**

##         **+status**

##     **}**

## 

##     **class HostelStaffService {**

##         **+listEligibleCaretakers()**

##         **+validateEligibility()**

##         **+assignCaretaker()**

##     **}**

## 

##     **class StaffRepository {**

##         **+getEligibleCaretakers()**

##         **+getStaffById()**

##     **}**

## 

##     **class AssignmentRepository {**

##         **+saveAssignment()**

##     **}**

## 

##     **%% Relationships**

##     **SuperAdmin --> HostelStaffService : initiates**

##     **HostelStaffService --> StaffRepository : queries**

##     **HostelStaffService --> AssignmentRepository : persists**

##     **HostelStaffService --> CaretakerAssignment : creates**

##     **CaretakerAssignment --> Hostel : assignedTo**

##     **CaretakerAssignment --> Staff : caretaker**

## 


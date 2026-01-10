## **classDiagram**

##     **class SuperAdmin {**

##         **+adminId**

##         **+name**

##         **+assignWarden()**

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

##     **class WardenAssignment {**

##         **+assignmentId**

##         **+assignedDate**

##         **+status**

##     **}**

## 

##     **class HostelStaffService {**

##         **+listEligibleWardens()**

##         **+validateEligibility()**

##         **+assignWarden()**

##     **}**

## 

##     **class StaffRepository {**

##         **+getEligibleWardens()**

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

##     **HostelStaffService --> WardenAssignment : creates**

##     **WardenAssignment --> Hostel : assignedTo**

##     **WardenAssignment --> Staff : warden**

## 


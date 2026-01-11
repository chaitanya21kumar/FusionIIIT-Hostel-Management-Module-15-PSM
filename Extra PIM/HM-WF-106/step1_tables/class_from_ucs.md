classDiagram
    class SuperAdmin {
        +adminId
        +name
        +email
        +createHostel()
    }

    class Hostel {
        +hostelId
        +name
        +type
        +address
        +capacity
        +status
        +createdAt
        +setInactiveStatus()
    }

    class HostelService {
        +validateHostelData()
        +checkDuplicateHostel()
        +saveHostel()
    }

    class HostelRepository {
        +persistHostel()
        +findByName()
    }

    %% Relationships
    SuperAdmin --> HostelService : initiates
    HostelService --> Hostel : creates
    HostelService --> HostelRepository : uses
    HostelRepository --> Hostel : stores

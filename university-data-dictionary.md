## Students Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Student ID | String | STDXXX | Y | Unique student identifier | STD001 |
| Name | Text | 50 | Y | Student full name | John Smith |
| Age | Integer | 2 | Y | Student age | 20 |
| Gender | Text | 10 | Y | Student gender | Male |
| Major | Text | 50 | Y | Field of study | Computer Science |
| Enrollment Year | Integer | 4 | Y | Year of enrollment | 2023 |
| GPA | Decimal | 3,2 | Y | Grade point average | 3.75 |

## Professors Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Professor ID | String | PROFXXX | Y | Unique professor identifier | PROF001 |
| Department ID | String | DEPTXXX | Y | Associated department | DEPT001 |
| Office | Text | 10 | Y | Office location | Room 101A |
| Courses Taught | Text | 200 | Y | List of courses | CS101, CS102 |
| Research Interests | Text | 200 | N | Research areas | AI, ML |

## Courses Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Course ID | String | CRSXXX | Y | Unique course identifier | CRS001 |
| Title | Text | 100 | Y | Course name | Database Systems |
| Credits | Integer | 1 | Y | Course credit hours | 3 |
| Department ID | String | DEPTXXX | Y | Associated department | DEPT001 |
| Syllabus | Text | 500 | Y | Course outline | Course covers... |
| Prerequisites | Text | 200 | N | Required courses | CRS100 |

## Departments Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Department ID | String | DEPTXXX | Y | Unique department ID | DEPT001 |
| Name | Text | 100 | Y | Department name | Computer Science |
| Head ID | String | PROFXXX | Y | Department head | PROF001 |

## Enrollments Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Enrollment ID | String | ENRXXX | Y | Unique enrollment ID | ENR001 |
| Student ID | String | STDXXX | Y | Student reference | STD001 |
| Course ID | String | CRSXXX | Y | Course reference | CRS001 |
| Semester | Text | 20 | Y | Academic semester | Fall 2023 |
| Grade | Text | 2 | N | Course grade | A+ |
| Status | Text | 20 | Y | Enrollment status | Active |

## Classrooms Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Classroom ID | String | CLSXXX | Y | Unique classroom ID | CLS001 |
| Building | Text | 50 | Y | Building name | Science Hall |
| Room Number | Text | 10 | Y | Room identifier | 301 |
| Capacity | Integer | 3 | Y | Room capacity | 100 |

## Schedules Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Schedule ID | String | SCHXXX | Y | Unique schedule ID | SCH001 |
| Course ID | String | CRSXXX | Y | Course reference | CRS001 |
| Classroom ID | String | CLSXXX | Y | Classroom reference | CLS001 |
| Time Slot | String | TIMXXX | Y | Time slot reference | TIM001 |

## Libraries Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Library ID | String | LIBXXX | Y | Unique library ID | LIB001 |
| Name | Text | 100 | Y | Library name | Main Library |
| Location | Text | 100 | Y | Physical location | North Campus |

## Staff Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Staff ID | String | STFXXX | Y | Unique staff ID | STF001 |
| Name | Text | 100 | Y | Staff name | Jane Doe |
| Role | Text | 50 | Y | Staff position | Administrator |
| Department ID | String | DEPTXXX | Y | Department reference | DEPT001 |

## Clubs Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Club ID | String | CLBXXX | Y | Unique club ID | CLB001 |
| Name | Text | 100 | Y | Club name | Chess Club |
| Advisor ID | String | PROFXXX | Y | Faculty advisor | PROF001 |

## Events Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Event ID | String | EVTXXX | Y | Unique event ID | EVT001 |
| Name | Text | 100 | Y | Event name | Spring Fair |
| Date | Date | DD/MM/YYYY | Y | Event date | 15/04/2024 |
| Location | Text | 100 | Y | Event location | Main Hall |

## Scholarships Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Scholarship ID | String | SCHLXXX | Y | Unique scholarship ID | SCHL001 |
| Name | Text | 100 | Y | Scholarship name | Merit Award |
| Amount | Decimal | 10,2 | Y | Scholarship amount | 5000.00 |
| Eligibility | Text | 200 | Y | Requirements | GPA >= 3.5 |

## Applications Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Application ID | String | APPXXX | Y | Unique application ID | APP001 |
| Student ID | String | STDXXX | Y | Student reference | STD001 |
| Scholarship ID | String | SCHLXXX | Y | Scholarship reference | SCHL001 |
| Status | Text | 20 | Y | Application status | Pending |

## Fees Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Fee ID | String | FEEXXX | Y | Unique fee ID | FEE001 |
| Student ID | String | STDXXX | Y | Student reference | STD001 |
| Amount | Decimal | 10,2 | Y | Fee amount | 1000.00 |
| Due Date | Date | DD/MM/YYYY | Y | Payment deadline | 30/01/2024 |

## Hostels Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Hostel ID | String | HOSXXX | Y | Unique hostel ID | HOS001 |
| Name | Text | 100 | Y | Hostel name | East Hall |
| Capacity | Integer | 4 | Y | Total capacity | 200 |

## Hostel_Assignments Table
| Data Name | Data Type | Length/Format | Mandatory | Description | Sample |
|-----------|-----------|---------------|-----------|-------------|---------|
| Assignment ID | String | ASGXXX | Y | Unique assignment ID | ASG001 |
| Student ID | String | STDXXX | Y | Student reference | STD001 |
| Hostel ID | String | HOSXXX | Y | Hostel reference | HOS001 |
| Room Number | Text | 10 | Y | Room identifier | E101 |
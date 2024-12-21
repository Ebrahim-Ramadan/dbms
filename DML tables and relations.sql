-- University Management System

-- define tables
students [icon: user, color: lightblue]{
  id string pk
  name string
  age int
  gender string
  major string
  enrollment_year int
  gpa float
}

professors [icon: user, color: lightgreen]{
  id string pk
  name string
  department_id string
  office string
  courses_taught string
  research_interests string
}

courses [icon: book, color: orange]{
  id string pk
  title string
  credits int
  department_id string
  syllabus string
  prerequisites string
}

departments [icon: building, color: purple]{
  id string pk
  name string
  head_id string
}

enrollments [icon: file-text, color: yellow]{
  id string pk
  student_id string
  course_id string
  semester string
  grade string
  enrollment_date string
  status string
}

classrooms [icon: home, color: pink]{
  id string pk
  building string
  room_number string
  capacity int
}

schedules [icon: calendar, color: teal]{
  id string pk
  course_id string
  classroom_id string
  time_slot string
}

time_slots [icon: clock, color: gray]{
  id string pk
  day string
  start_time string
  end_time string
}

libraries [icon: book-open, color: brown]{
  id string pk
  name string
  location string
}

library_books [icon: book, color: darkgreen]{
  id string pk
  title string
  author string
  library_id string
}

staff [icon: user-check, color: lightgray]{
  id string pk
  name string
  role string
  department_id string
}

administration [icon: briefcase, color: darkblue]{
  id string pk
  name string
  position string
}

clubs [icon: users, color: red]{
  id string pk
  name string
  advisor_id string
}

events [icon: calendar, color: lightyellow]{
  id string pk
  name string
  date string
  location string
}

scholarships [icon: gift, color: gold]{
  id string pk
  name string
  amount int
  eligibility string
}

applications [icon: file-text, color: lightpurple]{
  id string pk
  student_id string
  scholarship_id string
  status string
}

transcripts [icon: file, color: lightbrown]{
  id string pk
  student_id string
  issue_date string
}

fees [icon: dollar-sign, color: lightred]{
  id string pk
  student_id string
  amount_due int
  due_date string
}

hostels [icon: home, color: lightgreen]{
  id string pk
  name string
  capacity int
}

hostel_assignments [icon: file-text, color: lightblue]{
  id string pk
  student_id string
  hostel_id string
  room_number string
}
academic_advisors [icon: user-tie, color: lightorange] {
  
  id string pk
  name string
  department_id string
  office string
}
course_prerequisites [icon: link, color: lightgray] {
  
  id string pk
  course_id string
  prerequisite_course_id string
}



-- define relationships
students.major > departments.id
professors.department_id > departments.id
courses.department_id > departments.id
enrollments.student_id > students.id
enrollments.course_id > courses.id
schedules.course_id > courses.id
schedules.classroom_id > classrooms.id
library_books.library_id > libraries.id
staff.department_id > departments.id
clubs.advisor_id > professors.id
applications.student_id > students.id
applications.scholarship_id > scholarships.id
transcripts.student_id > students.id
fees.student_id > students.id
hostel_assignments.student_id > students.id
hostel_assignments.hostel_id > hostels.id
enrollments.enrollment_date > schedules.time_slot
students.id > enrollments.student_id
courses.id > enrollments.course_id
professors.id > courses.id
students.id > academic_advisors.id
course_prerequisites.course_id > courses.id
course_prerequisites.prerequisite_course_id > courses.id

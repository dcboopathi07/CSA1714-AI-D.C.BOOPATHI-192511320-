% Facts
student(101, boopathi).
student(102, rahul).
student(103, priya).

teacher(t1, john).
teacher(t2, david).

subject(s1, prolog).
subject(s2, python).
subject(s3, java).

% Relationships
teaches(t1, s1).
teaches(t2, s2).
teaches(t1, s3).

studies(101, s1).
studies(102, s2).
studies(103, s3).

% Rules
student_teacher(Student, Teacher) :-
studies(Student, Subject),
teaches(Teacher, Subject).

% Queries
% ?- student(101, Name).
% ?- student_teacher(101, Teacher).
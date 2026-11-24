student(arun, cse, 21).
student(bala, it, 22).
student(chitra, cse, 20).
student(divya, ece, 21).

department(D, Name) :-
student(Name, D, _).

above_age(Age, Name) :-
student(Name, _, A),
A > Age.
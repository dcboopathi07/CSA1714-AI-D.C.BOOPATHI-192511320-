symptom(ram, fever).
symptom(ram, cough).

symptom(raj, headache).
symptom(raj, fever).

disease(X, flu) :-
symptom(X, fever),
symptom(X, cough).

disease(X, fever) :-
symptom(X, fever).

disease(X, migraine) :-
symptom(X, headache).

diagnosis(X) :-
disease(X, D),
write('Disease: '),
write(D).
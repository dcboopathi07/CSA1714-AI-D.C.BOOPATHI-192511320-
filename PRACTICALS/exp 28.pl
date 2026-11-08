fact(rain).
fact(cloudy).

rule1 :-
fact(rain),
write('Road is wet'), nl.

rule2 :-
fact(cloudy),
write('Rain may come'), nl.

forward :-
rule1,
rule2.
edge(a, b, 2).
edge(a, c, 4).
edge(b, d, 3).
edge(c, d, 1).

best_first(Start, Goal) :-
path(Start, Goal, [Start]).

path(Goal, Goal, _) :-
write('Goal Reached').

path(Current, Goal, Visited) :-
edge(Current, Next, _),
\+ member(Next, Visited),
path(Next, Goal, [Next|Visited]).
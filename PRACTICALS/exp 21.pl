bird(parrot).
bird(pigeon).
bird(eagle).
bird(ostrich).
bird(penguin).

can_fly(parrot).
can_fly(pigeon).
can_fly(eagle).

cannot_fly(ostrich).
cannot_fly(penguin).

check_flight(X) :-
can_fly(X),
write(X), write(' can fly').

check_flight(X) :-
cannot_fly(X),
write(X), write(' cannot fly').
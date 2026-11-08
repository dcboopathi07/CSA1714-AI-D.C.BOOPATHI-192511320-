male(john).
male(peter).
male(david).

female(mary).
female(susan).
female(anna).

parent(john, peter).
parent(mary, peter).
parent(peter, david).
parent(susan, david).
parent(peter, anna).
parent(susan, anna).

father(X, Y) :-
male(X),
parent(X, Y).

mother(X, Y) :-
female(X),
parent(X, Y).

sibling(X, Y) :-
parent(Z, X),
parent(Z, Y),
X \= Y.
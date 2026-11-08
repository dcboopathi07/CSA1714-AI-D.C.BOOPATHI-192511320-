% Facts
male(john).
male(peter).
male(david).
female(mary).
female(susan).
female(lisa).

% Parent relationships
parent(john, peter).
parent(mary, peter).
parent(peter, david).
parent(susan, david).
parent(peter, lisa).

% Rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
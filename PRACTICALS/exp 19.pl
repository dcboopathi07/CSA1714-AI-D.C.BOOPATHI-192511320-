% Planet Database
planet(mercury, 1).
planet(venus, 2).
planet(earth, 3).
planet(mars, 4).
planet(jupiter, 5).
planet(saturn, 6).
planet(uranus, 7).
planet(neptune, 8).

% Planet properties
planet_type(mercury, terrestrial).
planet_type(venus, terrestrial).
planet_type(earth, terrestrial).
planet_type(mars, terrestrial).
planet_type(jupiter, gas_giant).
planet_type(saturn, gas_giant).
planet_type(uranus, ice_giant).
planet_type(neptune, ice_giant).

% Rules
inner_planet(X) :-
planet(X, N),
N =< 4.

outer_planet(X) :-
planet(X, N),
N > 4.

% Queries
% ?- planet(X, 3).
% ?- inner_planet(X).
% ?- outer_planet(X).
% ?- planet_type(earth, Type).
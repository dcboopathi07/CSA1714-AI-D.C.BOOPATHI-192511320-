diet(diabetes, 'Avoid sugar and sweets').
diet(obesity, 'Eat fruits and vegetables').
diet(bp, 'Avoid salt and oily foods').
diet(heart_disease, 'Eat low fat food').

suggest_diet(Disease) :-
diet(Disease, Food),
write('Suggested Diet: '),
write(Food).
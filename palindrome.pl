% palindrome.pl
% By: Pedro Muniz,
%
% We can use this program to find out, for any given word or linguistic
% expression, if it is a palindrome: if, by inverting its characters, we
% get the same word. The query must take the form: palindrome(anyword).
% and the answer will be True (if the word is a palindrome) or False.


accRev([Cab|Rab], A, R) :-
    accRev(Rab,[Cab|A], R).
accRev([], A, A).

rev(L, R) :-
    accRev(L, [], R).

palindromo(X) :-
    atom_chars(X, List), rev(List, RevList), List = RevList.

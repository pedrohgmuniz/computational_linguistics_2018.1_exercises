% palindrome.pl
% A program to find out, for any given word/expression, if it is a
% palindrome: if, by inverting its characters, we get the same word.
% By: Pedro Muniz.
% Team: Pedro Muniz, H�lio Leonam, Adonis Sousa.
% coding: utf-8
%
% The query must take the form: palindrome(anyword). The output will
% be True if the word is a palindrome and False if it is not.

accRev([Cab|Rab], A, R) :-
    accRev(Rab,[Cab|A], R).
accRev([], A, A).

rev(L, R) :-
    accRev(L, [], R).

palindromo(X) :-
    atom_chars(X, List), rev(List, RevList), List = RevList.

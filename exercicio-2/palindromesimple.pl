% palindromesimple.pl
% Simplified version of palindrome.pl, using a buit-in functor:
% reverse/2.
% We can use this program to find out, for any given word or expression,
% if it is a palindrome: if, by inverting its characters, we get the
% same word.
% By: Pedro Muniz. Team: Pedro Muniz, Hélio Leonam, Adonis Sousa.
% coding: utf-8
%
% The query must take the form: palindrome(anyword). The output will
% be True if the word is a palindrome and False if it is not.

palindrome(X) :-
    atom_chars(X, List), reverse(List, RevList), List = RevList.

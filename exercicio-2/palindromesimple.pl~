% palindromesimple.pl
% By: Pedro Muniz,
%
% Simplified version of the palindrome program, using a buit-in functor:
% reverse/2.
% We can use this program to find out, for any given word or
% linguistic expression, if it is a palindrome: if, by inverting its
% characters, we get the same word. The query must take the form:
% palindrome(anyword). and the answer will be True (if the word is a
% palindrome) or False.


palindrome(X) :-
    atom_chars(X, List), reverse(List, RevList), List = RevList.

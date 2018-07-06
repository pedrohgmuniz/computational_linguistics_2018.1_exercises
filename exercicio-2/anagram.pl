% anagram.pl
% A program to find out, for any pair of words, if they are
% anagrams, that is, if they contain the same letters in any order.
% By: Pedro Muniz
% Team: Pedro Muniz, Hélio Leonam, Adonis Sousa.
% coding: utf-8

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                               ABOUT:                                 %
% A query must take the form: anagram(word1, word2).                   %
% The inter predicate is used to get the list of elements which is the %
% result of the intersection of two given lists                        %
%                                                                      %
% The program works fine. It does what it is supposed to do.           %
% Tere is just one tiny little bug: upon finding a pair of anagrams,   %
% it outputs 'true' 4 times before stopping (and outputting false, as  %
% it typically does).                                                  %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Rules for getting a list of the intersecting elements of two lists:
inter([], _, []).

inter([H1|T1], L2, [H1|A]) :-
    member(H1, L2),
    inter(T1, L2, A).

inter([_|T1], L2, A) :-
    inter(T1, L2, A).

% Rule for:
% 1. Transforming the two inputs into lists,
% 2. Getting the intersection of the two lists,
% 3. Checking if the length of the intersection is the same as
% the length of the two original lists:
anagram(X, Y) :-
    atom_chars(X, ListX),
    atom_chars(Y, ListY),
    inter(ListX, ListY, Intersect),
    length(Intersect, L), length(ListY, L), length(ListX, L).

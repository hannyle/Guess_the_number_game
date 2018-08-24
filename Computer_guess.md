# Guess_the_number_game
Guess the number game implementation computer POV
In this implementation your task is to make the computer guess your number in an arbitrary
range of numbers a, b by using
Binary search strategy. The computer should be guaranteed to do it in the number of tries t
which is defined as ceiling(log base 2 of (b ­ a)). That is if a is 0 and b is 200, then log2 (200
­ 0) = 7.643 and the ceiling is just this number rounded to the nearest integer above it, hence
we get 8.
Also, you should include a 0 but not include n in your numbers range, which
Is mathematically represented as [0, n).
Both ceiling and log functions are present in the math module, though you can easily
implement ceiling function yourself.
Your game should look something like this, you may use your own messages as long as
they make sense. In my case I have h for higher, l for lower and y for equals.
What range is your number in?
0, 200
Is your number 100?
h
Is your number 150?
h
Is your number 175?
l
Is your number 163?
y
Woah, that was tricky!
Play again? y/n
This assignment should be submitted by the next Wednesday June 8th 9 A.M.


Guess the number game implementation player POV

In this assignment your task is to implement a game called 'guess the number' for an arbitrary range of numbers a, b.

The number of tries should be set to the ceiling of the log base 2 of (b - a), that is if a is 0 and b is 200, then log2 (200 - 0) = 7.643 and the
ceiling is just this number rounded to the nearest integer above it, hence we get 8.

Also, you should include a 0 but not include n in your numbers range, which iss mathematically represented as [0, n).

Both ceiling and log functions are present in the math module, though you can easily implement ceiling function yourself.

Your game should look something like this:

Please enter 2 values for range:

0, 200

I have picked a number between 0 and 200, what’s your guess?

You have 8 tries left.

100

This number is lower than the number I have in mind! Next try?

You have 7 tries left.

150

This number is lower than the number I have in mind! Next try?

You have 6 tries left

175

This number is higher than the number I have in mind! Another guess?

You have 5 tries left

163

Thaat's right! That was my number!

Play again? y/n

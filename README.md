## Diceroller by Tilia

A simple dice roller script using Python3

While diceroller is running, it will continually loop, starting 
out with asking for the user to input a "roll." The input must 
start with a number, end with a number, and only contain the letter
"d" in between. It is not case sensitive, and the user may put 
spaces or not between them. 

Valid inputs:

```
4d8
1 D100
37 d 3029
```

invalid inputs:
```
d20
hello
that's what she said
```

If the input is not recognized, an error message will appear, and 
it wil send the user back to the original prompt. 

If the user types "help" it will display a helpful message.
If the user types "q" (not case sensitive), it will end the program.
If the user types "r" (not case sensitive), it will reuse the previous roll input.


### Changelog

#### [2.1] - 2020-09-10
- Removed homebrew rules from crit checker
- Added changelog
- Improved documentation, added README

#### [2.0] - 2018-06-27
- Added crit detection
- Added Help documentation
- Added re-roll feature

#### [1.0] - 2017-06-20
- Created the dice roller


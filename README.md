[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7JiC6Pwe)
# tPythonModule03fall25
tPythonModule03fall25

Created 9/10/25 by dH

This assignment is used to record course points for work submitted in the current GitHub Classroom repository. 

There is nothing to submit for this assignment - submit all code that you created for this module to the GitHub Classroom repo and you will receive full credit for this assignment!

Watch all the videos for this module and write the following Python programs:

Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the integers. If the user enters anything other than an integer, detect their mistake using try and except and print an error message and skip to the next integers.

Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

Code up Worked Exercise 6.5 as viewed in the video. This program involves prompting the user for a list of numbers, storing these numbers in a list, and then calculating the maximum and minimum numbers after the user has finished entering their numbers. The user indicates they are done by entering "done". Here's how you could implement this in Python.

This code snippet does the following:

Initializes an empty list called numbers to store the numeric inputs from the user.
Enters a loop where it continuously prompts the user to enter a number or 'done' to finish the input process.
If the user inputs 'done', the loop breaks.
If the user enters a number, the program attempts to convert the input to a float and add it to the numbers list. If the conversion fails (e.g., because the input is not a number), it catches the ValueError and prompts the user again without exiting or crashing.
After the user indicates they are done by entering 'done', the program checks if any numbers were entered. If so, it calculates and prints the maximum and minimum values using the max() and min() functions. If no numbers were entered, it prints a message indicating this.

This approach ensures that the program dynamically accepts a list of numbers from the user, handles invalid inputs gracefully, and computes the maximum and minimum values correctly.

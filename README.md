# F1 Driver Guessing Game
> A "Wordle" style game where the user guessses an F1 driver and is then given information based on that guess to assist in guessing the correct driver.

A random driver is chosen from a database and split into characteristics variables and it is the user's task to figure out which driver it is. The user is prompted for an input and that input itself is split into different characteristics which is then used to compare the user's input to the randomly chosen driver. The game then returns clues to help the user guess the correct answer.

For example: lets say the randomly chosen driver is Jenson Button. The user is prompted for an input and guesses Lewis Hamilton. The characteristics of Lewis Hamilton is compared against the secretly chosen driver, Jenson Button, and gives the user clues to further refine their guess. So it would show that the nationality of the secret driver is the same as Lewis Hamilton, that they have less World Championship titles, less points, etc. The user is then prompted to guess another driver and should keep in mind the clues they have been given. So now the user should guess another driver of the same nationality (because they have been told it is correct) but with less points, etc. than Lewis Hamilton.

This gameplay loop goes on until the player guesses the correct answer, or has 10 guesses.

---

## Note to self and anyone that may read through this

This app is still a WIP as of this commit. I have been working on this offline and decided to add it to the portfolio while continuing the work on it to give me a sense of ownership and show what I am currently doing.

As such, there are multiple "notes to self" within the code that I used to remind myself of future improvements, things to work on, etc. From now on I will try to use the Github features to assign bugs to myself as a way of learning how Github works and to ensure I am following a more sensible approach to this work.

## Installing / Getting started

As of this commit, the program can be downloaded and run from within an IDE of your choice with pandas and BS4 installed. Eventually I will compile into an .exe and the goal is to host the app online for all to play.
  
---

## Additional Features

Additional features that could be added:

    • Host app online
    • Allow for a predictive drop down list of drivers for the player to use to guess from (this would prevent spelling errors and aid the player to keep guessing)
    • When hosted online, show clues through colour cues (i.e. red is incorrect, yellow is partly correct, green is correct).
    • Add a "daily" feature to encourage players to return each day
    • Add the ability to filter the dataset so players are more likely to guess correctly based on their knowledge of F1 (currently all drivers that scored 0 points         are filtered out)
    • Ensure compatibility online with mobile users

---

## Motivation

The motivation for this program is because I enjoy games and I enjoy F1. I watched a Youtuber play different online guessing games that have a similar game structure and wanted to create one that I would enjoy.

It is also the perfect way to find motivation in an early project when learning the ropes and once I have finished the main code (still ongoing at time of writing) I will then look to host the app online.

This will give me a good insight into an entire app's lifecycle (albeit only a small personal version) and introduce me to the idea of "full stack" development and means I can easily share the finished product with friends who may be interested in playing it - I feel that seeing someone use something I have created will be a really important milestone.

---

## Licensing

Daniel Ellis

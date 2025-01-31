   
# Ultimate Speed Typing Test
This program aims to measure your typing accuracy.

# Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Installation
In order to properly use the Ultimate Speed Typing Test, you will need to install some python packages. We recommend that you install these packages using the pip command.
If you do not have pip installed in your system, please, in a terminal window, insert the following command line:
    
    sudo apt install python3-pip
    
After you get the pip command installed, it is now time to install the required python packages for running the Ultimate Speed Typing Test.
Please, install getch package:

    pip install https://pypi.python.org/packages/source/g/getch/getch-1.0-python2.tar.gz#md5=586ea0f1f16aa094ff6a30736ba03c50
   
And, again in the terminal window, install the pyfiglet:
    
    pip install pyfiglet


Now, you are ready to use the Ultimate Speed Typing Test!

# Usage
To launch the program, the user can enter 2 additional input arguments: the Maximum Value and/or the User Time Mode.
If none of them are inserted, the default maximum value is 10 and the user time mode is set to false. 

There are 2 game modes: by number of typed letters and by time in seconds.
The User Time Mode input argument sets the game mode. If its false (as default) the game mode is set by the number of the typed letters. In other hand, if the user call the utm input argument when launching the game, the game mode is set to the seconds of typing.
The Maximum Value input argument sets the end of the test (in runaway seconds or in typed keys).

For example, if the user run the command 
    
    main.py -mv 50 -utm
    
The game will end after 50 seconds of the moment that began.

After the program is launched, user will be informed about the game configurations, and will be asked to press a key.
After that action, a 3-second countdown will take place and the letters to type start to be requested.

When the time limit or attempts are reached, the statistics of the game are presented.


# Results

After the end of the test, the game will show to user his performance, by displaying some indicators values.
The list of the presented results is show in the following the table:

Parameter | Description 
--- | --- 
test_duration | total test duration 
test_start | begin test date 
test_end | ends test date
number_of_types | number of inputs 
number_of_hits | number of correct inputs 
accuracy | inputs accuracy (hits/total) 
type_average_duration | average duration of the user answers 
type_hit_average_duration | average duration of the correct user answers 
type_miss_average_duration | average duration of the wrong user answers 
types | list of information of each user answer: letter requested, letter received and ellapsed answer time (duration) 

With all this suitable program, we hope that you could improve your typing skills.

    

jumble_solver
=============

Solution to twice coding challenge. 

Although the instructions specified to not import any modules, I decided the `argparse` module would be useful for running the program on the command line. 

The default dictionary `my_2of12.txt` file was slightly modified from `12dicts-5.0/2of12.txt`.  I modified it by removing some one-chracter words that really shouldn't be considered words (e.g. 'b', 'c', 'd', etc.).  One can also supply another dictionary file as a command line argument.

I assume that the dictionary file is composed of only one word in each line, and I treat all uppercase and lowercase words the same.  So 'Dog' is the same as 'dog'.

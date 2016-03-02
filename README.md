Matt Anderson
Brigham Young University
3/2/16

This repository includes several examples of Pyomo code. For more information see the 
documentation of Pyomo available online at: http://www.pyomo.org/documentation/

If you have never used Pyomo before I suggest following the steps outlined in the quickstart guide below:


QUICKSTART GUIDE
1) Create a new repository on your computer of these files. The two most important files are
   "Abstract_Simple.py" and "params_1.dat". They need to be in the same directory.
2) Download a solver that can be used with pyomo. I suggest installing the glpk solver. Follow
   the instructions on this website: https://en.wikibooks.org/wiki/GLPK
3) Once you have the solver installed open Terminal in the directory where the Abstract_Simple.py
   and params_1.dat files are located.
4) Enter this command to solve: $ pyomo solve Abstract_Simple.py params_1.dat --solver=glpk --summary
5) The long option --summary causes output to be printed within terminal. A file called "results.yml"
   will also be generated and will be located in the same directory.

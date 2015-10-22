# toys
A collection of miscellaneous scripts to solve toy problems and questions.

#### Mutexpuzzle
A computer program accesses an array of 16384 free memory addresses starting with address number 2. 
Each time the program runs it proceeds to the first open memory address (numbered N, starting with 2), 
locks it, and then flips the state of every Nth address thereafter (without locking any of them). 
There are two possible states that can be flipped: free and allocated (lock-free). The program then 
keeps making runs as long as there are free memory addresses; when it is done, some of the addresses 
are locked and others are not.

If there were 16384 addresses, what is the highest-numbered address that is locked when the program is finished?

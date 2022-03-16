# Lab-2
Lab Task: Error detection and recovery

This lab focuses on detection of bit errors and recovering from such errors.

The client generates a NxN matrix of bits, i.e., 0s and 1s only. The client then transmits this matrix to the server. Before transmission, the client may induce a 1-bit error in the data at random. A 1-bit error means 1 is changed to 0 or 0 is changed to 1.

### Programming Tasks
1. The server detects all such 1-bit errors
2. The server run an error correcting code so that it can correct the 1 bit error.

## Execution
First, head over to the right directory which will contain both the `server.py` and `client.py` files.

Then, simply run `python3 server.py` to start the server.

Similarly, run `python3 client.py` to run the client once.

The server will run and bind locally to port `42069` and the client will try and send requests to the same.
# Lab-1
This contains a basic TCP and UDP server and client

Solves the following 2 tasks in each of the protocols
1. Client responds back to the server with an acknowledgment of the server’s
message. 
2. The client generates a set of N random numbers (N is chosen at random between 25 and 100) and sends this list to the server. The numbers are in the range of (1-100). The server examines this list and removes duplicates and sends back the deduplicated set back to the client. The client displays:
- The final list of numbers
-  The list of numbers that were identified as duplicates

## Execution
First, head over to the right directory which will contain both the `server.py` and `client.py` files.

Then, simply run `python3 server.py` to start the server.

Similarly, run `python3 client.py` to run the client once.

The server will run and bind locally to port `42069` and the client will try and send requests to the same.
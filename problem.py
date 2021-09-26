"""
For this problem, you will build a rock-paper-scissors server and client.

The server function will be given a ip address and port number for the server to listen on.
For the server, after a connection is received follow this script:
1. Prompt the user to enter their play: "Rock", "Paper", or "Scissors"
    1a. If the user does not supply one of those strings, give them the same prompt again
2. Randomly choose what your server will play.
3. "Calculate" who won the game.
4. Tell the user their move, the server's move, and who won, along with how how many games each side has won.
5. Prompt the user if they want to play again, either "Yes" or "No".
    5a. If yes, start over from 1.
    5b. If no, tell the user to have a nice day and close the connection.

The client will be given a port number and host to connect to.
Once the client is connected it should play a number of games equal to the games_to_play number provided.
You can choose your play for each round however you want.
"""
import socket
import random


def rps_server(listening_host: str, listening_port: int):
    pass


def rps_client(host: str, port: int, games_to_play: int = 1):
    pass


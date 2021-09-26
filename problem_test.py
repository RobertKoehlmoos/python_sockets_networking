from problem import rps_server, rps_client
import threading
import socket

plays = ("rock", "paper", "scissors")


def test_server():
    port = 9475
    server = threading.Thread(target=rps_server, args=("", port))
    server.start()
    at_end = False
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", port))
        first_request = s.recv(1024).decode("utf-8").lower()
        assert all(play in first_request for play in plays), "Server doesn't prompt for all plays"
        s.sendall(b"Rock")
        response = s.recv(1024).decode("utf-8").lower()
        assert "rock" in response, "Server doesn't show the plays each game"
        assert "0" in response, "Server doesn't display scores correctly"
        s.sendall(b"Yes")
        response = s.recv(1024).decode("utf-8").lower()
        assert "rock" in response, f"Server doesn't show the plays the second round response: {response}"
        s.sendall(b"Romp")
        response = s.recv(1024).decode("utf-8").lower()
        assert all(play in response for play in plays), "Failed to give same prompt when invalid move provided"
        s.sendall(b"Rock")
        s.recv(1024)
        s.send(b"No")
        at_end = True
    assert at_end, "Server exits early"
    server.join()


def test_client():
    port = 3333

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", port))
        s.listen()
        client = threading.Thread(target=rps_client, args=("127.0.0.1", port, 2))
        client.start()
        conn, addr = s.accept()
        with conn:
            conn.send(b"What are ya playing?")
            play = conn.recv(1024).decode("utf-8").lower().strip()
            assert play in plays, f"Invalid client response: {play}"
            conn.send(b"You might have won, Play again?")
            play_again = conn.recv(1024).decode("utf-8").lower().strip()
            assert play_again == "yes", f"Client said {play_again} instead of 'Yes' to playing again after the first round"
            conn.send(b"What are ya playing this time?")
            play = conn.recv(1024).decode("utf-8").lower().strip()
            assert play in plays, f"Invalid client response the second round: {play}"
            conn.send(b"You might have won, Play again?")
            play_again = conn.recv(1024).decode("utf-8").lower().strip()
            assert play_again == "no", f"Client said {play_again} instead of 'No' to playing again after the second round"
    client.join()

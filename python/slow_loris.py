import socket
import sys
import time
import random

log_level = 2

def log(text, level=1):
	if log_level >= level:
		print(text)

list_of_sockets = []

regular headers = [

# Port Scanner Tool

## Project Overview

The Port Scanner Tool is a Python-based application that scans a target IP address or URL to identify which ports within a specified range are open. The tool can be run in both normal and verbose modes, with the latter providing detailed information about the services running on the open ports. It can handle domain names or IP addresses and is designed to provide both a simple list of open ports or a detailed report that includes the associated service names.

This project demonstrates basic network scanning functionality and how to interact with sockets in Python to detect open ports and running services on remote machines.

## Technologies Used

Python: The primary programming language for implementing the port scanning logic.
Socket Library: A built-in Python library used for network communications, allowing for the detection of open ports by attempting connections to specified ports.
Regular Expressions: Used to validate IP addresses, ensuring the input is in the correct format.
Common Ports Mapping: A dictionary of common ports and their associated services, allowing the tool to provide human-readable information in verbose mode.
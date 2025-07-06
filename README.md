# 🚌 Python CAN Logger

A simple Python tool to capture CAN bus messages in real-time and log them to a CSV file using the [`python-can`](https://python-can.readthedocs.io/en/master/) library.

This tool is helpful for debugging and analyzing CAN communication in embedded systems like automotive ECUs, STM32 boards, and other CAN-enabled devices.



## 🚀 Features

- Connects to the CAN bus using a Kvaser interface (configurable)
- Reads live CAN messages and saves them to a `.csv` file
- Logs timestamp, arbitration ID, DLC, and data bytes
- Gracefully exits on keyboard interrupt (`Ctrl+C`)



## 📁 Sample CSV Output

        Timestamp           Arbitration_ID    DLC            Data
2025-07-06 12:43:21.123    0x18FF50E5         8     01 23 45 67 89 AB CD EF


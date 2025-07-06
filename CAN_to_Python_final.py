'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                     CAN to Python Final Code
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import can
import csv
from datetime import datetime


def create_csv_from_can_messages(channel, bitrate, csv_filename):
    bus = can.interface.Bus(channel=channel, bustype='kvaser', bitrate=bitrate ,extended =True)
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Timestamp', 'Arbitration ID', 'DLC', 'Data'])
        try:
            while True:
                message = bus.recv()
                timestamp = datetime.fromtimestamp(message.timestamp).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                arbitration_id = hex(message.arbitration_id)
                dlc = message.dlc
                data = ' '.join(format(byte, '02X') for byte in message.data)

                csv_writer.writerow([timestamp, arbitration_id, dlc, data])

        except KeyboardInterrupt:
            print("User interrupted. Closing CSV file.")
        finally:
            csvfile.close()
            bus.shutdown()

channel = '0'
bitrate = 500000  # 500 kbps 
csv_filename = 'can_messages.csv'

create_csv_from_can_messages(channel, bitrate, csv_filename)



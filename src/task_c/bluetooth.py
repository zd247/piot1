from sense_hat import SenseHat
from src.task_b.monitorAndNotify import MonitorAndNotify as mntf
from res.container import Container as c
import bluetooth
import os
import time
import json


class Bluetooth():
   def __init__ (self):
      self.sense = SenseHat()
      self.target_address = None
      self.mntf = mntf()

   def lookUpNearbyBluetoothDevices(self):
      target_name = "Xperia"
      nearby_devices = bluetooth.discover_devices()
      for bdaddr in nearby_devices:
         if target_name == bluetooth.lookup_name( bdaddr ):
            print(bdaddr)
            self.target_address = bdaddr
            break
         if self.target_address is not None:
            print ("found target bluetooth device with address ", self.target_address)
         else:
            print ("could not find target bluetooth device nearby")

   def receiveMessages(self):
      server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
      
      port = 1
      server_sock.bind(("",port))
      server_sock.listen(1)
      
      client_sock,address = server_sock.accept()
      print("Accepted connection from " + str(address))
      
      data = client_sock.recv(1024)
      print("received [%s]" % data)
      
      client_sock.close()
      server_sock.close()
  
   def sendMessageTo(self, message):
      port = 7
      sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
      if self.target_address is not None:
         sock.connect((self.target_address, port))
         sock.send(message)
         print("Sent")
      else:
         print("No device connected")
         sock.close()

   def execute(self):
      while True:
         self.sense.clear()
         temp, humidity = self.mntf.readDataFromSense()
         humidity = round(humidity, 1)

         self.lookUpNearbyBluetoothDevices()

         if (temp > float(c.min_temp) and temp < float(c.max_temp)):
            message = "Temparture is " + str(temp)
            self.sendMessageTo(message)
         if (humidity > float(c.min_humidity) and humidity < float (c.max_humidity)):
            message = "Humidity is " + str(humidity)
            self.sendMessageTo(message)
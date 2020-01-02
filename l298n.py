#!/usr/bin/python

import RPi.GPIO as GPIO
import time

class L298N:
    def __init__(self, ena_pin, enb_pin, in1, in2, in3, in4):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.ena = ena_pin
        self.enb = enb_pin

        
        GPIO.setmode(GPIO.BOARD)
        
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)
        GPIO.setup(self.ena, GPIO.OUT)
        GPIO.setup(self.enb, GPIO.OUT)

        self.pwma = GPIO.PWM(self.ena, 1000)
        self.pwmb = GPIO.PWM(self.enb, 1000)
        time.sleep(1)

    def driveForward(self):
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.HIGH)
        GPIO.output(self.in4, GPIO.LOW)

    def driveReverse(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.HIGH)

    def breakMotors(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.oupput(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)
    
    def setPulse(self, pulse):
        self.pwma.ChangeDutyCycle(pulse)
        self.pwmb.ChangeDutyCycle(pulse)

    

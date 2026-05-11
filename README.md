# Lumen: Personal Assistant for the Elderly & Visually Impaired

Lumen is a specialized service robot built on the Raspberry Pi platform, specifically designed to foster independence and safety for the elderly and individuals with sight impairments. By combining hardware sensors with AI-driven interaction, Lumen serves as a vigilant and supportive companion in the home environment.
<img width="695" height="927" alt="1000072872" src="https://github.com/user-attachments/assets/561f5e27-8ab4-4d7e-889b-e4c8ee3911d8" />

## 🛠 Core Assistance Features

### 1. Medication & Health Management
* **Accessible Scheduling:** Users can register medication names and set specific dosage intervals through an intuitive graphical interface (see `ekrani.py` and `medicinee.py`).
* **Audible Reminders:** When it is time for a dose, Lumen triggers a high-priority audio alarm (`alarm.mp3`) and a visual popup, ensuring the user is notified even without looking at a screen (see `ekrani.py`).
* **Real-time Countdown:** The system maintains a live countdown for all active medications, helping users or caregivers stay informed about the next scheduled dose (see `ekrani.py`).

### 2. Autonomous Navigation & Obstacle Awareness
* **Blind-Spot Protection:** Using an ultrasonic sensor mounted on a servo-driven "head," the robot scans for obstacles and prevents collisions (see `koka.py` and `obstacle_avoider.py`).
* **Path Following:** Lumen can follow specific floor markers (lines) to navigate reliably and predictably between rooms (see `follow_the_line.py` and `lumen_m.py`).
* **Manual Override:** For complex maneuvers, the robot supports direct keyboard steering (Forward, Backward, Left, Right) with real-time distance feedback (see `roboti.py`).

### 3. Safety & Emergency Response
* **Gas Leak Monitoring:** A dedicated digital sensor constantly monitors the environment for hazardous gas levels (see `gas.py`).
* **Automatic Emergency Calls:** If a leak is detected, Lumen utilizes the Twilio API to automatically place a phone call to a caregiver or emergency contact (see `gas.py` and `telefonate.py`).

### 4. Companion AI & Intelligent Interaction
* **Face Recognition:** An integrated HuskyLens AI camera identifies registered users to provide personalized greetings, such as "Hello, Olseed!" (see `lumen_s.py`).
* **Weather Reports:** The robot fetches live weather data for Tirana and uses OpenAI's GPT models to synthesize natural, spoken descriptions of the forecast (see `lumen_s.py` and `moti.py`).
* **Vocal Feedback:** Communicates status updates and warnings verbally through the Piper and espeak text-to-speech engines (see `lumen_s.py` and `servo.py`).

## 🔧 Hardware & System Architecture
* **Logic & Control:** Raspberry Pi running Python-based sensor integration and scheduling logic (see `lumen_m.py`).
* **Vision & AI:** HuskyLens AI module and OpenAI API for natural language summaries (see `lumen_s.py`).
* **Safety & Connectivity:** Digital gas sensors and Twilio REST API for remote alerting (see `gas.py`).
* **Mobility:** DC motors driven by GPIO PWM and servo motors for expressive movement and scanning (see `lumen_m.py` and `koka.py`).

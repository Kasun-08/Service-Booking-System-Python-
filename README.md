# Car Service Booking System (Python)

## Overview
The **Car Service Booking System** is a console-based Python application that manages vehicle service and repair bookings.  
It supports **customer profile management**, **service scheduling**, and **staff operations** such as viewing bookings, adjusting time slots, and exporting booking data.

The project demonstrates **object-oriented programming**, input validation, file handling, and menu-driven system design using Python.

---

## Features

### Customer Features
- Create and edit customer profiles
- Book vehicle service or repair appointments
- View bookings using vehicle number
- Cancel bookings using reference number

### Staff Features
- Secure staff login system
- Create customer profiles
- Create and cancel bookings
- View bookings by date and branch
- Adjust service time slots
- Export booking details to a text file

---

## Technologies Used
- **Language:** Python 3
- **Libraries:**
  - `datetime` – Date validation
  - `random`, `string` – Reference number generation
- **Paradigm:** Object-Oriented Programming (OOP)

---

## System Design
The system is structured using the following classes:

- **Customer**  
  Stores customer and vehicle information.

- **Booking**  
  Represents a booking with date, time, branch, type, and reference number.

- **BookingSystem**  
  Core logic for managing customers, bookings, validation, staff authentication, and file export.

---

## Booking Rules
- Date format must be **YYYY-MM-DD**
- Service bookings use fixed time slots (`09:00` – `14:00`)
- Maximum **2 bookings per time slot per branch**
- Repair bookings do not require time slot selection

---

## How to Run

### Requirements
- Python **3.8 or later**

### Run the program
```bash
python booking_system.py

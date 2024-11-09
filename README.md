# Object-Oriented-Programming
The goal of this project is to build a Pharmacy Operations Management application using Object-Oriented Programming (OOP) principles. This app will streamline the essential daily tasks of pharmacy staff, including inventory control, order processing, and prescription management

# Pharmacy Operations Management System

This project provides a simple Object-Oriented Python application for managing key operations within a pharmacy. It includes functionality for handling customers, managing medications, restocking inventory, and processing purchases. This project demonstrates core concepts in OOP, including encapsulation, inheritance, and polymorphism.

---

## Project Structure

The code consists of three main classes:

1. **Client**
2. **Medicament (Medication)**
3. **Pharmacie (Pharmacy)**

Each class contains properties and methods that allow the pharmacy to efficiently handle customer and medication data.

### Classes and Methods

#### 1. `Client` Class
   - **Purpose**: Creates and manages client information.
   - **Attributes**:
     - `nom`: Name of the client.
     - `credit`: Client's credit balance.
   - **Methods**:
     - `__str__()`: Displays client details (name and credit).

#### 2. `Medicament` Class
   - **Purpose**: Creates and manages medication information.
   - **Attributes**:
     - `nom`: Name of the medication.
     - `prix`: Price of the medication.
     - `stock`: Quantity of the medication in stock.
   - **Methods**:
     - `__str__()`: Displays medication details (name and stock level).

#### 3. `Pharmacie` Class
   - **Purpose**: Manages pharmacy operations, including customers, medications, and transactions.
   - **Attributes**:
     - `listeclients`: List of `Client` objects in the pharmacy.
     - `listemedicaments`: List of `Medicament` objects in the pharmacy.
   - **Methods**:
     - `affichage`: Displays all clients and medications in the pharmacy.
     - `approvisionnement`: Restocks a specified medication in the pharmacy.
     - `liremedicament`: Checks if a medication is available in the pharmacy.
     - `lireclient`: Checks if a client is registered in the pharmacy.
     - `enregistrement`: Registers a new medication in the pharmacy.
     - `enregistrement_client`: Registers a new client in the pharmacy.
     - `lirequantite`: Verifies if the desired quantity of a medication is available.
     - `achat`: Handles the purchase of a medication, updates stock and client credit accordingly.
     - `quitter`: Terminates the program.

---

## Usage

To use the app, instantiate the `Pharmacie` class with a list of `Client` and `Medicament` objects, then call the various properties to perform operations.

### Example

```python
# Sample clients and medications
clients = [Client("Alice", 500), Client("Bob", 300)]
medicaments = [Medicament("Aspirin", 10, 100), Medicament("Ibuprofen", 15, 50)]

# Instantiate pharmacy
pharmacie = Pharmacie(clients, medicaments)

# Display clients and medications
pharmacie.affichage

# Register new medication
pharmacie.enregistrement

# Process a medication purchase
pharmacie.achat

# Quit program
pharmacie.quitter


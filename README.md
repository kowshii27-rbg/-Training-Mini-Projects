# Training-Mini-Projects

### Task 1: Urban Ride Fare Estimator &quot;FareCalc&quot; (Python Core)

* **Description:** A Python script that calculates ride fares based on travel distance, vehicle category (Economy, Premium, SUV), and time of day. It demonstrates input validation, dictionary mapping, conditional logic (applying a 1.5x surge multiplier during peak hours), and formatted string output.
* **Files:** `farecalc.py`
* **Output:**

<img width="988" height="1600" alt="WhatsApp Image 2026-04-17 at 4 46 02 PM" src="https://github.com/user-attachments/assets/40f6def1-f8dd-4cfe-b5fa-21f5ec6ddf42" />


```text
--- Urban Ride Fare Estimator ---
Enter travel distance (km): 12.5
Enter the time of day (0-23 hours): 18
Select a vehicle category (Economy/Premium/SUV): Premium

===================================
RIDE RECEIPT
===================================
Distance       : 12.50 km
Vehicle Type   : Premium
Base Fare      : 225.00 Rupees
Surge Pricing  : Yes (x1.5)
Final Price    : 337.50 Rupees
===================================


This project was built to demonstrate clean coding practices and modular architecture in Python. Key concepts include:

Technical Understanding:

* Modular Architecture: Clean separation between user input, business logic, and output formatting.
* Robust Error Handling: Uses `try-except` loops to gracefully handle invalid inputs without crashing.
* Clean Code Practices: Replaced messy `if-else` chains with dictionary lookups for O(1) pricing calculations.
* Dynamic Formatting: Uses Python f-strings for precise floating-point alignment on the final receipt.
```
### Task 2: Library Database Management &quot;Digital Library&quot; (SQL)

* **Description:** Demonstrates relational database design and advanced querying. Includes Data Definition Language (DDL) for creating linked tables with Primary and Foreign Keys, and Data Manipulation Language (DML) for multi-table `JOIN`s, aggregations (`GROUP BY`), subqueries, and date-based filtering.
* **Files:** `DigitalLibrary.sql`
* **Query Outcomes:**

```text
1. Table Creation: Successfully creates LibraryStudent, LibraryBooks, and BookLoans.
2. Overdue Logic: Returns [StudentName, BookTitle, IssuedDate] for books kept > 14 days.
3. Popularity Index: Returns [GenreCategory, TotalLoans] sorted by highest popularity.
4. Database Cleanup: Deletes records of students inactive for over 3 years.

Technical Understanding:

* Relational Schema Design: Built a normalized database structure using Primary and Foreign keys to enforce data integrity.
* Multi-Table Joins: Utilized `JOIN` operations to cleanly connect student, book, and transaction records for targeted reporting.
* Data Aggregation: Applied `GROUP BY` and `COUNT` functions to analyze borrowing trends and calculate popularity metrics.
* Targeted Data Cleanup: Wrote dynamic `DELETE` statements using subqueries and the `HAVING MAX()` function to safely prune inactive accounts.

```
### Task 3: Password Strength Validator &quot;SafeLog&quot; (Java Core)

* **Description:** A console-based password validation tool. Demonstrates iterative user input handling with `Scanner`, String traversal, character analysis using the `Character` wrapper class, and dynamically collecting error feedback using an `ArrayList`.
* **Files:** `PasswordValidator.java`
* **Output:**

```text
=== SafeLog Employee Portal ===
Your password must contain: At least 8 characters, 1 uppercase letter, and 1 digit.

Enter your new password: pass
Password Invalid. Please fix the following issues:
   - Too short (must be at least 8 characters).
   - Missing an uppercase letter.
   - Missing a digit (0-9).

Enter your new password: Password
Password Invalid. Please fix the following issues:
   - Missing a digit (0-9).

Enter your new password: SecurePassword123
Success! Password meets all corporate security policies.

Technical Understanding:

* Modular Design: Decoupled the core validation logic (`analyzePassword`) from the user interface (`main` method) for better code organization and testability.
* Dynamic Collections: Utilized Java `ArrayList` to collect and return comprehensive error feedback all at once, rather than stopping at the first failure.
* Character Processing: Implemented `for` loops and the `Character` wrapper class (`isUpperCase`, `isDigit`) to efficiently evaluate individual string elements.
* State Management: Used boolean flags and `while` loops to control application flow and create a seamless user retry mechanism.
```

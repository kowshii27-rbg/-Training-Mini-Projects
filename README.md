# Training-Mini-Projects

### Task 1: Urban Ride Fare Estimator &quot;FareCalc&quot; (Python Core)

* **Description:** A Python script that calculates ride fares based on travel distance, vehicle category (Economy, Premium, SUV), and time of day. It demonstrates input validation, dictionary mapping, conditional logic (applying a 1.5x surge multiplier during peak hours), and formatted string output.
* **Files:** `farecalc.py`
* **Output:**

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
```

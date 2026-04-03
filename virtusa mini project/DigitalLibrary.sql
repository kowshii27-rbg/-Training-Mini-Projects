--1. Table creation
CREATE TABLE LibraryStudent (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(150),
    EmailAddress VARCHAR(150)
);

CREATE TABLE LibraryBooks (
    BookID INT PRIMARY KEY,
    BookTitle VARCHAR(150),
    GenreCategory VARCHAR(150)
);

CREATE TABLE BookLoans (
    LoanID INT PRIMARY KEY,
    StudentID Int,
    BookID int,
    ReturnDate DATE,
    IssuedDate DATE,

    FOREIGN KEY (StudentID) REFERENCES LibraryStudent(StudentID),
    FOREIGN KEY (BookID) REFERENCES LibraryBooks(BookID)
);


--2.overdue logic

SELECT

s.StudentName,
b.BookTitle,
bl.IssuedDate

FROM BookLoans bl
JOIN LibraryStudent s ON bl.StudentID = s.StudentID
JOIN LibraryBooks b ON bl.BookID = b.BookID
WHERE bl.ReturnDate IS NULL
AND bl.IssuedDate < (CURRENTDATE - 14);

--3.popularity index

SELECT

b.GenreCategory,
COUNT(bl.LoanID) AS TotalLoans
FROM LibraryBooks b
JOIN BookLoans bl ON b.BookID = bl.BookID
GROUP BY b.GenreCategory
ORDER BY TotalLoans DESC;

DELETE FROM LibraryStudent
WHERE StudentID IN (
    SELECT StudentID
    FROM BookLoans
    GROUP BY StudentID
    HAVING MAX(IssuedDate) < (CURRENTDATE - INTERVAL '3' YEAR)
);
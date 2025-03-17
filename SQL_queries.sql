-- Create Database
CREATE DATABASE support_ticket_analyzer;

-- Use Database
USE support_ticket_analyzer;

-- Create Table
CREATE TABLE support_tickets (
  ticket_id INT PRIMARY KEY,
  message TEXT,
  category VARCHAR(50)
);

-- Sample Query: View All Tickets
SELECT * FROM support_tickets;

-- Sample Query: Count Tickets Per Category
SELECT category, COUNT(*) AS ticket_count
FROM support_tickets
GROUP BY category;

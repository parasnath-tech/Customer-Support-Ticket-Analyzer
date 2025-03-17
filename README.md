# Customer Support Ticket Analyzer 📝

## Overview  
A Machine Learning-based solution to automatically categorize and analyze customer support tickets. The project leverages **Python NLP**, **SQL databases**, and data automation techniques to streamline support ticket management and extract key business insights.

---

## Features

- **NLP-based categorization:** Uses Python’s Naive Bayes classifier to automatically classify tickets.
- **SQL integration:** Stores categorized tickets in a Railway-hosted MySQL database.
- **Automation:** Reduces manual classification efforts by **50%**.
- **Scalable:** Easily adaptable for large datasets and real-time processing.
- **Optional visualization:** Compatible with Looker Studio or BI tools for trend analysis.

---

## Technologies Used

- **Languages & Libraries:** Python, Pandas, Scikit-learn, MySQL Connector
- **Database:** MySQL (Hosted on Railway)
- **Tools:** GitHub, Railway, VS Code

---

## Project Workflow

1. **Data Preparation:**
   - Created a dataset of 100 customer support tickets.
   - Manually labeled first 30 tickets for training purposes.

2. **Model Training:**
   - Applied **Naive Bayes classifier** using `scikit-learn` to learn ticket categories.
  
3. **Automation:**
   - Predicted categories for remaining tickets.
   - Inserted fully categorized data into **Railway MySQL database**.

4. **Optional Visualization:**
   - Database can be connected to **Looker Studio** for real-time reporting.

---

## Repository Structure

```
Customer-Support-Ticket-Analyzer/
├── support_tickets.csv                  # Raw dataset of support tickets
├── support_tickets_categorized.csv      # Output CSV after categorization
├── ticket_classifier.py                 # Python script for categorizing tickets
├── insert_support_tickets.py            # Python script to insert data into MySQL
├── SQL_queries.sql                      # SQL queries (DB & table creation)
└── README.md                            # Project overview and instructions
```

---

## How to Run the Project

1. Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/Customer-Support-Ticket-Analyzer.git
```

2. Install dependencies:

```
pip install pandas scikit-learn mysql-connector-python
```

3. Update Railway database credentials in `insert_support_tickets.py`.

4. Run scripts:

```
python ticket_classifier.py
python insert_support_tickets.py
```

---

## SQL Table Creation Query

```
CREATE DATABASE support_ticket_analyzer;
USE support_ticket_analyzer;

CREATE TABLE support_tickets (
  ticket_id INT PRIMARY KEY,
  message TEXT,
  category VARCHAR(50)
);
```

---

## License

This project is licensed under the MIT License.

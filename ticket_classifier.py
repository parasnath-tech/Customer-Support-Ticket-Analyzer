import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Read CSV file with manually labeled categories
data = pd.read_csv('support_tickets.csv')

# Step 2: Drop rows without category labels (only first 30 are labeled for now)
labeled_data = data.dropna(subset=['category'])

# Step 3: Vectorize the text data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(labeled_data['message'])

# Step 4: Train Naive Bayes Model
model = MultinomialNB()
model.fit(X, labeled_data['category'])

# Step 5: Predict remaining unlabeled tickets
unlabeled_data = data[data['category'].isnull()]
X_unlabeled = vectorizer.transform(unlabeled_data['message'])
predictions = model.predict(X_unlabeled)

# Step 6: Add predicted categories back to the original data
data.loc[data['category'].isnull(), 'category'] = predictions

# Step 7: Save categorized data to a new CSV file
data.to_csv('support_tickets_categorized.csv', index=False)

print("Categorization completed! Check 'support_tickets_categorized.csv'")

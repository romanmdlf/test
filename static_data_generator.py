import pandas as pd
import random
from faker import Faker

# Initialize Faker and define seed for reproducibility
fake = Faker()
Faker.seed(0)
random.seed(0)

# Regenerate transaction data for each client
num_clients = 1000
num_transactions = 5000  # Total number of transactions
transaction_data = []

products = ['DCM', 'Liquidity', 'RSG & FX', 'Payments', 'Trade & Working Capital']
transaction_types = ['Purchase', 'Refund', 'Interest Payment', 'Fee Charged', 'Transfer']

for _ in range(num_transactions):
    client_id = f"{random.randint(1, num_clients):06d}"
    transaction_data.append({
        'clientid': client_id,
        'transaction_date': fake.date_this_year().strftime("%Y-%m-%d"),
        'product': random.choice(products),
        'transaction_type': random.choice(transaction_types),
        'transaction_amount': round(random.uniform(-5000, 10000), 2),
        'currency': random.choice(['USD', 'GBP', 'EUR']),
        'transaction_status': random.choice(['Completed', 'Pending', 'Failed']),
        'channel': random.choice(['Online', 'Branch', 'Mobile App', 'ATM']),
        'notes': fake.sentence(nb_words=10)
    })

# Create DataFrame
df_transactions = pd.DataFrame(transaction_data)
df_transactions.to_csv("client_history.csv", index=False)

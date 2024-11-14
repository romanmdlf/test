import pandas as pd
import random
from faker import Faker

# Initialize Faker and define seed for reproducibility
fake = Faker()
Faker.seed(0)
random.seed(0)

# Generate fake dataset
num_clients = 1000
client_data = []

regions = ['London', 'Glasgow', 'Manchester', 'Birmingham', 'Edinburgh', 'Liverpool', 'Bristol', 'Leeds']
account_types = ['Savings', 'Checking', 'Investment', 'Mortgage']
employment_status = ['Employed', 'Unemployed', 'Retired', 'Student', 'Self-Employed']
marital_status = ['Single', 'Married', 'Divorced', 'Widowed']

for i in range(1, num_clients + 1):
    client_data.append({
        'clientid': f"{i:06d}",
        'name': fake.name(),
        'dob': fake.date_of_birth(minimum_age=18, maximum_age=85).strftime("%Y-%m-%d"),
        'incomeytd': round(random.uniform(10000, 250000), 2),
        'accountopendate': fake.date_this_decade().strftime("%Y-%m-%d"),
        'region': random.choice(regions),
        'account_type': random.choice(account_types),
        'employment_status': random.choice(employment_status),
        'marital_status': random.choice(marital_status),
        'address': fake.address().replace("\n", ", "),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
        'credit_score': random.randint(300, 850),
        'total_accounts': random.randint(1, 10),
        'account_balance': round(random.uniform(500, 500000), 2),
        'is_premium_member': random.choice([True, False])
    })

# Create DataFrame
df_clients = pd.DataFrame(client_data)

# Display the DataFrame to the user
import ace_tools as tools; tools.display_dataframe_to_user("Client Data for Bank", df_clients)

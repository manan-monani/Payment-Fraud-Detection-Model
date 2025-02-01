import pandas as pd
import random
from datetime import datetime, timedelta
from uuid import uuid4

# Number of records
n = 1_000_000

# Generate sample data
amounts = [random.randint(10_000, 150_000) for _ in range(n)]  # Transaction amounts
user_ids = [f"user_{random.randint(1, 50000)}" for _ in range(n)]  # User IDs

times = [(datetime.now() - timedelta(minutes=random.randint(0, 1440))).isoformat() for _ in range(n)]  # Random timestamps in ISO format

locations = [{"latitude": round(random.uniform(-90, 90), 6), "longitude": round(random.uniform(-180, 180), 6)} for _ in range(n)]  # Latitude and Longitude

device_ids = [str(uuid4()) for _ in range(n)]  # Unique Device IDs

# Ensuring a fraud distribution of 7%
is_fraud = [1 if i < n * 0.07 else 0 for i in range(n)]  # 7% fraud transactions
random.shuffle(is_fraud)

# Create a DataFrame
df = pd.DataFrame({
    'amount': amounts,
    'userID': user_ids,
    'time': times,
    'deviceLocation': locations,
    'deviceID': device_ids,
    'isFraud': is_fraud
})

# File paths
csv_file_path = r'D:\project\Model\fraud_detection_dataset_large.csv'

# Save the dataset
df.to_csv(csv_file_path, index=False)

print(f"CSV file with {n} entries saved at {csv_file_path}")

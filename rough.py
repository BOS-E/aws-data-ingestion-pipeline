import random
import time
from datetime import datetime
import pandas as pd

data_list = []

for i in range(10):
    start_timestamp = time.time()
    end_timestamp = start_timestamp + random.randint(1, 30) * 86400  # Add 1 to 30 days

    start_date_str = time.strftime("%Y-%m-%d", time.localtime(start_timestamp))
    end_date_str = time.strftime("%Y-%m-%d", time.localtime(end_timestamp))

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    duration = (end_date - start_date).days

    data = {
        "bookingId": str(random.randint(100000, 999999)),
        "userId": str(random.randint(1000, 9999)),
        "propertyId": str(random.randint(10000, 99999)),
        "location": f"{random.choice(['New York', 'Los Angeles', 'Chicago'])}, {random.choice(['USA', 'Canada', 'Mexico'])}",
        "startDate": start_date_str,
        "endDate": end_date_str,
        "price": str(random.randint(100, 500)),
        "duration": duration
    }

    data_list.append(data)

# Create DataFrame and print it
df = pd.DataFrame(data_list)
print(df)
print(type(df.duration[0]))
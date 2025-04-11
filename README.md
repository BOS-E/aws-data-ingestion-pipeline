# 🏨 Streaming Booking Data Pipeline (Simulated)

This project simulates a real-time data engineering pipeline for hotel booking data using various AWS services. It is inspired by real-world platforms like Airbnb but uses **mock data** generated within the system.

## 📌 Overview

The pipeline generates fake booking records, filters them based on booking duration, and stores them in Amazon S3. It's designed to demonstrate key cloud-based data engineering concepts such as:

- Event-driven architecture  
- Real-time data ingestion and filtering  
- AWS-native CI/CD deployment  
- Fault-tolerant design using DLQ

## 🛠️ Technologies Used

- AWS Lambda  
- Amazon SQS (with Dead Letter Queue)  
- Amazon EventBridge Pipes  
- Amazon S3  
- AWS CodeBuild  
- Python (for Lambda functions)  

## 📈 Pipeline Flow

1. **Producer Lambda** generates random booking records and sends them to an **SQS Queue**.
2. **EventBridge Pipe** reads from SQS, filters out bookings with duration ≤ 1 day.
3. Filtered data is passed to a **Consumer Lambda**, which stores it as a `.csv` in **Amazon S3**.
4. If Lambda processing fails 3 times, the message is moved to the **DLQ**.
5. **AWS CodeBuild** automates deployment from a GitHub repo.

## 🧪 Sample Booking Data (JSON)

```json
{
  "bookingId": "550e8400-e29b-41d4-a716-446655440000",
  "userId": "user123",
  "propertyId": "prop456",
  "location": "Barcelona, Spain",
  "startDate": "2025-04-01",
  "endDate": "2025-04-05",
  "price": 450
}

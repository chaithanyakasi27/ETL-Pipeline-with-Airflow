
# Real-Time Twitter Data Pipeline with Airflow and AWS
![Real-Time Twitter Data Pipeline with Airflow and AWS](https://raw.githubusercontent.com/chaithanyakasi27/ETL-Pipeline-with-Airflow/refs/heads/main/Bitbucket%20Images/project%20diagram.png)


This project provides a comprehensive solution for capturing, processing, and storing real-time Twitter data using Python, Tweepy, Apache Airflow, and AWS services. The pipeline automates the entire workflow, making it scalable and efficient for handling streaming data from Twitter's API.

## Objectives

1. Extract real-time tweets using the Twitter API and the Tweepy library.
2. Orchestrate data extraction, processing, and storage tasks using Apache Airflow.
3. Store both raw and processed data securely in Amazon S3 for further analysis.
4. Leverage AWS EC2 to host and run the pipeline infrastructure.

## Key Components

### 1. Twitter API Integration:
- Authentication and connection using Tweepy.
- Fetch tweets based on specific keywords, hashtags, or user handles.

### 2. Workflow Automation with Airflow:
- DAGs (Directed Acyclic Graphs) define tasks for data extraction, processing, and storage.
- Airflow schedules and monitors these tasks for reliability.

### 3. AWS Services:
- **EC2**: Hosts Airflow and ensures pipeline availability.
- **S3**: Stores raw tweet data and processed datasets in an organized folder structure for analytics.

### 4. Data Storage:
- Raw tweets are saved in CSV format for flexibility.
- Processed data is stored in CSV or Parquet format for downstream tasks like visualization or machine learning.

### 5. Real-time Processing:
- Tweets are captured and sent through the pipeline as they are posted on Twitter.
- Enables immediate analysis and insights.

## Applications

- Sentiment analysis
- Social media monitoring
- Real-time analytics
- Building datasets for NLP (Natural Language Processing) projects.

---

## First Steps: Setting Up Twitter API Credentials

Follow these steps to configure your Twitter API credentials for the project:

1. **Create a Twitter Account.**
2. **Access the Twitter Developer Portal:**
   - Go to the Twitter Developer Portal.
   - Sign in with your Twitter account.
3. **Create an App:**
   - Navigate to the Apps section in the developer portal.
   - Click on "Create App" and provide the necessary details.
4. **Obtain API Keys and Bearer Token:**
   - Once the app is created, navigate to the Keys and Tokens tab.
   - Copy the following credentials:
     - API Key
     - API Secret Key 
     - Access Token
     - Access Token Secret
     - Bearer Token
5. **Set up Twitter API Credentials in Tweepy:**
   - Use the Tweepy library in your project to authenticate the Twitter API.
   - Add your credentials to the Python script.
6. **Secure Your Credentials:**
   - Avoid hardcoding your API keys in the script. Use environment variables or a configuration file to store them securely.

---

## Prerequisites
![Installation](https://raw.githubusercontent.com/chaithanyakasi27/ETL-Pipeline-with-Airflow/refs/heads/main/Bitbucket%20Images/ubuntu%20installation.png)

1. Python 3.x
2. Pandas (`pip install pandas`)
3. Tweepy (`pip install tweepy`)
4. Apache Airflow (`pip install apache-airflow`)
5. S3FS (Amazon S3 File System)

---

## Implementation Steps

### Twitter_ETL.py Script

1. Create a Python file named `Twitter_ETL.py` in your VS Code environment.
2. Implement the following steps in the script:
   - Extract real-time tweets using the Twitter API (Bearer Token) and the Tweepy library.
   - Specify the username of the user.
   - Step 1: Get the user ID.
   - Step 2: Fetch recent tweets from the user's timeline.
   - Step 3: Extract the tweet data into a structured format.
   - Step 4: Convert the extracted data to a Pandas DataFrame.
   - Step 5: Save the data to a CSV file in Amazon S3.

3. Run the script using the command:
   ```bash
   python Twitter_ETL.py
   ```
   The extracted data will be saved in an S3 bucket in CSV format.

---

## Hosting Airflow on AWS EC2
![EC2 Instance](https://raw.githubusercontent.com/chaithanyakasi27/ETL-Pipeline-with-Airflow/refs/heads/main/Bitbucket%20Images/EC2.png)

### Step 1: Create a VPC
- Configure a public subnet for security and provide public DNS.

### Step 2: Launch EC2 Instance
1. Use an Amazon Machine Image (AMI) such as Ubuntu 22.04 LTS SSD Volume type.
2. Choose a free-tier eligible instance (e.g., `t3.medium`).
3. Create a key pair and download the `.pem` file.
   - Key pair name: Use RSA and private key file format.
4. Select an existing VPC and subnet, and allow HTTPS and HTTP traffic from the internet.
5. Launch the EC2 instance.

### Step 3: Connect to EC2 Instance
![Connect EC2](https://raw.githubusercontent.com/chaithanyakasi27/ETL-Pipeline-with-Airflow/refs/heads/main/Bitbucket%20Images/Ec2%20Connect%20to%20instance.png)
1. Set the instance state to "Running".
2. Use the SSH client to connect to the instance with the command:
   ```bash
   ssh -i "airflow_ec2_key.pem" ubuntu@<EC2-Public-IP>
   ```

### Step 4: Install Required Packages
Run the following commands on the EC2 instance:
```bash
sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow pandas s3fs tweepy
```

### Step 5: Start Airflow
Run the command:
```bash
airflow standalone
```
Save the displayed username and password for logging into the Airflow web interface.

### Step 6: Access Airflow
- Copy the Public IPv4 DNS of the EC2 instance and paste it into your browser.
- Log in using the saved credentials.

---

## Setting Up S3
![S3](https://raw.githubusercontent.com/chaithanyakasi27/ETL-Pipeline-with-Airflow/refs/heads/main/Bitbucket%20Images/S3_bucket_output.png)

1. Create an S3 bucket and organize the folder structure.
2. Copy the S3 folder URL and paste it into the `Twitter_ETL.py` file.

---

## Integrating Airflow and the Pipeline
![Airflow](https://raw.githubusercontent.com/chaithanyakasi27/ETL-Pipeline-with-Airflow/refs/heads/main/Bitbucket%20Images/Dag_tiggers.png)

1. Create a DAG Python file and upload it to Airflow.
2. Use the following steps to structure the pipeline:
   - Import `Twitter_ETL` and define tasks in the DAG file.
   - Upload the files to the Airflow DAGs directory.
3. Refresh Airflow to view the `twitter_dag` file.
4. Trigger the DAG and monitor execution through the logs.
5. Upon successful execution, the processed data will be saved in the S3 bucket.

---

## Conclusion

This project sets up an end-to-end real-time Twitter data pipeline using Airflow and AWS. It enables robust data extraction, processing, and storage workflows suitable for various applications like sentiment analysis, social media monitoring, and real-time analytics.

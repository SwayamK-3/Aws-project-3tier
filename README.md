# Aws-project-3tier
AWS  project to host static website using various aws services.

AWS 3-Tier Web Application – Feedback Management System
Project Overview

This project demonstrates the implementation of a 3-Tier Web Application Architecture using AWS Cloud services.
The application is a serverless feedback management system where users can submit feedback through a web interface, and the data is securely processed and stored using AWS managed services.
The project follows industry best practices by separating the Presentation Layer, Application Layer, and Data Layer, ensuring scalability, security, and high availability.
-------------------------------------------------------------------------------------------------------------------------------------
Architecture Overview (3-Tier Design)
1️ Presentation Layer (Frontend Tier)

Built using HTML, CSS, and JavaScript

Hosted on Amazon S3 Static Website Hosting

Publicly accessible via an S3 bucket policy

Collects user input (Name, Email, Feedback)

Sends data to backend via API Gateway
---------------------------------------------------------------
2️ Application Layer (Backend Tier)

Implemented using AWS Lambda (Python)

Triggered by Amazon API Gateway

Handles:

Input validation

Business logic

Error handling

CORS configuration

Serverless design ensures no server management and automatic scaling
-----------------------------------------------------------------------------------
3️ Data Layer (Database Tier)

Uses Amazon DynamoDB

Fully managed NoSQL database

Stores feedback records with:

Unique ID

Name

Email

Feedback content

Highly scalable, durable, and low-latency storage
-------------------------------------------------------------------------------
Detailed Workflow

1. User opens the web application hosted on Amazon S3

2. User fills out the feedback form and clicks Submit

3. JavaScript sends a POST request to API Gateway

4. API Gateway forwards the request to AWS Lambda

5. Lambda function:

Parses and validates request data

Stores feedback in DynamoDB

Returns success or error response

6. Frontend displays confirmation message to the user

----------------------------------------------------------------
AWS Services Used         Service	Purpose
Amazon S3	             Static website hosting
Amazon API Gateway	      REST API endpoint
AWS Lambda	                Backend logic
Amazon DynamoDB	            Data storage
IAM	                 Access control and permissions


--------Security Considerations-------------------------

IAM roles with least privilege access

Public access limited only to S3 website content

Backend services secured through IAM policies

CORS enabled for controlled frontend-backend communication

----------Deployment Summary-------------------------------------------------

---> Create an S3 bucket and enable static website hosting

---> Upload frontend files (HTML, CSS, JS)

---> Configure bucket policy for public read access

---> Create a DynamoDB table

---> Develop Lambda function and attach DynamoDB permissions

---> Create API Gateway REST API and integrate Lambda

---> Update frontend API endpoint URL

-----------------------------------------------------------------------------------------------------------
Conclusion :--

This AWS 3-Tier Feedback Management System showcases how modern cloud applications can be built using serverless technologies while maintaining scalability, security, and clean architectural separation. It reflects real-world enterprise design patterns commonly used in production environments.


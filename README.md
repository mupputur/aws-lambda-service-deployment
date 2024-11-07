# Project Overview 
     

# AWS Lambda Deployment with AWS SAM
  The serverless Lambda function is defined with customer data, and when a user inputs a customer `id` in the event JSON, the Lambda function returns the corresponding customer data. For Lambda function deployment, we used an AWS CloudFormation Template (CFT) and employed the AWS Serverless Application Model (SAM) CLI to deploy the function from the local environment to the AWS Management Console


## Setup & Installation 

Clone : 

1. Install python version 3.11 
For Windows 

For Mac 

For Linux : 

2. Create virtual environemnt  

3.  Activate Virtual Environment 

4.  Install depdenecies 


Prereqsite  : 

- Install AWS CLI :   DOC REF  
- COnfigure AWS :  
- INSTAL SAM SLI


## Project Structure

 * [src](./src)
   * [file21.ext](./dir2/file21.ext)
   * [file22.ext](./dir2/file22.ext)
   * [file23.ext](./dir2/file23.ext)
 * [dir1](./dir1)
   * [file11.ext](./dir1/file11.ext)
   * [file12.ext](./dir1/file12.ext)
 * [file_in_root.ext](./file_in_root.ext)
 * [README.md](./README.md)
 * [dir3](./dir3)

## Key Files and Their Purpose
- template.yaml: AWS SAM template defining the Lambda function and necessary IAM permissions.
main.py

tests
awsUtils - The purpose of this package is to define the common utilities specific to aws resources 
commonUtils - To define common utilities for 

## Prerequisites
Before deploying the application, ensure the following tools are installed and configured on your machine:
**AWS CLI**
**AWS SAM CLI**

After the installation, configure your AWS CLI with your credentials by entering the following command in your terminal or cmd:
`aws configure`
You’ll be prompted to enter your AWS Access Key ID, Secret Access Key, default region, and output format.

## Deployment Instructions
### Step 1: Clone the Repository
Clone the repository to your local machine.

### Step 2: Package and Deploy with SAM
Use the AWS SAM CLI to package and deploy the application. This process will upload the Lambda function code to S3 and deploy the application via CloudFormation.

- Package the Application: SAM will create a packaged template with an S3 URI for your Lambda function code.
`sam package --template-file template.yaml --output-template-file packaged.yaml --s3-bucket your-sam-bucket-name`
- Replace your-sam-bucket-name with your S3 bucket name. SAM will upload the Lambda code (`src/` folder) to the specified bucket and output the packaged.yaml file.

- Deploy the Packaged Template:
`sam deploy --template-file packaged.yaml --stack-name customerDataLambda --capabilities CAPABILITY_IAM`
- customerDataLambda is the name of your CloudFormation stack. You can change it by renaming with different name.
- --capabilities CAPABILITY_IAM allows SAM to create necessary IAM roles for Lambda.

### Step 3: Verify Stack Creation
Once the deployment is complete, check the CloudFormation stack in the AWS Console:
- Go to the CloudFormation Console and locate customerDataLambda (or your chosen stack name).
- Navigate to the Outputs tab to find the Lambda function's ARN and other deployment details.

### Step 4: Test the Lambda Function 
You can test the Lambda function from the AWS Console or AWS CLI. The function expects an event with the following structure:
```JSON
{
    "id": "12345"
}
```
Testing in AWS Console
- Open the Lambda function in the AWS Console.
- Go to the Test tab.
- Click Create a new test event and enter the sample JSON above.
- Click Test to invoke the function.
The expected response should look like this:

```JSON
{
  "statusCode": 200,
  "body": "{\"customerID\": \"12345\"}"
}
```

## PR Release Guidelines 

1.  Format 
2. 
To ensure the template is correct, you can validate it before deployment:
`aws cloudformation validate-template --template-body file://template.yaml --region us-east-1`
If successful, this command should confirm the template's validity.

cf
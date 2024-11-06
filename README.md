# AWS Lambda Deployment with AWS SAM

This repository contains a simple AWS Lambda function that returns the `customer_id` from an incoming event. The Lambda function is deployed using AWS Serverless Application Model (SAM) in a CloudFormation stack.

## Files in This Repository

- **main.py**: Contains the Lambda function code (`lambda_handler`), which extracts and returns the `customer_id` from an incoming event.
- **template.yaml**: AWS SAM template to define and deploy the Lambda function and necessary IAM permissions.

## Prerequisites

- AWS CLI installed and configured with access to your AWS account
- AWS SAM CLI installed
- A configured S3 bucket to store the Lambda function code package

## Deployment Steps
After you clone the repository and install the dependencies in the requirements.txt file, follow the steps

### Step 1: Zip and Upload main.py file to S3

### Step 2: Modify the Lambda Function Code Path
  Update the `CodeUri` in `template.yaml` to specify the S3 location where the Lambda function code will be uploaded.
  - **template.yaml**
  Resources:
      AwsLambdaServiceDeployment:
        Type: AWS::Serverless::Function
        Properties:
          CodeUri: s3://your-bucket-name/path/to/code.zip  # Update it with your S3 URI
          Handler: main.lambda_handler
          Runtime: python3.12

### Step 3: Validate the CloudFormation Template
Before deploying, validate the template:
aws cloudformation validate-template --template-body file://template.yaml --region us-east-1
If successful, this command should return a JSON output confirming template validation.

### Step 4: Deploy the  stack
Deploy the CloudFormation stack using the AWS Console:
1. Go to the AWS CloudFormation Console.
2. Click Create stack > with new resources (standard).
3. Under Specify template, choose upload a template file, select template.yaml, and click Next.
4. Enter a Stack name (e.g., customerDataLambda).
5. Acknowledge IAM permissions and click create stack.

### Step 5: Verify the Stack Creation
Once the stack is created, navigate to the Outputs section in the stack details to find the Lambda function's ARN and other details.

### Step 6: Test the Lambda Function
You can test the Lambda function through the AWS Console.

The lambda function expects an event with the below structure
{
  "customers": {
    "id": "12345"
  }
}

Testing in the AWS Console
1. Open the Lambda function in the AWS Console.
2. Go to the Test tab.
3. Click Create a new test event.
4. Enter the sample input JSON above and save.
5. Click Test to invoke the function and check the response.

Check the output in the next tab i..e `Execution results`, you should get the below response:

{
    "statusCode": 200,
    "body": "{\"customerID\": \"12345\"}"
}
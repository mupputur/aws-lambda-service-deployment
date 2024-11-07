# AWS Lambda Deployment with AWS SAM
This repository contains an AWS Lambda function that returns a customer_id from an incoming event. The Lambda function is deployed using AWS Serverless Application Model (SAM) within a CloudFormation stack.

## Files in This Repository
- template.yaml: AWS SAM template defining the Lambda function and necessary IAM permissions.
- README.md: Documentation file providing setup and deployment instructions.
- src: Contains the source code and dependencies for the Lambda function.
  - awsUtils: (Empty folder)
    - __init__.py:  (Empty file)
  - commonUtils: (Empty folder)
    - __init__.py:  (Empty file)
  - __init__.py:  (Empty file)
  - main.py: The main Lambda function code (lambda_handler) to extract and return the customer_id from an incoming event.
  - requirements.txt: (Exmpty foler) List of Python dependencies required by the Lambda function.

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
  "customers": {
    "id": "12345"
  }
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

## Optional: Validate the CloudFormation Template
To ensure the template is correct, you can validate it before deployment:
`aws cloudformation validate-template --template-body file://template.yaml --region us-east-1`
If successful, this command should confirm the template's validity.
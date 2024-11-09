# Project Overview 

# AWS Lambda Deployment with AWS SAM
  The serverless Lambda function is defined with customer data, and when a user inputs a customer `id` in the event JSON, the Lambda function returns the corresponding customer data. For Lambda function deployment, we used an AWS CloudFormation Template *(CFT)* and employed the AWS Serverless Application Model *(SAM)* CLI to deploy the function from the local environment to the AWS Management Console

## Setup & Installation 
**Cloning the Repository:**
1. Open a Terminal *(macOS/Linux)* or Command Prompt/PowerShell *(Windows)*.
2. Ensure Git is installed by typing the below command:
    ```
    git --version
    ```
If it isn't installed, follow the Git installation guide.

3. Clone the repository using the git clone command:
    ```
    git clone https://github.com/mupputur/aws-lambda-service-deployment.git
    ```
4. Navigate to the directory with:
    ```
    cd lambda-service-deployment
    ```
**Python Installation**

For Windows: 
- Follow this link to install Python: [Python](https://www.python.org/)

For MacOS:
- Open Terminal.
- Use Homebrew (if not installed, follow [brew.sh](https://brew.sh/)) to install Python
  ```
  brew install python
  ```
- Verify installation 
  ```
  python3 --version
  ```

For Linux : 
- Open Terminal and Update the package list:
  ```
  sudo apt update
  ```
- Install python: 
  ```
  sudo apt install python3 python3-pip
  ```
- Verfiy installation 
  ```
  pyhon3 --version
  ```

**To verify Installation (Windows/Linux/MacOS)**
```
python --version 
```
or 
```
python3 --version
```
**Create virtual environemnt (Windows/Linux/MacOS)**
- This will create a virtual environment named myenv in the current directory.
  ```
  python -m venv myenv
  ```

**Activate Virtual Environment** 

For Windows:
- In cmd 
  ```
  myenv\Scripts\activate
  ```
- In PowerShell 
  ```
  .\myenv\Scripts\Activate
  ```
For MacOS/Linux:
- In terminal 
  ```
  source myenv/bin/activate
  ```

**Install depdenecies (Windows/Linux/MacOS)** 
- In terminal 
  ```
  Pip install package-name
  ``` 
Replace `package-name` with the name of the package you want to install.

## Project Structure

 * [src](./src)
   * [awsUtils](./src/awsUtils)
      * [\_\_init_\_\.py](./src/awsUtils/__init__.py)
   * [commonUtils](./src/commonUtils/__init__.py)
      * [\_\_init_\_\.py](./src/commonUtils/__init__.py)
   * [\_\_init_\_\.py](./src/__init__.py)
   * [lambda_function.py](./src/lambda_function.py)
   * [requirements.txt](./src/requirements.txt)
 * [tests](./tests)
   * [test_lambda_function.py](./tests/test_lambda_function.py)
 * [README.md](./README.md)
 * [template.yaml](./template.yaml)

## Key Files and Their Purpose
1. template.yaml: AWS SAM template defining the Lambda function and necessary IAM permissions.
2. lambda_function.py: The main Lambda function code (`lambda_handler`) to extract and return the `customer_id` from an incoming event.
3. test-lambda_function.py: executes test cases to validate the Lambda function’s behavior and ensure expected outcomes from various input events.
4. awsUtils: The purpose of this package is to define the common utilities specific to aws resources 
5. commonUtils: The purpose of this package is to define the common utilities specific to local operations. 

## Prerequisites
Before deploying the application, ensure the following tools are installed and configured on your machine:

- Install **AWS CLI** & **AWS SAM CLI**. DOC REF: [VDAC TechDocs](https://docs.google.com/document/d/1aGymLtfXVnkxhYE_7wasWwSuBNwAwBy8/edit?usp=sharing&ouid=106368174545171611925&rtpof=true&sd=true)
- After the installation, configure the AWS with your credentials by entering the following command in your terminal or cmd:

  ```
  aws configure
  ```
You’ll be prompted to enter your AWS Access Key ID, Secret Access Key, default region, and output format.

## Deployment Instructions
### Step 1: Clone the Repository
- Clone the repository to your local machine.
DOC REF: [VDAC TechDocs](https://docs.google.com/document/d/1T3Z-dE1C1Qa3MZDvagxDn8Vm-6tbWaZCMO_SnkVzALo/edit?usp=sharing)
### Step 2: Package and Deploy with SAM
Use the AWS SAM CLI to package and deploy the application. This process will upload the Lambda function code to S3 and deploy the application via CloudFormation.
- Package the Application: SAM will create a packaged template with an S3 URI for your Lambda function code.
  ```
  sam package --template-file template.yaml --output-template-file packaged.yaml --s3-bucket your-sam-bucket-name
  ```
- Replace `your-sam-bucket-name` with your S3 bucket name. SAM will upload the Lambda code (`src/` folder) to the specified bucket and output the `packaged.yaml` file.
- Deploy the Packaged Template:
  ```
  sam deploy --template-file packaged.yaml --stack-name customerDataLambda --capabilities CAPABILITY_IAM
  ```
  - `customerDataLambda` is the name of your CloudFormation stack. You can change it by renaming with different name.
  - `--capabilities CAPABILITY_IAM` allows SAM to create necessary IAM roles for Lambda.

### Step 3: Verify Stack Creation
Once the deployment is complete, check the CloudFormation stack in the AWS Console:
- Go to the CloudFormation Console and locate customerDataLambda (or your chosen stack name).
- Navigate to the Outputs tab to find the Lambda function's ARN and other deployment details.

### Step 4: Test the Lambda Function 
You can test the Lambda function from the AWS Console. The function expects an event with the following structure:

**Testing in AWS Console**
- Open the Lambda function in the AWS Console.
- Go to the Test tab.
- Click Create a new test event and enter the sample JSON below.
  ```JSON
  {
      "id": 1
  }
  ```
- Click Test to invoke the function.
The expected response should look like this:

  ```JSON
  {
    "statusCode": 200,
    "body": "{\"id\": 1, \"email\": \"isidro_von@hotmail.com\", \"name\": \"Torrey Veum\", \"company\": \"Hilll, Mayert and Wolf\"}"
  }
  ```
## PR Release Guidelines 
- DOC REF: [VDAC TechDocs](https://docs.google.com/document/d/1sVLKaCtT399pW7XGwI5HSrOWQ-DqruK3F7rmcV87MY0/edit?usp=sharing)

- To ensure the template is correct, you can validate it before deployment:
  ```
  aws cloudformation validate-template --template-body file://template.yaml --region us-east-1
  ```
  If successful, this command should confirm the template's validity.
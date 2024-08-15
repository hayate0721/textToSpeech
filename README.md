# Text-to-Speech Lambda Function with Amazon Polly

This AWS Lambda function converts input text into speech using Amazon Polly and stores the resulting audio file in an S3 bucket. It returns a URL for accessing the generated audio file.

## Features

- Converts text to speech using Amazon Polly.
- Stores the synthesized audio in an S3 bucket.
- Returns a URL to access the audio file.

## Prerequisites

Before deploying and using this Lambda function, make sure you have the following:

- AWS account with necessary permissions for Lambda, Polly, and S3.
- S3 bucket created to store the generated audio files.
- AWS CLI configured with appropriate credentials.

## Setup

1. **Create an S3 Bucket**: 
   - Create an S3 bucket that will be used to store the Polly-generated audio files. Make sure the bucket allows public access if you want to share the audio files publicly.

2. **Deploy the Lambda Function**:
   - Go to the AWS Management Console and create a new Lambda function.
   - Copy the code from `lambda_function.py` into the Lambda editor.
   - Attach the necessary roles to the Lambda function, granting it permissions to use Polly and upload files to the S3 bucket.

3. **Set Environment Variables**:
   - Set up environment variables in your Lambda function for the S3 bucket name if you want to avoid hardcoding the bucket name in the function code.

4. **Test the Function**:
   - You can test the function using the AWS Lambda console by providing a sample event payload with a `text` field.

## Permissions

Ensure that your Lambda function has the necessary permissions to:

- Use Amazon Polly to synthesize speech.
- Write objects to your S3 bucket.

You can attach an IAM role to the Lambda function with the following policies:

- `AmazonPollyFullAccess`
- `AmazonS3FullAccess` (or more restrictive policies if needed)

## Notes

- You can change the `VoiceId` parameter in the `polly.synthesize_speech` call to use different voices provided by Amazon Polly.
- Make sure your S3 bucket policy allows public access if you intend to share the audio files with a wider audience.
- Consider implementing additional error handling and logging to make the function more robust.


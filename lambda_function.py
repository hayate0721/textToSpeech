import boto3
import json

# Initialize Polly and S3 clients
polly = boto3.client('polly')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Ensure the text key is present in the event
    if 'text' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: The event must include a "text" field.')
        }

    # Retrieve the text from the event
    text = event['text']

    try:
        # Use Amazon Polly to synthesize speech
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            VoiceId='Joanna'  # You can change this to any available voice
        )

        # Save the audio stream to an S3 bucket
        s3_bucket = 'polly-text-to-audio-bucket'  # Replace with your S3 bucket name
        s3_key = 'polly_output.mp3'  # Define a unique name for the output file

        # Read the audio stream from Polly's response
        audio_stream = response['AudioStream'].read()

        # Upload the audio stream to S3 without setting ACL
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=audio_stream)

        # Generate the S3 URL for the uploaded file
        s3_url = f"https://{s3_bucket}.s3.amazonaws.com/{s3_key}"

        # Return a success message with the URL
        return {
            'statusCode': 200,
            'body': json.dumps(f"Audio file saved to S3. Access it here: {s3_url}")
        }
    except Exception as e:
        # Handle errors gracefully
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error generating or saving audio: {str(e)}")
        }

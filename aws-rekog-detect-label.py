import boto3

if __name__ == "__main__":

    #imageFile='moviestar.jpg'
    photo='moviestar.jpg'
    bucket='prasrekog'
    client=boto3.client('rekognition')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    
    #with open(imageFile, 'rb') as image:
    #response = client.detect_labels(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + photo)    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))

    print('Done...')
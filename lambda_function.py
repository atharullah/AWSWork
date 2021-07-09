import boto3

s3 = boto3.client('s3')

def lambda_handler(event,context):
    try:
        print("First commit from github")

        # Get the object from the event and show its content type
        bucketName = event['Records'][0]['s3']['bucket']['name']
        fileName = event['Records'][0]['s3']['object']['key']
        #input_file = os.path.join(bucketName,fileName)
        print(bucketName)
        print(fileName)
        # basewidth = 300
        # img = Image.open(input_file)
        # wpercent = (basewidth / float(img.size[0]))
        # hsize = int((float(img.size[1]) * float(wpercent)))
        # img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        # img.save('resized_image.jpg')

        return "Success"
    except Exception as e:
        print(e)
        raise e
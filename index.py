import boto3
aws_access_key_id = "AKIAU4EQQIVLWXJV5ACA"
aws_secret_access_key = "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"

dynamodb = boto3.resource('dynamodb', region_name='eu-central-1',
                                  aws_access_key_id=aws_access_key_id,
                                  aws_secret_access_key=aws_secret_access_key)
table_name = 'authors'
table = dynamodb.Table(table_name)

response = table.scan()

html_content = '<ul>'
for item in response['Items']:
    html_content += f'<li>{item["author_name"]} - {item["book_title"]}</li>'
html_content += '</ul>'

with open('/var/www/html/index.html', 'w') as f:
    f.write(html_content)

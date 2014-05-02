### AWS credentials: ####
# Change entries here to match your own #
# Get values for the first two entries from the "Security crediential" Tab
# Under in the menu under your name.
aws_access_key_id='AKIAIGQBGRALIYCT7GDA'
aws_secret_access_key='jfDF9hs/I9fizs/6XV+fx0AkiOqXs4F7q7CE/lzt'
# Get the Keypair in the EC2 Dashboard page.
#keyPairFile="~/.ssh/aws_key.pem" # name of file keeping local key
keyPairFile="/Users/xinxin/.ssh/aws_key.pem" # name of file keeping local key
key_name="aws_key" # name of keypair (not name of file where key is stored)
# Set the security group On the EC2 page (You will need to add IP addresses if
# you want to connect from a place previously unauthorized.
security_groups=['xinxin']
### End of AWS credentials ####

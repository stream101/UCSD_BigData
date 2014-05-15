import pickle
vault='/Users/xinxin/Course/bigdata/Vault'
with open(vault+'/RootCred.pkl','wb') as pickle_file:
    pickle.dump({'ID':'x7jin','key_id':'AKIAITGKSGQB3ICTPZWA','secret_key':'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',\
                 'password':'123',\
                 'ssh_key_name':'aws_key',\
                 'ssh_key_pair_file':'/Users/xinxin/.ssh/aws_key.pem',\
                 'security_groups':'xinxin'}
                ,pickle_file)

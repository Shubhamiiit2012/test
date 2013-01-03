from boto.ec2.connection import EC2Connection
import boto

AWS_ACCESS_KEY_ID = 'AKIAIKGBMWUN7KOJ5PEQ'
AWS_SECRET_ACCESS_KEY = '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'

def main():
    conn=EC2Connection(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
    
    rs=conn.get_all_volumes()
    print(len(rs))

if __name__=='__main__':
    main()

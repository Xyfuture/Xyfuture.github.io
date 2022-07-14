import os,sys
import datetime

if __name__ == "__main__":
    os.system('git add -A')
    os.system('git commit -m "commit all {}"'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    os.system('git push origin main')
    print("push to remote")
import sys
import os
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/dynwebhook', methods=['POST'])
def dynwebhook():
 param = request.data.decode("utf-8")

 print("called dyn webhook:" + str(param)); sys.stdout.flush()
 os.system("./dynwebhook.sh "+param)
 return '', 200


if __name__ == '__main__':
 app.run(host="0.0.0.0",port=8090)


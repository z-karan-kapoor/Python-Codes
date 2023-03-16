from flask import Flask, request
from get_post_req import requests_op



obj=requests_op()


requests_op.app.run(debug=True)
from flask import Flask
app = Flask('app')

@app.route('/')
def customer_churn_prediction(main):
  return main

app.run(host='0.0.0.0', port=8080)
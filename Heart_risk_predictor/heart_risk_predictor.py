from flask import Flask,render_template,request
import joblib
import numpy as np

model=joblib.load('heart_risk_Linear_regression.sav')

app=Flask(__name__)

@app.route('/')
def index():
	return render_template('patient_details.html')

@app.route('/getresults',methods=["POST"])
def getresults():
	
	result=request.form
	
	name=result['name']
	gender=float(result['gender'])
	age=float(result['age'])
	tc=float(result['tc'])
	hdl=float(result['hdl'])
	sbp=float(result['sbp'])
	smoke=float(result['smoke'])
	bpm=float(result['bpm'])
	diab=float(result['diab']) 

	test_data=np.array([gender,age,tc,hdl,smoke,bpm,diab]).reshape(1,-1)
	predicted_target=model.predict(test_data)

	resultDict={"name":name,"risk":round(predicted_target[0],2)}

	return render_template('patient_result.html',results=resultDict)

app.run(debug=True)
	
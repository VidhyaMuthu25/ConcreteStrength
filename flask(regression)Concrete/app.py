from flask import Flask, request, jsonify, render_template
from joblib import load
app = Flask(__name__)
model=load('pro1.save')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    
    '''
    For rendering results on HTML GUI
    '''
    
    x_test = [[int(x) for x in request.form.values()]]
    #print(x_test)
    
    prediction = model.predict(x_test)
    output=prediction[0]
   
    
    return render_template('index.html', prediction_text='Concrete strength {}'.format(output))

'''@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    #For direct API calls trought request
    
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)'''

if __name__ == "__main__":
    app.run(debug=True)

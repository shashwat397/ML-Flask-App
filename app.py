from flask import Flask,render_template,request
app = Flask(__name__)
import pickle
# from sklearn.externals import joblib
model = pickle.load(open('model.pkl','rb'))

@app.route('/',methods = ['GET','POST'])
def pred():
    if request.method == 'POST':
        # try:
            params = request.form
            duration = int(params['duration'])
            color = int(params['color'])
            breed = float(params['breed'])
            x1 = int(params['x1'] )  
            x2 = int(params['x2'])
            condition = int(params['condition'])
            length, height = 0, 0
            result = model.predict([[breed,length, height, duration, color, x1, x2, condition]])
            return render_template('result.html',result = result)
        # except:
        #     return render_template('index.html')

    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug = True)
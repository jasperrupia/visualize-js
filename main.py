
from flask import Flask , render_template
  
app = Flask(__name__) #creating the Flask class object   
 

@app.route('/chartjs') 
def chartJs():  
    return render_template('chartjs.html');  

@app.route('/apexcharts') 
def apexCharts():  
    return render_template('apexcharts.html');  


if __name__ =='__main__':  
    app.run(debug = True) 
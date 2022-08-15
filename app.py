
from flask import Flask , render_template
  
app = Flask(__name__) #creating the Flask class object   
 

@app.route('/') 
def index():   
    return 'Welcome you'; 


@app.route('/chartjs') 
def chartJs():  
    return render_template('chartjs.html')  


@app.route('/googlechart')  
def googleChart():  
    return render_template('googlechart.html')


@app.route('/plotly')  
def plotly():  
    return render_template('plotly.html')


@app.route('/apexcharts')  
def apexCharts():  
    return render_template('apexcharts.html')


@app.route('/d3') 
def d3():  
    return render_template('d3.html') 


if __name__ =='__main__':   
    app.run(debug = True)  


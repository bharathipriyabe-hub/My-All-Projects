from flask import Flask ,render_template,request,redirect,url_for
app=Flask(__name__)
products={}
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/products')
def product_list():
    return render_template('product.html',products=products)
@app.route('/add_product',methods=['POST'])
def add_product():
    pid=request.form['pid']
    name=request.form['name']
    price=request.form['price']
    products[pid]={'name':name,'price':price}
    return redirect(url_for('product_list'))
@app.route('/delete_product/<pid>')
def delete_product(pid):
    if pid in products:
        del products[pid]
    return redirect(url_for('product_list'))
@app.route('/edit_product/<pid>',methods=['GET','POST'])
def edit_product(pid):
    if request.method=='POST':
       name=request.form['name']
       price=request.form['price']
       products[pid]={'name':name,'price':price}
       return redirect(url_for('product_list'))
    else:
        product=products.get(pid)
        return render_template('edit_product.html',pid=pid,product=product)
if __name__=='__main__':
    app.run(debug=True)


    
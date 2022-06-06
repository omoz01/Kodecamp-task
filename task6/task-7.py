from home.models import Product

#open the command propmt
#navigate to the project folder and activate the virtual environment
#run "python manage.py shell"
#run "from home.models import Product"
#run 'x = Product(product_category="furniture", product_name="office table", product_price=200000)'
#this line of code means; youve assigned 200000 for a office table in the furniture category
#then run "x.save()" to save the data in the Product database
#run "Product.object.all()" to get all the database in the Product table.
#run "Product.objects.filter(product_name="office table")" to filter by the product name
#you can a single record from the table by runnig "x= Product.objects.all()" then "x.first()" or put any position you desire to the record
#To change a product price, make sure you filter out the product for example by running
#"x = Product.objects.filter(product_name="office table").filter(product_category="furniture").first()"
#then run "x.product_price" to crosscheck the price before changing it, then run "x.product_price=800000" to change it.
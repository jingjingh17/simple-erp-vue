import sqlite3
import random
from faker import Faker

# 初始化 Faker
fake = Faker('zh_CN')

# 连接到 SQLite 数据库（如果文件不存在，会自动创建）
conn = sqlite3.connect('./app/simple_erp.db')
cursor = conn.cursor()

# 插入数据的函数
def insert_customers(num_records):
    for _ in range(num_records):
        name = fake.company()
        contact_name = fake.name()
        contact_email = fake.email()
        contact_phone = fake.phone_number()
        address = fake.address()
        city = fake.city()
        country = fake.country()
        cursor.execute('''
        INSERT INTO Customers (CustomerName, ContactName, ContactEmail, ContactPhone, Address, City, Country)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        ''', (name, contact_name, contact_email, contact_phone, address, city, country))

# 插入产品数据
def insert_products(num_records):
    product_names = [
        '笔记本电脑', '智能手机', '平板电脑', '显示器', '键盘', '鼠标', '打印机', '扫描仪',
        '耳机', '音箱', '充电器', '移动电源', '硬盘', '内存条', '显卡', '处理器', '主板', '机箱',
        '散热器', '电源适配器', '路由器', '交换机', '网络摄像头', 'U盘', '光驱'
    ]

    categories = [
        '电子产品', '家具', '服装', '书籍', '玩具', '办公用品', '家用电器', '运动器材',
        '美容护肤', '食品饮料', '汽车配件', '健康保健', '宠物用品', '乐器', '园艺工具'
    ]
    for _ in range(num_records):
        name = random.choice(product_names)
        category = random.choice(categories)
        price = round(random.uniform(10, 1000), 2)
        stock = random.randint(1, 100)
        cursor.execute('''
        INSERT INTO Products (ProductName, Category, Price, Stock)
        VALUES (?, ?, ?, ?);
        ''', (name, category, price, stock))


# 插入库存数据
def insert_inventory(num_records):
    product_ids = [row[0] for row in cursor.execute('SELECT ProductID FROM Products')]
    for _ in range(num_records):
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 200)
        cursor.execute('''
        INSERT INTO Inventory (ProductID, Quantity)
        VALUES (?, ?);
        ''', (product_id, quantity))


# 插入销售数据
def insert_sales_orders(num_records):
    customer_ids = [row[0] for row in cursor.execute('SELECT CustomerID FROM Customers')]
    for _ in range(num_records):
        customer_id = random.choice(customer_ids)
        order_date = fake.date_between(start_date='-1y', end_date='today')
        total_amount = round(random.uniform(100, 10000), 2)
        order_status = random.choice(['待处理', '已发货', '已完成', '已取消'])
        cursor.execute('''
        INSERT INTO SalesOrders (CustomerID, OrderDate, TotalAmount, OrderStatus)
        VALUES (?, ?, ?, ?);
        ''', (customer_id, order_date, total_amount, order_status))

# 插入销售数据明细
def insert_sales_order_details(num_records):
    sales_order_ids = [row[0] for row in cursor.execute('SELECT SalesOrderID FROM SalesOrders')]
    product_ids = [row[0] for row in cursor.execute('SELECT ProductID FROM Products')]
    for _ in range(num_records):
        sales_order_id = random.choice(sales_order_ids)
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 20)
        unit_price = round(random.uniform(10, 500), 2)
        cursor.execute('''
        INSERT INTO SalesOrderDetails (SalesOrderID, ProductID, Quantity, UnitPrice)
        VALUES (?, ?, ?, ?);
        ''', (sales_order_id, product_id, quantity, unit_price))


# 插入采购订单
def insert_purchase_orders(num_records):
    supplier_ids = [row[0] for row in cursor.execute('SELECT SupplierID FROM Suppliers')]
    for _ in range(num_records):
        supplier_id = random.choice(supplier_ids)
        order_date = fake.date_between(start_date='-1y', end_date='today')
        total_amount = round(random.uniform(100, 10000), 2)
        order_status = random.choice(['待处理', '已发货', '已完成', '已取消'])
        cursor.execute('''
        INSERT INTO PurchaseOrders (SupplierID, OrderDate, TotalAmount, OrderStatus)
        VALUES (?, ?, ?, ?);
        ''', (supplier_id, order_date, total_amount, order_status))

def insert_purchase_order_details(num_records):
    purchase_order_ids = [row[0] for row in cursor.execute('SELECT PurchaseOrderID FROM PurchaseOrders')]
    product_ids = [row[0] for row in cursor.execute('SELECT ProductID FROM Products')]
    for _ in range(num_records):
        purchase_order_id = random.choice(purchase_order_ids)
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 50)
        unit_price = round(random.uniform(10, 500), 2)
        cursor.execute('''
        INSERT INTO PurchaseOrderDetails (PurchaseOrderID, ProductID, Quantity, UnitPrice)
        VALUES (?, ?, ?, ?);
        ''', (purchase_order_id, product_id, quantity, unit_price))



def insert_suppliers(num_records):
    for _ in range(num_records):
        name = fake.company()
        contact_name = fake.name()
        contact_email = fake.email()
        contact_phone = fake.phone_number()
        address = fake.address()
        city = fake.city()
        country = fake.country()
        cursor.execute('''
        INSERT INTO Suppliers (SupplierName, ContactName, ContactEmail, ContactPhone, Address, City, Country)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        ''', (name, contact_name, contact_email, contact_phone, address, city, country))



# 插入随机数据
insert_customers(900)


# 提交事务
conn.commit()

# 关闭连接
conn.close()
print("数据插入完成！")

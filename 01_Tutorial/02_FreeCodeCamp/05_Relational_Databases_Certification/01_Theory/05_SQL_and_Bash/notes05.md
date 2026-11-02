# Working With SQL

## 什么是 SQL 中的归一化？

## 什么是 SQL 注入，以及有哪些防止它的方法？

```sql
'SELECT * FROM users WHERE username = ' + username_input + ' AND password = ' + password_input + ';'
```

## 什么是 N+1 问题？

### 减少查询次数

```sql
SELECT
  orders.order_id,
  orders.product,
  orders.quantity,
  customers.customer_id,
  customers.name AS customer_name,
  customers.email AS customer_email,
  customers.address AS customer_address
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
WHERE orders.order_id IN (SELECT order_id FROM orders LIMIT 50)
```

2026.10.26

# Workshop

IFS = Internal Field Separator

2026.10.26 17:23

```sql
SELECT a1, a2 WHERE a2 != 'foobar' ORDER BY a1 LIMIT 10
```

2026.10.29 16:09

```sql
SELECT * FROM students WHERE last_name < 'M' AND gpa = 3.9 OR gpa < 2.3;
```

上面这一段结果是`last_name < 'M' AND gpa = 3.9`或`gpa < 2.3`。

```sql
SELECT * FROM students WHERE last_name < 'M' AND (gpa = 3.9 OR gpa < 2.3);
```

上面这个是名字加3.9或者2.3或者都有。

2026.10.29 17:35

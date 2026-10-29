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

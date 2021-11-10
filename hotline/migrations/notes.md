# schema notes for dbdiagram.io

It's a draft!

```sql
// Tickets
Table ticket as Tic {
  id int [pk, increment]
  created_at datetime [default: `now()`]
  customer_id int [ref: > C.id]
  technician_id int [ref: - Tec.id]
  customer_reference varchar [ref: - C.reference]
}

// Customers
Table customers as C {
  id int [pk, increment]
  description varchar
  reference varchar
}

// Technicians
Table technicians as Tec {
  id int [pk, increment]
  first_name varchar
  last_name varchar
  department_id int [ref: - D.id]
}

// Departments
Table departments as D {
    id int [pk, increment]
    description varchar
}

// Products

// 

```
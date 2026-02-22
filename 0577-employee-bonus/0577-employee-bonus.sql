# Write your MySQL query statement below
select name,bonus from Employee left join Bonus on Employee.empId=Bonus.EmpId where Bonus.bonus<1000 or Bonus.bonus is null;
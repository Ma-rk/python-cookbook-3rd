# 1-2 임의 순환체의 요소 나누기

record = ('Ma-rk', 'kim.mark.dev@gmail.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

print(name)
print(email)
print(phone_numbers)

sales_record = [1, 2, 3, 4, 5, 6, 7, 8]
*trailing_qtrs, current_qtr = sales_record
trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)

print(current_qtr)
print(trailing_avg)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

print(uname)
print(homedir)
print(sh)

data = ['Ma-rk', 50, 91.1, (2012, 12, 21)]
name, _, _, (_, _, day) = data
print(name)
print(day)

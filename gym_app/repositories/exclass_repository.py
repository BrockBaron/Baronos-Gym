from db.run_sql import run_sql
from models.exclass import Class
from models.member import Member

# save new exclass
def save(exclass):
    sql = "INSERT INTO exclass(name, activity_type, duration, capacity) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [exclass.name, exclass.activity_type, exclass.duration, exclass.capacity]
    results = run_sql(sql, values)
    exclass.id == results[0]['id']
    return exclass
    
# select all classes

# select specific class by id

# delete all exclassess

# delete specific exclass by id
from db.run_sql import run_sql
from models.exclass import Exclass
from models.member import Member

# save new exclass
def save(exclass):
    sql = "INSERT INTO exclass(name, activity_type, duration, capacity) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [exclass.name, exclass.activity_type, exclass.duration, exclass.capacity]
    results = run_sql(sql, values)
    exclass.id == results[0]['id']
    return exclass
    
# select all classes
def select_all():
    exclasses = []
    
    sql = "SELECT * FROM exclasses"
    results = run_sql(sql)
    
    for row in results:
        exclass = Exclass(row['name'], row['activity_type'], row['duration'], row['capacity'], row['id'])
        exclasses.append(exclass)
    return exclasses


# select specific class by id

# delete all exclassess

# delete specific exclass by id
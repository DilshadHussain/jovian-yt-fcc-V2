from sqlalchemy import create_engine, text
import os

db_connection_str = os.environ.get('DB_CONNECTION_STRING')

engine = create_engine(db_connection_str,
          connect_args={
                "ssl": {
                  "ssl_ca": "/etc/ssl/cert.pem"
                }
             })

# with engine.connect() as conn:
#   result = conn.execute(text("SELECT * FROM jobs"))

#   result_dicts = []
#   for row in result.all():
#     result_dicts.append(row._mapping)
    
# print(result_dicts)

def load_jobs_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))

    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs
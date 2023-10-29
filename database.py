from sqlalchemy import create_engine, text

db_connection_str = "mysql+pymysql://g64p32mdelh4n6zapkbz:pscale_pw_sbBalhUQswwYC9cbHPxoHvbOr0tbPCVV3uM4WL0maXB@aws.connect.psdb.cloud/adarshp?ssl_ca=/etc/ssl/certs/ca-certificates.crt?charset=utf8mb4"

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
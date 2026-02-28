# import psycopg2
# from psycopg2 import OperationalError
# from .settings import DATABASES

# def connect_to_database():
#     connection = None
#     try:
#         config = DATABASES['default']
        
#         connection = psycopg2.connect(
#             dbname=config['NAME'],
#             user=config['USER'],
#             password=config['PASSWORD'],
#             host=config['HOST'],
#             port=config['PORT']
#         )
#         print("Conexión exitosa a la base de datos.")
        
#     except OperationalError as e:
#         print(f"Error de conexión (Host/Red/Credenciales): {e}")
#     except Exception as e:
#         print(f"Ocurrió un error inesperado: {e}")
        
#     return connection

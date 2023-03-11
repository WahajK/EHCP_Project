import logging
import asyncio
import aiocoap.resource as resource
import aiocoap
import mysql.connector

class SQL_Data(resource.Resource):
    async def render_get(self, request):
        #Payload Splitting
        payload = request.payload.decode('utf8').split('+')
        username = payload[0]
        password = payload[1]
        flag = payload[2]
        # Connect to the database
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="msvcr100",
            database="iot",
	        auth_plugin='auth_socket',
        )
        
        # Create a cursor
        cursor = cnx.cursor()

        # Execute a query
        if flag == "0":
            query = "SELECT * FROM user where username = '{}' and password = '{}'".format(username,password)
        else:
            query = "SELECT * FROM user_dup where username = '{}' and password = '{}'".format(username,password)
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Clean up
        cursor.close()
        cnx.close()
        
        return aiocoap.Message(content_format=0, payload=str(rows).encode('utf8'))

# logging setup

logging.basicConfig(level=logging.INFO)
logging.getLogger("coap-server").setLevel(logging.DEBUG)

def main():
    # Resource tree creation
    root = resource.Site()

    root.add_resource(['SQL_Data'], SQL_Data())

    asyncio.Task(aiocoap.Context.create_server_context(bind=('127.0.0.1',5683),site = root))

    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()

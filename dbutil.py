
import sqlite3


class Dbutil_Sqlite:
    def __init(self,database):
        self.db=database
        self.conn=sqlite3.connect(database)

    def connecta(self,datatabase):
        self.database=datatabase
        self.conn=sqlite3.connect(self.database)

    
    def run_sql(self,query):
        self.cursor=self.conn.execute(query)
        self.conn.commit

    def tb_insert(self,tb,fields={}):
        """Descripción de la función

        Inserta en una tabla sqlite 3 los campos/valores
        especificado en el parametro fields

        Parameters
        ----------
        tb : string
            Nombre de la tabla
        fields : dictionary
            Formato {"CAMPO 1":valor,"CAMPO 2":valor}
        Returns
        -------
        tipo
            Descripción de los valores que devuelve
        """
        self.campos="("
        self.valores=" VALUES("
        self.fields=fields
        
        #Todos los campos/valores del diccionario
        try:

            for f in self.fields:
                #Construir lista de campos
                #formato: (CAMPO 1,CAMPO 2,....)
                self.campos=self.campos+ f+","

                #Construir la lista de valores
                #formato VALUES('TEXTO',100,....)
                #si es texto encerramos el valor entre comillas simples
                if type(self.fields[f])==str:
                    self.valores=self.valores+"'"+fields[f]+"',"
                else:
                    self.valores=self.valores+str(fields[f])+","
                
            #Cerrar parentesis
            self.campos=self.campos[0:len(self.campos)-1]+")"
            self.valores=self.valores[0:len(self.valores)-1]+")"
            #Construimos la sentencia INSERT
            sql="INSERT INTO "+tb+self.campos+self.valores
            #Ejecutamos la sentencia
            self.cursor=self.conn.cursor()
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except Exception as e:
            print(e.args)
            return False
        finally:
            self.conn.close()


    def tb_update(self,tb,filter,fields={}):
        """Descripción de la función

        Actualiza en una tabla sqlite3 los campos/valores
        especificado en el parametro fields aplicando un 
        where con la string especificada en filter

        Parameters
        ----------
        tb : string
            Nombre de la tabla
        filter : string
            condiciòn especificada en la clausula WHERE
        fields : dictionary
            Formato {"CAMPO 1":valor,"CAMPO 2":valor}
        Returns
        -------
        tipo
            Descripción de los valores que devuelve
        """
        self.campos="("
        self.valores=" SET "
        self.fields=fields
        #Todos los campos/valores del diccionario
        for f in self.fields:
            self.valores=self.valores+f+"="

            #Construir la lista de valores
            #formato VALUES('TEXTO',100,....)
            #si es texto encerramos el valor entre comillas simples
            if type(self.fields[f])==str:
                self.valores=self.valores+"'"+self.fields[f]+"',"
            else:
                self.valores=self.valores+str(self.fields[f])
                self.valores=self.valores+","
            
        #Cerrar parentesis
        self.valores=self.valores[0:len(self.valores)-1]
        #Construimos la sentencia INSET
        sql="UPDATE "+tb+self.valores+" WHERE "+filter
        print(sql)
        #Ejecutamos la sentencia
        self.cursor=self.conn.cursor()
        self.cursor.execute(sql)
        self.conn.commit()

db=Dbutil_Sqlite()
db.connecta("grafico.db")
campos={"NOMBRE":"PRUEBA 3","SOMBRA":1,"LEYENDAS":1}
db.tb_insert("grafico",campos)
db.connecta("grafico.db")
db.tb_update("grafico","NOMBRE='PRUEBA 2'",campos)



    
        

        




import psycopg2

class ConexaoFactory:
    def get_conexao(self):
        return psycopg2.connect(host="silly.db.elephantsql.com", database="dmhesvhi", user="dmhesvhi", password="zbeWx5cZCPZCEL0ZwVC815YyYzb27kjo")

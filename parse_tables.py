import re

class Table_parser:
    def _init__ (self):
        pass
    
    def __clean_and_split_query(self, query):
        query = re.sub(r"--[\\rnt]*[\w\s,.]*[\\rnt]*", '', query)
        query = re.sub(r"[\r\n\t\s]+", " ", query)
        query = re.sub(r'[\r\t]+', '', query)
        query = re.sub(r'\s*\(\s*', ' ( ', query)
        query = re.sub(r'\s*\)\s*', ' ) ', query)
        query = re.sub (r'[\n\s]+', ' ', query)
        ws_bracket = re.sub(r"\][^\.]", "] ", query)
        splited = ws_bracket.upper().split(" ")
        return splited


    def __parse_tables(self, splited_query):
        table_names = []
        keywords = ['FROM', 'JOIN']
        keyword_appeared = False
        for i in range(len(splited_query)):
            if keyword_appeared:
                if splited_query[i][0] != "(":
                    table_names.append(splited_query[i])
                keyword_appeared = False
            elif splited_query[i] in keywords:
                keyword_appeared = True
        if 'SYSDATE' in table_names:
            table_names.remove('SYSDATE')
        return table_names


    def __remove_brackets(self, tables):
        for i in range(len(tables)):
            tables[i] = tables[i].replace("[", "").replace("]", "")
        return tables


    def __get_unique_names(self, tables):
        return list(set(tables))


    def get_tables(self, sql):
        splited_sql = self.__clean_and_split_query(sql)
        tables = self.__parse_tables(splited_sql)
        tables = self.__remove_brackets(tables)
        return self.__get_unique_names(tables)

import os
from parse_tables import Table_parser
from parse_xml import Xml_parser

root_dir = r"F:\BackupsAndOther\work\report_parsing"
files_list = os.listdir(root_dir);
for file in files_list:
    all_tables = []
    xp = Xml_parser(root_dir + '\\' + file)
    tp = Table_parser()
    queries = xp.get_sql()
    print(file)
    for query in queries:
        tables = tp.get_tables(query)
        for table in tables:
            if table not in all_tables:
                all_tables.append(table)
    print(all_tables)
    print('\n')
import urllib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Sku, Vendor


class DatabaseReader:

    def __init__(self):
        params = urllib.parse.quote_plus(
            "DRIVER=SQL Server;SERVER=10.0.0.30;DATABASE=Overseas_TEST;UID=sa;PWD=SQLsrv4fr")
        engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params, echo=True)
        self.session = sessionmaker(bind=engine)()

    def get_vendor_names(self):
        query = self.session.query(Sku).join(Vendor)
        return [name for name in query.with_entities(Vendor.name).distinct()]



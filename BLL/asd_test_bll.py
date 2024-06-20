from DAL.asd_db import AsdDBDal
from datetime import date


class AsdBL:
    def __init__(self):
        self.__factory_db_dal=AsdDBDal()

    def orgenize_data(self, objAsd):
        
        for i in range(0,len(objAsd),12):
            new_obj = {}
            thisObj = objAsd[i:i+13]
            for count, item in enumerate(thisObj):
                if count ==5:
                    continue
                if count == 11:
                    new_obj["personal"] = item
                    self.__factory_db_dal.insert_new_tests(new_obj)
                    print(new_obj)
                else:
                    new_obj["test" + str(count)] = item
        
        
        return "created" 
   
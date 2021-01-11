import sys

def main():
#  print("main function")

 class parking:
      
    

    vehicles_allowed=[('motorcycle','small'),('car','medium'),('bus','large')]
   

    def __init__(self):
        self.__parkingspace=[
         {"space":"", "size":"small","Id":1,"vehicle_parked":False},
         {"space":"", "size":"small","Id":2,"vehicle_parked":False},
         {"space":"", "size":"small","Id":3,"vehicle_parked":False},
         {"space":"", "size":"small","Id":4,"vehicle_parked":False},
         {"space":"", "size":"small","Id":5,"vehicle_parked":False},
         {"space":"", "size":"small","Id":6,"vehicle_parked":False},
         {"space":"", "size":"small","Id":7,"vehicle_parked":False},
         {"space":"", "size":"small","Id":8,"vehicle_parked":False},
         {"space":"", "size":"small","Id":9,"vehicle_parked":False},
         {"space":"", "size":"small","Id":10,"vehicle_parked":False},
         {"space":"", "size":"medium","Id":11,"vehicle_parked":False},
         {"space":"", "size":"medium","Id":12,"vehicle_parked":False},
         {"space":"", "size":"medium","Id":13,"vehicle_parked":False},
         {"space":"", "size":"medium","Id":14,"vehicle_parked":False},
         {"space":"", "size":"medium","Id":15,"vehicle_parked":False},
         {"space":"", "size":"medium","Id":16,"vehicle_parked":False},
         {"space":"", "size":"medium","Id":17,"vehicle_parked":False},
         {"space":"", "size":"large","Id":18,"vehicle_parked":False},
         {"space":"", "size":"large","Id":19,"vehicle_parked":False},
         {"space":"", "size":"large","Id":20,"vehicle_parked":False},
    ]
        print("parking slot created")

    def checkvehicle(self,vehicledetails):
        for (vehicle,size) in self.vehicles_allowed:
            
             if (vehicle==vehicledetails["vehicle_name"]):
              print(vehicle,"vechile name")
              vehicledetails["size"]=size
              return vehicledetails
        return False    

    def allotparking(self,vehicledetails):
        vechiledetails=self.checkvehicle(vehicledetails)
        if vechiledetails:
            for i in self.__parkingspace:
               if(i["vehicle_parked"]==False and i["size"]==vechiledetails["size"]):
                   i["space"]=vechiledetails["vehicle_name"]
                   i["vehicle_ID"]=vechiledetails["vehicle_ID"]
                   i["vehicle_parked"]=True
                   print("parking slot Id :", i["Id"])
                   print("vechile id :", i["vehicle_ID"])
                   print()
                   break
            return self.__parkingspace   



#  p= parking()
#  print(p.allotparking({"vehicle_name":"car", "vehicle_ID":"b987"}))
 if len(sys.argv) != 4:
    print(sys.argv)
    print('usage: ./parking.py {--type & --id} file')
    sys.exit(0)
 else:
   p= parking()
   vehicletype =  sys.argv[2]
   _id = sys.argv[4]
   vehicledetails= {"vehicle_name":vehicletype, "vehicle_ID":_id}
   print(p.allotparking(vehicledetails))

if __name__ =="__main__":
 main()


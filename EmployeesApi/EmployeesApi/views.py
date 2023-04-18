from rest_framework.decorators import api_view
from rest_framework.response import Response

import json
import uuid

edata = ''
with open('D:\SAHAJ\wce-employee-mgmt.vishalmadle13\EmployeesApi\EmployeesApi\data.json', 'r') as f:
    edata = json.load(f)

@api_view(['GET','PUT','DELETE'])
def employee(request,id) : 
    # print("0..................")
    with open('D:\SAHAJ\wce-employee-mgmt.vishalmadle13\EmployeesApi\EmployeesApi\data.json', 'r') as f:
        edata = json.load(f)
    
    if id not in edata  and id != "all":
        return Response({ 'message' : "Employee with {id} was not found"}) 
    

    if(request.method == 'GET'):
        if id == "all":
            with open('D:\SAHAJ\wce-employee-mgmt.vishalmadle13\EmployeesApi\EmployeesApi\data.json', 'r')  as f:
                edata = json.load(f) 
            data = json.dumps(edata) 
            # print(data)
            return Response(data)
        empObj = edata.get(id)  
        data = json.dumps(empObj)
        return Response(data)
    
    
    if(request.method == 'PUT'): 
        reqName = request.POST.get('name')
        reqCity = request.POST.get('city')
        reqDict = {'name' : reqName,'city' : reqCity}
        # print(reqDict)
        edata.update(id = reqDict)
        json_object = json.dumps(edata)
        with open('D:\SAHAJ\wce-employee-mgmt.vishalmadle13\EmployeesApi\EmployeesApi\data.json', 'w')  as outfile:
            outfile.write(json_object)
        empObj = edata.get(id) 
        data = json.dumps(empObj)
        return Response(data)



    if(request.method == 'DELETE'):
        if id in data :
            empObj = edata.get(id)
            edata.pop(id)
            json_object = json.dumps(edata)
            with open('D:\SAHAJ\wce-employee-mgmt.vishalmadle13\EmployeesApi\EmployeesApi\data.json', 'w')  as outfile:
                outfile.write(json_object)
            data = json.dumps(empObj)
            return Response(data)





@api_view(['GET','POST'])
def employeePost(request):
    with open('D:\SAHAJ\wce-employee-mgmt.vishalmadle13\EmployeesApi\EmployeesApi\data.json', 'r') as f:
        edata = json.load(f)
    if(request.method == 'POST'):
        id = uuid.uuid4()
        reqName = request.GET.get('name')
        reqCity = request.GET.get("city")
        # print(reqName)
        reqDict = {"name" : reqName,'city' : reqCity}
        # print(reqDict)
        edata[str(id)] = reqDict
        
        json_object = json.dumps(edata)
        with open('D:\SAHAJ\wce-employee-mgmt.vishalmadle13\EmployeesApi\EmployeesApi\data.json', 'w')  as outfile:
            outfile.write(json_object)
            
        return Response({"employeeId": id})
    
    if(request.method == 'GET'):
        return Response({"hii":"ki"})
    


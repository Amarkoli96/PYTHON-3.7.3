inputfile = open("Samsung Galaxy Tab A 8.0 (2019) - Full tablet specifications.html","r")
csv=open("datasheet.csv","w+")
csv.write("DEVICE_NAME,LAUNCH,CHIPSET,BODY,DISPLAY,PLATFORM,MEMORY\n")

def csv_write(key,index):
    while(1):
        data=inputfile.readline()
        if key in data:
            data=data.split('>')
            print(data)
            data=data[index].split('<')
            data=data[0].replace(',','-')
            csv.write("{},".format(data))
            print(data)
            break


csv_write('data-spec="modelname"',1)
csv_write('data-spec="released-hl"',4)
csv_write('data-spec="chipset-hl"',1)
csv.close()

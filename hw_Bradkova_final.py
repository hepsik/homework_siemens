#data=b'\x00 \x008\x01\x00\x00*6ES7 146-6HE00-0BB0 S C-PNRJ60012022\x00\x01B3\x01\x0c\x00\x00\x00\x00\x00\x05\x01\x01\x00\x0f

class I_M: 
    def print(self):
        self.block_header = self.data[0:6]
        self.manuf_ID = int("".join(map(str,list(self.data[6:8]))))
        self.on = f"'{self.data[8:28].decode('utf-8')}'"
        self.sn = f"'{self.data[28:44].decode('utf-8')}'"
        self.hw_revision = int("".join(map(str,list(self.data[44:46]))))
        self.sw_revision = ".".join(map(str,list(self.data[46:50])))
        self.revision_status = ",".join(map(str,list(self.data[50:52])))
        self.profile_ID = int("".join(map(str,list(self.data[52:54]))))
        self.profile_type = int("".join(map(str,list(self.data[54:56]))))
        self.im_version = str(self.data[56:58])
        self.im_support = int("".join(map(str,list(self.data[58:60]))))
        return f"Block header = {self.block_header} \nManufacture ID = {(self.manuf_ID)}\nOrder number = {self.on} \nSerial number = {self.sn} \nHardware revision = {self.hw_revision} \nSoftware revision = {self.sw_revision} \nRevision status = {self.revision_status} \nProfile ID = {self.profile_ID} \nProfile-specific type = {self.profile_type} \nI&M version = {self.im_version} \nI&M support = {self.im_support}"
    def update(self, data):
        self.data = data
    def __str__(self) -> str:
        return f"Raw data: {self.data}"
    def compare(self):
        self.block_header = self.data[0:6]
        self.manuf_ID = int("".join(map(str,list(self.data[6:8]))))
        self.on = f"{self.data[8:28].decode('utf-8')}"
        self.sn = f"{self.data[28:44].decode('utf-8')}"
        self.hw_revision = int("".join(map(str,list(self.data[44:46]))))
        self.sw_revision = ".".join(map(str,list(self.data[46:50])))
        self.revision_status = ",".join(map(str,list(self.data[50:52])))
        self.profile_ID = int("".join(map(str,list(self.data[52:54]))))
        self.profile_type = int("".join(map(str,list(self.data[54:56]))))
        self.im_version = str(self.data[56:58])
        self.im_support = int("".join(map(str,list(self.data[58:60]))))
        if self.manuf_ID == 42:
            result = True
        else: 
            result = False
            print (f"Manufacture ID = {self.manuf_ID}")
        
        if self.on == "6ES7 146-6HF00-0BB0 ":
            result2 = True
        else:
            result2 = False
            print (f"Order number = '{self.on}'")
        
        if self.sn == 'S C-PNRJ60012022':
            result3 = True
        else:  
            result3 = False
            print (f"Serial number = '{self.sn}'")
        
        if self.profile_ID == 0:
            result4 = True
        else:
            result4 = False
            print (f"Profile ID = {self.profile_ID}")
        
        if self.profile_type == 5:
            result5 = True
        else:
            result5 = False
            print (f"Profile-specific type = {self.profile_type}")
        
        if self.im_version == str(b'\x01\x01'): 
            result6 = True
        else:
            result6 = False
            print (f"I&M Version = {self.im_version}")
        
        if self.im_support == 14:
            result7 = True
        else:
            result7 = False
            print (f"I&M Support = {self.im_support}")

        results = [result, result2, result3, result4, result5, result6, result7]
        a = 0
        for item in results:  
            if item == True:
                a = a + 0
            else:
                a = a + 1
        if a > 0:
            return f"Number of unequal elements is: {a}"  
        else:
            return 0    
    def __repr__(self) -> str:
        self.block_header = self.data[0:6]
        self.manuf_ID = int("".join(map(str,list(self.data[6:8]))))
        self.on = f"'{self.data[8:28].decode('utf-8')}'"
        self.sn = f"'{self.data[28:44].decode('utf-8')}'"
        self.hw_revision = int("".join(map(str,list(self.data[44:46]))))
        self.sw_revision = ".".join(map(str,list(self.data[46:50])))
        self.revision_status = ",".join(map(str,list(self.data[50:52])))
        self.profile_ID = int("".join(map(str,list(self.data[52:54]))))
        self.profile_type = int("".join(map(str,list(self.data[54:56]))))
        self.im_version = str(self.data[56:58])
        self.im_support = int("".join(map(str,list(self.data[58:60]))))
        rep = f"Block header = {self.block_header} \nManufacture ID = {(self.manuf_ID)}\nOrder number = {self.on} \nSerial number = {self.sn} \nHardware revision = {self.hw_revision} \nSoftware revision = {self.sw_revision} \nRevision status = {self.revision_status} \nProfile ID = {self.profile_ID} \nProfile-specific type = {self.profile_type} \nI&M version = {self.im_version} \nI&M support = {self.im_support}"
        return rep 
    def call(self):
        self.block_header = self.data[0:6]
        self.manuf_ID = int("".join(map(str,list(self.data[6:8]))))
        self.on = f"'{self.data[8:28].decode('utf-8')}'"
        self.sn = f"'{self.data[28:44].decode('utf-8')}'"
        self.hw_revision = int("".join(map(str,list(self.data[44:46]))))
        self.sw_revision = ".".join(map(str,list(self.data[46:50])))
        self.revision_status = ",".join(map(str,list(self.data[50:52])))
        self.profile_ID = int("".join(map(str,list(self.data[52:54]))))
        self.profile_type = int("".join(map(str,list(self.data[54:56]))))
        self.im_version = str(self.data[56:58])
        self.im_support = int("".join(map(str,list(self.data[58:60]))))
        voc = {"Block header" : self.block_header, "Manufacture ID" : self.manuf_ID, "Order number" : self.on, "Serial number" : self.sn, "Hardware revision" : self.hw_revision, "Software revision" : self.sw_revision, "Revision status" : self.revision_status, "Profile ID" : self.profile_ID, "Profile-specific type" : self.profile_type, "I&M version" : self.im_version, "I&M support" : self.im_support}
        field_name = input("Field name:")
        if field_name in voc:
            return f"{field_name} = {voc[field_name]}"
        else:
            return f"Entered field name does not exist"

        
  
response = I_M()
response.data = (b'\x00 \x008\x01\x00\x00*6ES7 146-6HE00-0BB0 S C-PNRJ60012022\x00\x01B3\x01\x0c\x00\x00\x00\x00\x00\x05\x01\x01\x00\x0f')
print(response)
response.update(b'\x00 \x008\x01\x00\x00*9ES7 146-6HE00-0BB0 S C-PNRJ60012022\x00\x01B3\x01\x0c\x00\x00\x00\x00\x00\x05\x01\x01\x00\x0f')
print(response)
print(response.print())
print(response.call())



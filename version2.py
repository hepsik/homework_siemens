#data=b'\x00 \x008\x01\x00\x00*6ES7 146-6HE00-0BB0 S C-PNRJ60012022\x00\x01B3\x01\x0c\x00\x00\x00\x00\x00\x05\x01\x01\x00\x0f
df_manuf_ID = 42
df_on = "6ES7 146-6HF00-0BB0 "
df_sn = 'S C-PNRJ60012022'
df_profile_ID = 0
df_profile_type = 5
df_im_version = b'\x01\x01'
df_im_support = 14

class I_M: 
    def __init__(self, data):
        self.data = data
        self.block_header = self.data[0:6]
        self.manuf_ID = int("".join(map(str,list(self.data[6:8]))))
        self.on = f"{self.data[8:28].decode('utf-8')}"
        self.sn = f"{self.data[28:44].decode('utf-8')}"
        self.hw_revision = int("".join(map(str,list(self.data[44:46]))))
        self.sw_revision = ".".join(map(str,list(self.data[46:50])))
        self.revision_status = ",".join(map(str,list(self.data[50:52])))
        self.profile_ID = int("".join(map(str,list(self.data[52:54]))))
        self.profile_type = int("".join(map(str,list(self.data[54:56]))))
        self.im_version = self.data[56:58]
        self.im_support = int("".join(map(str,list(self.data[58:60]))))
    def print(self):
        return f"Block header = {self.block_header} \nManufacture ID = {(self.manuf_ID)}\nOrder number = '{self.on}' \nSerial number = '{self.sn}' \nHardware revision = {self.hw_revision} \nSoftware revision = {self.sw_revision} \nRevision status = {self.revision_status} \nProfile ID = {self.profile_ID} \nProfile-specific type = {self.profile_type} \nI&M version = {self.im_version} \nI&M support = {self.im_support}"
    def update(self, data):
        self.data = data
    def __str__(self) -> str:
        return f"Raw data: {self.data}"
    def compare(self):
        if self.manuf_ID == df_manuf_ID:
            result = True
        else: 
            result = False
            print (f"Manufacture ID = {self.manuf_ID}")
        
        if self.on == df_on:
            result2 = True
        else:
            result2 = False
            print (f"Order number = '{self.on}'")
        
        if self.sn == df_sn:
            result3 = True
        else:  
            result3 = False
            print (f"Serial number = '{self.sn}'")
        
        if self.profile_ID == df_profile_ID:
            result4 = True
        else:
            result4 = False
            print (f"Profile ID = {self.profile_ID}")
        
        if self.profile_type == df_profile_type:
            result5 = True
        else:
            result5 = False
            print (f"Profile-specific type = {self.profile_type}")
        
        if self.im_version == df_im_version: 
            result6 = True
        else:
            result6 = False
            print (f"I&M Version = {self.im_version}")
        
        if self.im_support == df_im_support:
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
        rep = f"Block header = {self.block_header} \nManufacture ID = {(self.manuf_ID)}\nOrder number = '{self.on}' \nSerial number = '{self.sn}' \nHardware revision = {self.hw_revision} \nSoftware revision = {self.sw_revision} \nRevision status = {self.revision_status} \nProfile ID = {self.profile_ID} \nProfile-specific type = {self.profile_type} \nI&M version = {self.im_version} \nI&M support = {self.im_support}"
        return rep 
    def call(self):
        voc = {"Block header" : self.block_header, "Manufacture ID" : self.manuf_ID, "Order number" : self.on, "Serial number" : self.sn, "Hardware revision" : self.hw_revision, "Software revision" : self.sw_revision, "Revision status" : self.revision_status, "Profile ID" : self.profile_ID, "Profile-specific type" : self.profile_type, "I&M version" : self.im_version, "I&M support" : self.im_support}
        field_name = input("Field name:")
        if field_name in voc:
            return f"{field_name} = {voc[field_name]}"
        else:
            return f"Entered field name does not exist"

        
  
response = I_M(b'\x00 \x008\x01\x00\x00*6ES7 146-6HE00-0BB0 S C-PNRJ60012022\x00\x01B3\x01\x0c\x00\x00\x00\x00\x00\x05\x01\x01\x00\x0f')

print(response)
print(response.compare())
response.update(b'\x00 \x008\x01\x00\x00*8ES7 146-6HE00-0BB0 S C-PNRJ60012022\x00\x01B3\x01\x0c\x00\x00\x00\x00\x00\x05\x01\x01\x00\x0f')
print(response.print())
response = I_M(b'\x00 \x008\x01\x00\x00*9ES7 146-6HE00-0BB0 S C-PNRJ60012022\x00\x01B3\x01\x0c\x00\x00\x00\x00\x00\x05\x01\x01\x00\x0f')
print(response.call())
print(response.compare())
class PC():
    pc_counter=0
    def __init__(self,cpu,gpu,ram_slot1,ram_slot2):
        self.cpu=cpu
        self.gpu=gpu
        self.ram_slot1=ram_slot1
        self.ram_slot2=ram_slot2
        self.overall_ram=self.ram_slot2+self.ram_slot1
        PC.pc_counter+=1
        
    
    @staticmethod   
    def Show_info():
        print("Generic PC information")
        print(f"CPU: Not Available\nGPU: Not Available\nram slot 1: Not Available\nram slot 2: Not Available\noverall ram: Not Available")  
        print()
    
ob1=PC("Ryzen 5","GTX 1060",8,8)
ob2=PC("Ryzen 5","GTX 1060",8,8)
ob3=PC("Ryzen 5","GTX 1060",8,8)
ob1.Show_info()

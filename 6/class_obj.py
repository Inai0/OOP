class PC():
    def __init__(self, cpu, gpu, ram_slot1, ram_slot2):
        self.cpu = cpu
        self.gpu = gpu
        self.ram_slot1 = ram_slot1
        self.ram_slot2 = ram_slot2
        self.overall_ram = self.ram_slot2 + self.ram_slot1
        PC.Show_info(self)

    def Show_info(self):
        print("Generic PC information")
        print(f"CPU: {self.cpu}\nGPU: {self.gpu}\nram slot 1: {self.ram_slot1}\nram slot 2: {self.ram_slot2}")
    
ob1 = PC("Ryzen 5", "GTX 1060", 8, 8)
ob1.Show_info()


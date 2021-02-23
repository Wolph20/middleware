import subprocess
import pandas as pd
import sys

class Distribution:
    def __init__(self, samples, inter_arrive):
        self.samples = samples
        self.inter_arrive = inter_arrive

    def unif_dist(self):
        cmd = './generator ' + str(self.samples) + ' 500 ' + str(self.inter_arrive) + ' 80 549093 1 0 0 1 > traza_'+ str(self.samples) +'.csv'
        return subprocess.call(cmd, shell=True)
        

    def poisson_dist(self):
        cmd = './generator ' + str(self.samples) + ' 500 ' + str(self.inter_arrive) + ' 80 549093 2 0 0 1 > traza_'+ str(self.samples) +'.csv'
        return subprocess.call(cmd, shell=True)
    
    def normal_dist(self):
        cmd = './generator ' + str(self.samples) + ' 500 ' + str(self.inter_arrive) + ' 80 549093 3 10 5 1 > traza_'+ str(self.samples) +'.csv'
        return subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    
    if len(sys.argv) == 5:
        id_worker = sys.argv[1]
        inter_arrive = sys.argv[2]
        service_time = sys.argv[3]
        dist = sys.argv[4]
        
        samples = [100, 1000, 10000]
        counter = 1
        for i in samples:
            while counter == 1:
                subprocess.call('make >/dev/null; cd QueueSimulator/ ; make >/dev/null ; cd ..', shell=True)
                counter += 1
            
            get = Distribution(i, inter_arrive)

            if dist == '1':
                get.unif_dist()

            elif dist == '2':
                get.poisson_dist()

            elif dist == '3':
                get.normal_dist()

            else:
                print("Valor erróneo en el argumento de tipo de distribución, favor de ingresar un número entre 1-3")
            

            data = pd.read_csv("./traza_"+str(i)+".csv", names=['arrive_time', 'worker_id', 'petition_type', 'memory_size', 'portion'], header=None, sep=" ")

            data = pd.DataFrame(data)
            length = len(data)
            sum = 0

            # Se calcula la media del tiempo de arribo
            
            a = data.iloc[:1,:1].values
            b = data.iloc[length-1:length,:1].values
            sum = b - a

            inter_arrive_meanTime = float(sum/(length*1000))

            size_storage = data['memory_size'].sum()
            write = data['petition_type'].where(data['petition_type']=='w').count()
            read = data['petition_type'].where(data['petition_type']=='r').count()
            operation_number = write + read

            subprocess.call("echo Samples: " + str(i) + " ; echo Inter-arrival mean time: " + str(inter_arrive_meanTime) + " ; echo Write: " + str(write) + " ; echo Read: " + str(read) + " ; echo Number of workers: " + str(id_worker), shell=True)
            
            subprocess.call('./QueueSimulator/single ' + str(inter_arrive_meanTime) + ' ' +
            str(service_time) + ' ' + str(operation_number) + " ; echo Total Size: " + str(size_storage) + " ; echo \n", shell=True)

            
        subprocess.call('make clean > /dev/null; cd QueueSimulator/ ; make clean >/dev/null ; cd ..', shell=True)

    else:
        print("Error - Introduce los argumentos correctamente")
        print('Ejemplo: middleware.py 1 1')


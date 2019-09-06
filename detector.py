import re
import csv

class Detector():
    #ejecuta la expresion regular y escibe en un  fichero 
    def parser(self, file_name, reg_exp, output_file_name):
        data_to_return = []
        with open(file_name, newline='') as File:  
            reader = csv.reader(File)
            for datos_a_tratar in reader:
                match_reg_exp = re.findall(reg_exp, str(datos_a_tratar))
                if match_reg_exp != [] :
                    data_to_return.append(match_reg_exp)
                data_regExp = str(match_reg_exp).strip('[]')
                print("-----------------___>>>>>>>----->>>> " + data_regExp)
                #data_to_return.append(data_regExp)
                evidences = open (output_file_name,'a')
                evidences.write(data_regExp)
                evidences.close()
                
            return data_to_return
    
    # recibe una lista de expresiones regulares y opcionalmente el nombre del fichero donde que va a parsear
    def run(self, reg_exps, output_file_name,file_name='web.csv'):
        for reg_exp in reg_exps:   
            return self.parser(file_name,reg_exp,output_file_name)



#bitcoin_reg_exps = [r'[1 3][a-km-zA-HJ-NP-Z1-9]{25,34}',r'0x[a-z0-9]{40}',r'[a-fA-F0-9]{64}']

#evidences_reg_exps = [r'(?:https?\:\/\/)?[\w\-\.]+\.onion',r'([\w\.,]+@[\w\.,]+\.\w+)']
#Detector().run(reg_exps=bitcoin_reg_exps, file_name='/home/wolfsburg/Escritorio/TFM/forocoches.csv',output_file_name='test.txt')

import re
import csv

class Detector():
    #ejecuta la expresion regular y escibe en un  fichero 
    def parser(self, file_name, reg_exp, out_file):
        with open(file_name, newline='') as File:  
            reader = csv.reader(File)
            for datos_a_tratar in reader:
                match_reg_exp = re.findall(reg_exp, str(datos_a_tratar))
                data_regExp = str(match_reg_exp).strip('[]')
                print(data_regExp)
                evidences = open (output_file_name,'a')
                evidences.write(data_regExp)
                evidences.close()
    
    # recibe una lista de expresiones regulares y opcionalmente el nombre del fichero donde que va a parsear
    def run(self, reg_exps, file_name='web.csv', output_file_name='evidences.txt'):
        for reg_exp in reg_exps:   
            self.parser(file_name,reg_exp,output_file_name)



bitcoin_reg_exps = [r'[1 3][a-km-zA-HJ-NP-Z1-9]{25,34}',r'0x[a-z0-9]{40}',
r'(?:https?\:\/\/)?[\w\-\.]+\.onion',r'([\w\.,]+@[\w\.,]+\.\w+)',r'[a-fA-F0-9]{64}']
Detector().run(reg_exps=bitcoin_reg_exps, file_name='/home/wolfsburg/Escritorio/TFM/forocoches.csv',output_file_name='test.txt')

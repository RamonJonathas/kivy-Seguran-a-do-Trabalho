

resposta = str('..')

    
def dimensionamento_sesmt(grau,numero_trabalhadores):
    global resposta

    if grau == int(1):
        if numero_trabalhadores <501:
            resposta = 'sem sesmt'
        elif numero_trabalhadores >500 and numero_trabalhadores <1001:
            resposta ='1 tecnico de enfermagem'
        elif numero_trabalhadores >1000 and numero_trabalhadores <2001:
            resposta ='1 tec seguranca do trabalho e 1 medico do trabalho*'
        elif numero_trabalhadores >2000 and numero_trabalhadores <3501:
            resposta = '1 tec de segurança do trabalho \n 1 eng seguranca* \n 1 tec de enfermagem*** \n 1 medico do trablho* '
        elif numero_trabalhadores >3500 and numero_trabalhadores <5001:
            resposta = '2 tec segurança\n1 eng de segurança* \n 1 tec de enfermagem \n  1 enfermeiro do trabalho* \n 1 medico do trabalho'
        elif numero_trabalhadores >5000:
            resposta = '1 técnico de segurança, 1 engenheiro de segurança do trabalho* , 1 técnico de enfermagem, 1 médico do trabalho*'    
    
    elif grau == int(2):
        if numero_trabalhadores <501:
            resposta = 'sem sesmt'
        elif numero_trabalhadores >500 and numero_trabalhadores <1001:
            resposta ='1 tecnico de enfermagem'
        elif numero_trabalhadores >1000 and numero_trabalhadores <2001:
            resposta ='1 técnico de seguranca do trabalho, 1 engenheiro de segurança do trabalho*, 1 técnico de enfermagem*** e 1 médico do trabalho*'
        elif numero_trabalhadores >2000 and numero_trabalhadores <3501:
            resposta = '2 técnicos de segurança do trabalho, 1 engenheiro de segurança do trabalho*, 1 técnico de enfermagem*** e 1 medico do trabalho'
        elif numero_trabalhadores >3500 and numero_trabalhadores <5001:
            resposta = '5 técnicos de segurança do trabalho, 1 engenheiro de segurança do trabalho, 1 técnico de enfermagem, 1 enfermeiro do trabalho e 1 médico do trabalho'
        elif numero_trabalhadores >5000:
            resposta = '1 técnico de segurança do trabalho , 1 engenheiro de segurança do trabalho* , 1 técnico de enfermagem, 1 médico do trabalho'    
    
    elif grau == int(3):
        if numero_trabalhadores >49 and numero_trabalhadores <101:
            resposta = 'sem sesmt'  
        elif numero_trabalhadores >100 and numero_trabalhadores <251:
            resposta = '1 técnico de enfermagem,'
        elif numero_trabalhadores >250 and numero_trabalhadores <501:
            resposta = '2 técnicos de enfermagem'
        elif numero_trabalhadores >500 and numero_trabalhadores <1001:
            resposta = '3 técnicos de segurança do trabalho, 1 enegenheiro de segurança do trabalho*, 1 médico do trabalho*'
        elif numero_trabalhadores >1000 and numero_trabalhadores <2001:
            resposta = '4 técnicos de segurança do trabalho,1 engenheiro de segurança do trabalho, 1 técnico de enfermagem*** e 1 médico do trabalho'
        elif numero_trabalhadores >2000 and numero_trabalhadores <3501:
            resposta = '6 técnicos de segurança do trabalho, 1 engenheiro de segurança do trabalho, 1 técnico de enfermagem, 1 enfermeiro do trabalho e 1 médicos do trabalho* '
        elif numero_trabalhadores >3500 and numero_trabalhadores <5001:
            resposta = '8 técnicos de segurança do trabalho, 2 engenheiros de segurança do trabalho,1 técnico de enfermagem, 1 enfermeiro do trabalho e 2 médicos do trabalho'
        elif numero_trabalhadores >5000:
            resposta = '3 técnicos de segurança do trabalho , 1 engenheiro de segurança do trabalho , 1 técnico de enfermagem e 1 médico do trabalho'    
    
    elif grau == int(4):
        if numero_trabalhadores >49 and numero_trabalhadores <101:
            resposta = '1 engenheiro de segurança do trabalho'  
        elif numero_trabalhadores >100 and numero_trabalhadores <251:
            resposta = '2 técnicos de segurança do trabalho, 1 engenheiro de segurança do trabalho* e 1 médico do trabalho*'
        elif numero_trabalhadores >250 and numero_trabalhadores <501:
            resposta = '3 técnicos de segurança do trabalho, 1 engenheiro de segurança do trabalho* e 1 médico do trabalho*'
        elif numero_trabalhadores >500 and numero_trabalhadores <1001:
            resposta = '4 técnicos de segurança do trabalho, 1 engenheiro de segurança do trabalho, 1 técnico de enfermagem*** e 1 médico do trabalho'
        elif numero_trabalhadores >1000 and numero_trabalhadores <2001:
            resposta = '5 técnicos de segurança do trabalho, 1 engenheiro de segurança do trabalho e 1 médico do trabalho*'
        elif numero_trabalhadores >2000 and numero_trabalhadores <3501:
            resposta = '8 técnicos de segurança do trabalho, 2 engenheiros de segurança do trabalho, 1 técnico de enfermagem, 1 enfermeiro do trabalho e 2 médicos do trabalho'
        elif numero_trabalhadores >3500 and numero_trabalhadores <5001:
            resposta = '10 técnicos de segurança do trabalho, 3 engenheiros de segurança do trabalho, 1 técnico de enfermagem,1 enfermeiro do trabalho e 2 médicos do trabalho'
        elif numero_trabalhadores >5000:
            resposta = '3 técnicos de segurança do trabalho, 1 engenheiro de segurança do trabalho e 1 médico do trabalho*'
    


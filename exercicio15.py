hora = float(input('digite quanto vc ganha por hora trabalhada: '))
horames = float(input('digite quantas horas vc trabalha por mes: '))

salario = hora * horames
IR = 0.11
INSS = 0.08
SINDICATO = 0.05
LIQUIDO = 0.76

print(
    "+ Salário Bruto : R$ {:.2f} \n"
    "- IR (11%) : R$ {:.2f} \n"
    "- INSS (8%) : R$ {:.2f} \n"
    "- Sindicato (5%) : R$ {:.2f} \n"
    " \nSalário Liquido : R$ {:.2f}"

        .format(salario, salario * IR, salario * INSS, salario * SINDICATO, salario * LIQUIDO)

)

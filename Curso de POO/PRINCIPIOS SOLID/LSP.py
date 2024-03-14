# FORMA NO OPTIMA YA QUE LA SUBCLASE NO PUEDE HACER LO MISMO QUE LA CLASE BASE
# class Ave:
#     def volar(self):
#         return "Estoy volando"
    
# class Pinguino(Ave):
#     def volar(self):
#         return "No puedo volar"
    
# def hacer_volar(ave = Ave): #VARIABLE DE PARAMETRO
#     return ave.volar()

#FORMA OPTIMA USANDO EL PRINCIPIO LSP

# class Ave:
#     pass

# class AveVoladora(Ave):
#     def volar(self):
#         return "Estoy volando"
    
# class AveNoVoladora(Ave):
#     pass
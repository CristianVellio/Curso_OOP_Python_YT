#CODIGO OPTIMO SIGUIENDO PRINCIPIOS SOLID

import os
from openai import OpenAI

client = OpenAI(api_key="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")
OpenAI.api_key = os.getenv ("OPENAI_API_KEY")
system_init = '''Hace de cuenta que sos un analizador de sentimientos.
                 Yo te paso sentimientos y vos analizas de los mensajes 
                 y me das una respuesta con al menos 1 carcater y como maximo 4 caracteres
                 SOLO RESPUESTAS NUMERICAS. Donde -1 es negatividad maxima, 0 es neutral y 1 es positividad maxima.
                 Podes ir entre esos rangos, es decir 0.3, -0.5 etc tambien son validos.
                 (Podes responder solo con ints o floats)'''
                 
mensajes = [{"role": "system", "content": system_init}]

class Sentimiento: #CREAMOS LA CLASE SENTIMIENTOS RESPONSABILIDAD UNICA REPRESENTAR SENTIMIENTO
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color
        
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color,self.nombre)

class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos = rangos
    #CLASE ANALIZADOR DE SENT TIENE LA RESP DE MAPEAR POLARIDADES A SENT (DEF CUAL VA A SER EL SENT)
    #CUMPLE OCP YA QUE PODEMOS SEGUIR AHREHANDO RANGOS SIN MODIFICAR EL CODIGO
    def analizar_sentimiento(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("Muy Negativo", "31")
    
rangos = [
    ((-0.6,-0.3), Sentimiento("Negativo","31")),
    ((-0.3,-0.1), Sentimiento("Algo Negativo","31")),
    ((-0.1,0.1), Sentimiento("Neutral","33")),
    ((0.1,0.4), Sentimiento("Algo Positivo","32")),
    ((0.4,0.9), Sentimiento("Positivo","32")),
    ((0.9,1), Sentimiento("Muy Positivo","32"))
]

        #CUMPLIMOS EL DIP YA QUE NO DEPENDEMOS DE UNA BIBLIOTECA EXTERNA
analizador = AnalizadorDeSentimientos(rangos)

while True:
    user_prompt = input("\x1b[1;33m" +"\nDecime algo: " + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt}) #de esta forma estamos dando la orden a CHATG que analice lo escrito por el usuario
    
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 8
    )
    
    respuesta = completion.choices[0].message.content
    mensajes.append({"role": "assistant", "content": respuesta}) #AGREGANDO LA RESPUESTA QUE NOS DA EL CHATBOT
    
    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)
    
    #PODEMOS HACER ESTO CON TEXTBLOAT EN IDIOMA INGLES SIN PAGAR API KEYS DE OPENAI
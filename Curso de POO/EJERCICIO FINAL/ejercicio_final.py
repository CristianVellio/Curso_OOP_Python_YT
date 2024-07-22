# import os
# from openai import OpenAI

# client = OpenAI(api_key="??????????????????????????????????????????")
# OpenAI.api_key = os.getenv ("OPENAI_API_KEY")
# system_init = '''Hace de cuenta que sos un analizador de sentimientos.
#                  Yo te paso sentimientos y vos analizas de los mensajes 
#                  y me das una respuesta con al menos 1 carcater y como maximo 4 caracteres
#                  SOLO RESPUESTAS NUMERICAS. Donde -1 es negatividad maxima, 0 es neutral y 1 es positividad maxima.
#                  Podes ir entre esos rangos, es decir 0.3, -0.5 etc tambien son validos.
#                  (Podes responder solo con ints o floats)'''
                 
# mensajes = [{"role": "system", "content": system_init}]

# class AnalizadorDeSentimientos:
#     def analizar_sentimiento(self, polaridad):
#         if polaridad > -0.8 and polaridad <= -0.3:
#             return "\x1b[1;31m" + "Negativo" + "\x1b[0;37m" #ESTO ES PARA DARLE COLOR AL TEXTO
#         elif polaridad > -0.3 and polaridad < -0.1:
#             return "\x1b[1;31m" + "Algo Negativo" + "\x1b[0;37m"
#         elif polaridad >= -0.1 and polaridad <= 0.1:
#             return "\x1b[1;33m" + "Neutral" + "\x1b[0;37m"
#         elif polaridad >= -0.1 and polaridad <= 0.4:
#             return "\x1b[1;32m" + "Algo positivo" + "\x1b[0;37m"
#         elif polaridad >= -0.4 and polaridad <= 0.9:
#             return "\x1b[1;32m" + "Positivo" + "\x1b[0;37m"
#         elif polaridad > 0.9:
#             return "\x1b[1;32m" + "Muy positivo" + "\x1b[0;37m"
#         else:
#             return "\x1b[1;31m" + "Muy Negativo" + "\x1b[0;37m"
        
# analizador = AnalizadorDeSentimientos()

# while True:
#     user_prompt = input("\x1b[1;33m" +"\nDecime algo: " + "\x1b[0;37m")
#     mensajes.append({"role": "user", "content": user_prompt}) #de esta forma estamos dando la orden a CHATG que analice lo escrito por el usuario
    
#     completion = client.chat.completions.create(
#         model = "gpt-3.5-turbo",
#         messages = mensajes,
#         max_tokens = 8
#     )
    
#     respuesta = completion.choices[0].message.content
#     mensajes.append({"role": "assistant", "content": respuesta}) #AGREGANDO LA RESPUESTA QUE NOS DA EL CHATBOT
    
#     sentimiento = analizador.analizar_sentimiento(float(respuesta))
#     print(sentimiento)

produto =float(input("Insira o valor do produto:\n"))

parcelas=int(input("insira a quantidade de parcelas que deseja(para pagamento à vista digite 0):\n"))

if(parcelas==0):
        print("Seu pagamento não terá acrescimo, agradecemos pela compra!")

else:

 if(parcelas<=3):

   x1=produto*0.1

   x2=produto+x1

   x3=x2/parcelas

   print("O valor do seu produto agora é de:",x2, "\nO valor das parcelas é de:",x3)

 else:

   if (parcelas>=4):

     x1=produto*0.2

     x2=produto+x1

     x3=x2/parcelas

     print("O valor do seu produto agora é de:",x2, "\nO valor das parcelas é de:",x3)

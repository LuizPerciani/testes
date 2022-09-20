<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <style type="text/css">
      body {
          font-family: Calibri;
      }
      h2, p {
          font-weight: 900;
      }
    </style>

    <script type="text/javascript">

        //a seguir definimos uma arrow function (função de seta):
        valorParcelas = (valorCompra, qtdeParcelas) => {
            if (qtdeParcelas <= 2) { //sem juros
                return (valorCompra/qtdeParcelas).toFixed(2); //formatamos com duas casas decimais
            }
            else { //com juros de 5%
                let vp = (valorCompra + 5/100*valorCompra) / qtdeParcelas;
                return vp.toFixed(2); //resultado formatado com duas casas decimais
                //toPrecision(n) -> qtde total de dígitos
                //toFixed(n) -> qtde de casas decimais (depois do ponto)                
            }
        }

        function valorParcelas_V02(valorCompra, qtdeParcelas) {
            if (qtdeParcelas <= 2) { //sem juros
                return (valorCompra/qtdeParcelas).toFixed(2); //formatamos com duas casas decimais
            }
            else { //com juros de 5%
                let vp = (valorCompra + 5/100*valorCompra) / qtdeParcelas;
                return vp.toFixed(2); //resultado formatado com duas casas decimais
                //toPrecision(n) -> qtde total de dígitos
                //toFixed(n) -> qtde de casas decimais (depois do ponto)                
            }
        }

        //inicialmente solicitaremos os dados ao usuário:
        var vc = Number(prompt("Digite o valor da compra: "));
        var qp = Number(prompt("Digite a quantidade de parcelas: "));
    </script>

</head>

<body>

    <h2>Compra parcelada</h2>

    <p>Dados fornecidos</p>

    Valor da compra: R$ 
      <script type="text/javascript"> 
            document.write(vc.toFixed(2));
      </script> <br/>

    Quantidade de parcelas: 
      <script type="text/javascript"> 
           document.write(qp); 
      </script> <br/>

    <p>Resultado</p>
    
    Valor das parcelas: R$ 
      <script type="text/javascript"> 
        document.write( valorParcelas(vc, qp) + "<br/><br/>" ); 
        document.write( "Usando uma função tradicional: " + valorParcelas_V02(vc, qp) + "<br/>" ); 
    </script>

</body>

</html>

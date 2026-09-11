---
id: cardionet-conexao-cnet
categoria: CardioNet
produtos: [CardioNet Client, CardioNet Server, Portal CardioNet]
titulo: "O CardioNet não conecta / exame não sobe para o Portal CardioNet"
volume_suri: "102 casos em 3 meses"
fontes: ["Notas internas do projeto de integração DICOM/CardioNet"]
status: "⚠️ rascunho — validar com Filipe"
---

## Resposta rápida (bot / primeira mensagem) — versão preliminar

Falha de conexão do CardioNet costuma ser um destes três casos:

1. **Sem acesso à internet** no computador onde o Client/Server está instalado (checar navegação básica primeiro).
2. **Firewall/antivírus corporativo bloqueando** a comunicação do software com o servidor Cardios.
3. **Credencial incorreta ou expirada** — as credenciais de conexão são as mesmas da conta do serviço de saúde no Portal CardioNet.

## Passo a passo para orientar o cliente

1. Confirmar se o computador tem internet funcionando normalmente (fora do CardioNet).
2. Pedir para tentar acessar o Portal CardioNet pelo navegador com as mesmas credenciais — se não conseguir logar ali também, é problema de credencial, não de conexão do software.
3. Se o portal abre normalmente mas o software não conecta, orientar a checar com o TI do cliente se há bloqueio de firewall/antivírus.

## Quando escalar para atendimento humano

- Portal acessível e credenciais corretas, mas o software Client/Server continua sem conectar.
- Suspeita de bloqueio de rede que o cliente não consegue resolver sozinho (nível 1 não deve tentar abrir portas remotamente).

## Fonte / observações

⚠️ Este artigo foi montado com base no que já sabíamos do projeto de integração CardioNet/DICOM (não é um manual de troubleshooting oficial) — é o que mais precisa da revisão do Filipe antes de virar conteúdo final, incluindo confirmar quais portas/URLs específicas costumam ser bloqueadas.

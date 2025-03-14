# Conversor de Temperatura

Este projeto é um conversor de temperatura desenvolvido em Python. Ele permite converter valores entre Celsius, Fahrenheit e Kelvin, além de fornecer uma interface gráfica para facilitar a interação do usuário.

## Funcionalidades
- Conversão entre as escalas Celsius, Fahrenheit e Kelvin.
- Interface gráfica utilizando Tkinter.
- Exibição de imagens representando a sensação térmica (frio, aconchegante e quente).
- Opção de conversão via terminal.

## Tecnologias Utilizadas
- Python
- Tkinter (para interface gráfica)
- Pillow (para manipulação de imagens PNG)

## Como Executar

### Modo Gráfico
1. Certifique-se de ter o Python instalado.
2. Instale as dependências com:
   ```bash
   pip install pillow
   ```
3. Execute o script principal:
   ```bash
   python nome_do_arquivo.py
   ```

### Modo Terminal
1. Execute o script:
   ```bash
   python nome_do_arquivo.py
   ```
2. Escolha a conversão desejada digitando a letra correspondente.
3. Insira a temperatura e veja o resultado.

## Estrutura do Código
- **Funções de conversão**: Implementam a lógica para conversão de temperaturas.
- **Interface gráfica (Tkinter)**: Permite entrada de dados e exibição do resultado.
- **Determinação de clima**: Define a sensação térmica com base na temperatura.
- **Modo terminal**: Permite a conversão via linha de comando.

## Exemplo de Uso
### Modo Gráfico
1. Digite a temperatura desejada.
2. Escolha a conversão no menu suspenso.
3. Clique no botão "Converter".
4. O resultado será exibido na tela junto com a imagem correspondente.

### Modo Terminal
```bash
Escolha uma letra
a - Celsius para Fahrenheit
b - Celsius para Kelvin
c - Fahrenheit para Celsius
d - Fahrenheit para Kelvin
e - Kelvin para Celsius
f - Kelvin para Fahrenheit
```
Após escolher uma opção, insira a temperatura e visualize o resultado.

## Imagens
Certifique-se de que os arquivos de imagem (`Cold Emoji.png`, `Relieved Emoji.png` e `Hot Emoji.png`) estejam no mesmo diretório do script.

## Autor
Desenvolvido por [Seu Nome].

## Licença
Este projeto está licenciado sob a MIT License.


def celsius_para_fahrenheit(c):
  return (c * 9/5) + 32

def celsius_para_kelvin(c):
  return c + 273.15

def fahrenheit_para_celsius(f):
  return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
  return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
  return k - 273.15

def kelvin_para_fahrenheit(k):
  return (k - 273.15) * 9/5 + 32

def mostrar_menu():
  print("\n" + "="*50)
  print("       🌡️ CONVERSOR DE TEMPERATURA 🌡️")
  print("="*50)
  print("1. Celsius → Fahrenheit")
  print("2. Celsius → Kelvin")
  print("3. Fahrenheit → Celsius")
  print("4. Fahrenheit → Kelvin")
  print("5. Kelvin → Celsius")
  print("6. Kelvin → Fahrenheit")
  print("7. Sair")
  print("="*50)

def main():
  while True:
      mostrar_menu()
      escolha = input("Escolha uma opção (1 a 7): ")

      if escolha == '7':
          print("\n✅ Obrigado por usar o Conversor de Temperatura Python! ❄️🔥")
          break

      if escolha not in ['1', '2', '3', '4', '5', '6']:
          print("❌ Opção inválida. Tente novamente.")
          continue

      try:
          valor = float(input("Digite o valor da temperatura: "))
      except ValueError:
          print("❌ Por favor, insira um número válido.")
          continue

      if escolha == '1':
          resultado = celsius_para_fahrenheit(valor)
          print(f"{valor}°C = {resultado:.2f}°F")
      elif escolha == '2':
          resultado = celsius_para_kelvin(valor)
          print(f"{valor}°C = {resultado:.2f}K")
      elif escolha == '3':
          resultado = fahrenheit_para_celsius(valor)
          print(f"{valor}°F = {resultado:.2f}°C")
      elif escolha == '4':
          resultado = fahrenheit_para_kelvin(valor)
          print(f"{valor}°F = {resultado:.2f}K")
      elif escolha == '5':
          resultado = kelvin_para_celsius(valor)
          print(f"{valor}K = {resultado:.2f}°C")
      elif escolha == '6':
          resultado = kelvin_para_fahrenheit(valor)
          print(f"{valor}K = {resultado:.2f}°F")

if __name__ == "__main__":
  main()

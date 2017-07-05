def primo(n):
  i = 2
  cont = 0
  while i<n:
    if n%i == 0:
      cont += 1
    i += 1
  if cont==0: print("Primo")
  else: print("N primo")

primo(23)
primo(24)
primo(1)
primo(2)
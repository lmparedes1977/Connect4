def testa_vitoria(lista, lst):
  l1, l2 = lista, lst
  if testa_diagonal_menor(l1, l2) or testa_diagonal_maior(l1, l2) or testa_vertical(l1, l2) or testa_horizontal(l1, l2):
    return True
  else:
    return False


def testa_diagonal_menor(lista, lst):

    l1, l2 = lista, lst
    soma = {'3.0': 0, '4.0': 0, '5.0': 0, '6.0': 0, '6.1': 0, '6.2': 0}
    k = {'k1': 3, 'k2': 4, 'k3': 5, 'k4': 6, 'k5': 7, 'k6': 8}

    for i in range(6):
        for j in range(7):
            if j == (k['k1'] - i):  # 3.0
                if l1[i][j] == l2[0]:
                    soma['3.0'] += 1
                elif l1[i][j] != l2[0]:
                    soma['3.0'] = 0
                if soma['3.0'] == 4:
                    break
            if j == (k['k2'] - i):  # 4.0
                if l1[i][j] == l2[0]:
                    soma['4.0'] += 1
                elif l1[i][j] != l2[0]:
                    soma['4.0'] = 0
                if soma['4.0'] == 4:
                    break
            if j == (k['k3'] - i):  # 5.0
                if l1[i][j] == l2[0]:
                    soma['5.0'] += 1
                elif l1[i][j] != l2[0]:
                    soma['5.0'] = 0
                if soma['5.0'] == 4:
                    break
            if j == (k['k4'] - i):  # 6.0
                if l1[i][j] == l2[0]:
                    soma['6.0'] += 1
                elif l1[i][j] != l2[0]:
                    soma['6.0'] = 0
                if soma['6.0'] == 4:
                    break
            if j == (k['k5'] - i):  # 6.1
                if l1[i][j] == l2[0]:
                    soma['6.1'] += 1
                elif l1[i][j] != l2[0]:
                    soma['6.1'] = 0
                if soma['6.1'] == 4:
                    break
            if j == (k['k6'] - i):  # 6.2
                if l1[i][j] == l2[0]:
                    soma['6.2'] += 1
                elif l1[i][j] != l2[0]:
                    soma['6.2'] = 0
                if soma['6.2'] == 4:
                    break
            if 4 in soma.values():
                break
    return True if 4 in soma.values() else False



def testa_diagonal_maior(lista, lst):
  l1, l2 = lista, lst

  soma = {'2.0': 0, '1.0': 0, '0.0': 0, '0.1': 0, '0.2': 0, '0.3': 0}

  for i in range(6):
    for j in range(7):
      if j == i: # 0.0
        if l1[i][j] == l2[0]:
          soma['0.0'] += 1
        elif l1[i][j] != l2[0]:
          soma['0.0'] = 0
        if soma['0.0'] == 4:
          break
      if j == (i+1): # 0.1
        if l1[i][j] == l2[0]:
          soma['0.1'] += 1
        elif l1[i][j] != l2[0]:
          soma['0.1'] = 0
        if soma['0.1'] == 4:
          break
      if j == (i+2): # 0.2
        if l1[i][j] == l2[0]:
          soma['0.2'] += 1
        elif l1[i][j] != l2[0]:
          soma['0.2'] = 0
        if soma['0.2'] == 4:
          break
      if j == (i+3): # 0.3
        if l1[i][j] == l2[0]:
          soma['0.3'] += 1
        elif l1[i][j] != l2[0]:
          soma['0.3'] = 0
        if soma['0.3'] == 4:
          break
      if i == (j+1): # 1.0
        if l1[i][j] == l2[0]:
          soma['1.0'] += 1
        elif l1[i][j] != l2[0]:
          soma['1.0'] = 0
        if soma['1.0'] == 4:
          break
      if i == (j+2): # 2.0
        if l1[i][j] == l2[0]:
          soma['2.0'] += 1
        elif l1[i][j] != l2[0]:
          soma['2.0'] = 0
        if soma['2.0'] == 4:
          break
      if 4 in soma.values():
        break
  return True if 4 in soma.values() else False


def testa_vertical(lista, lst):
    soma = 0
    for i in range(7):
        soma = 0
        for j in range(6):
            if lista[j][i] == lst[0]:
                soma += 1
            elif lista[j][i] != lst[0]:
                soma = 0
            if soma == 4:
                break
        if soma == 4:
            break
    return True if soma == 4 else False


def testa_horizontal(lista, lst):
    soma = 0
    for i in range(6):
        soma = 0
        for j in range(7):
            if lista[i][j] == lst[0]:
                soma += 1
            elif lista[i][j] != lst[0]:
                soma = 0
            if soma == 4:
                break
        if soma == 4:
            break
    return True if soma == 4 else False




heckboard = np.zeros((8,8),dtype=int)
checkboard[::2,0::2] = 1
checkboard[1::2,1::2] = 1
print(checkboard)
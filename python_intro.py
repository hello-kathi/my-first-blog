def hi(name):
    print('Hi ' + str(name) + '!')
    
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')
for i in range(1, 6):
    hi(i)
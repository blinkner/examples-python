def calcularResistencia(v_fonte, v_led, i_led):
    '''Função para calcular a resistência necessária para um led.'''
    return (v_fonte - v_led) / i_led

v_fonte = float(input('Valor da fonte de tensão (V): '))
v_led = float(input('Valor da tensão do LED (V): '))
i_led = 0.020

print('Resistor necessário: ', calcularResistencia(v_fonte, v_led, i_led), ' ohms')
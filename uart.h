#ifndef _UART_H_
#define _UART_H_

#define TX_PIN 2

#define UART_START_BIT 0
#define UART_DATA_FIRST_BIT 1
#define UART_DATA_LAST_BIT 8
#define UART_PARITY_BIT 9
#define UART_STOP_BIT 10

int uart_putchar(char c);
void uart_init();

#endif

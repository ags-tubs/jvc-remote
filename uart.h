#ifndef _UART_H_
#define _UART_H_

#define TX_PIN 2

#define PARITY_NONE 0
#define PARITY_EVEN 1
#define PARITY_ODD 2
/* Parity Mode */
#define UART_PARITY_MODE PARITY_EVEN


#define UART_START_BIT 0
#define UART_DATA_FIRST_BIT 1
#define UART_DATA_LAST_BIT 8

#if UART_PARITY_MODE == PARITY_NONE
#define UART_STOP_BIT UART_DATA_LAST_BIT+1
#else
#define UART_PARITY_BIT UART_DATA_LAST_BIT+1
#define UART_STOP_BIT UART_DATA_LAST_BIT+2
#endif

int uart_putchar(char c);
void uart_init();

#endif
